import requests      # to make API calls
import json          # for dealing with the JSON responses
import pandas as pd   # for data frames


### NLP Bible Project 

 """This is an in-depth analysis on David & Solomon with the two stories that made Israel's most prominent kings eternal sensations"""
 
 ##### Stage 1: API Call
 
 book = "" 
chapter = ""
verse = ""
#text1 = ""
#text2 = ""


text1 = pd.DataFrame()
text2 = pd.DataFrame()

url = "https://getbible.net/json?passage="


# for some reason the API doesn't return true JSON responses, so insert the below
end = "&raw=true"   # place the raw data into JSON format ()

# Story 1: David & Goliath

def get_text1():
    global book, chapter, verse, text1 # replace these variables with the previously used ones
    try:
        book = "1 Samuel"
        chapter = "17"
        # verse = input("Enter the verse:")
        verse_int = 1         # Begin with verse 1
        #text1 = pd.DataFrame()
        text1 = []
        while True:           # If the above is successful....apply the following steps:
            verse = str(verse_int) # Convert the verse no into string format
            url_response = url + book + chapter + ":" + verse + end + "&version=web"
            response = requests.get(url_response).json()
            verse_upper = response["book"][0]["chapter"]   # digging through the nested JSON
            verse_lower = verse_upper[verse]["verse"]     # same as above
            print("Verse " + verse + ": " + verse_lower)
            verse_int = verse_int + 1    # increment the verse by 1 (move to the next verse)
            #text1.append("Verse " + verse + ": " + verse_lower)
            text1.append(verse_lower)        # eliminating the verse no is for my NLP project (I'll include it in another time) 
    except KeyError:
        print("End of David & Goliath")
    except json.decoder.JSONDecodeError:
        print("That's all the verses in " + book + ".")


# Story 2: Solomon & the Two Prostitutes 

def get_text2():
    global book, chapter, verse, text2 # replace these variables with the previously used ones
    try:
        book = "1 Kings"
        chapter = "3"
        # verse = input("Enter the verse:")
        verse_int = 16         # Begin with verse 16
        #text2 = pd.DataFrame()
        text2 = []
        while True:           # If the above is successful....apply the following steps:
            verse = str(verse_int) # Convert the verse no into string format
            url_response = url + book + chapter + ":" + verse + end + "&version=web"
            response = requests.get(url_response).json()
            verse_upper = response["book"][0]["chapter"]   # digging through the nested JSON
            verse_lower = verse_upper[verse]["verse"]     # same as above
            print("Verse " + verse + ": " + verse_lower)
            verse_int = verse_int + 1    # increment the verse by 1 (move to the next verse)
            # text2.append("Verse " + verse + ": " + verse_lower)
            text2.append(verse_lower)        # eliminating the verse no is for my NLP project (I'll include it in another time) 
    except KeyError:
        print("End of Solomon's Judgment")
    except json.decoder.JSONDecodeError:
        print("That's all the verses in " + book + " " + chapter + ".")


# Return David's story
get_text1() 

# Return Solomon's story
get_text2()


# Return the text without the verse no's
text1
text2


# Convert the lists to string objects (NLP tokenizers only accept string format)
string1=' '.join([str(item) for item in text1])

# Convert the lists to string objects (NLP tokenizers only accept string format)
string2=' '.join([str(item) for item in text2])

text1 = string1
text2 = string2



#### Stage 2: NLP 

import nltk 
from nltk import sent_tokenize
from nltk import word_tokenize


print(type(text2))
print("\n")

print(text2)
print("\n")
print(len(text2))

# Tokenize the texts into sentences 
sentences1 = sent_tokenize(text1)
sentences2 = sent_tokenize(text2)

# How many sentences in David & Goliath?
print(len(sentences1))

# How many sentences in Solomon's Judgment?
print(len(sentences2))

# Tokenize texts by words 
words1 = word_tokenize(text1)
words2 = word_tokenize(text2)

### Text 1 - Text Mining 

from nltk.probability import FreqDist

# Find the most common words in David & Goliath
fdist = FreqDist(words1)
fdist.most_common(10)

# Plot the frequency distribution 
import matplotlib.pyplot as plt
fdist.plot(10)

""" What I find annoying with the results are the appearance of the stop words & punctuations. This blocks out the real insight from the data we're after. Let's sort this out. """

# Remove punctuation marks 
words1_no_punc = []

# Build a function to identify the punctuation marks 

for w in words1:
    if w.isalpha(): # if all the characters in the selected token are letters ... 
        words1_no_punc.append(w.lower())  # ...append into the empty list above 
        
# This is the text without punctuation marks 
print(len(words1_no_punc))   # No. of characters 
print(words1_no_punc)        # Text 1 without punctuations

# Plot the frequency distribution again 
fdist = FreqDist(words1_no_punc)
fdist.most_common(10)


# Stopwords removal
from nltk.corpus import stopwords

# Read stopwords into a variable
sw = stopwords.words('english')
print(sw)

# Function to remove stopwords
clean_words1 = []

for w in words1_no_punc:
    if w not in sw:
        clean_words1.append(w)
        
# Let's see the text without the stop words 
print(len(clean_words1))
print(clean_words1)


# Run the frequency distribution graph one more time 
fdist = FreqDist(clean_words1)
fdist.plot(10)


"""Let's introduce the wordcloud 

With this visual, the words that occur the 'most' will appear in large font, while words that appear the least will appear in smaller font"""


# Visualise words via WordCloud 
from wordcloud import WordCloud, ImageColorGenerator
import numpy as np
from PIL import Image


crown_mask = np.array(Image.open("crown.jpg"))

def transform_format(value): 
    if val == 0:
        return 255
    else:
        return val


transformed_crown_mask = np.ndarray((crown_mask.shape[0], crown_mask.shape[1]), np.int32)


wc = WordCloud(background_color='black', mask=crown_mask, max_words=1000).generate(text1)
plt.figure(figsize=(12,12))
plt.imshow(wc, interpolation = "bilinear")
plt.axis("off")


# Try with the Nigeria flag!!
#wc = WordCloud(background_color='white', mask=nigeria_flag, max_words=1000).generate(text1)
#image_colors=ImageColorGenerator(nigeria_flag)
#plt.figure(figsize=(12,12))
#plt.imshow(wc.recolor(color_func=image_colors), interpolation = "bilinear")
#plt.axis("off")


"""Excellent! Apart from the Philistines, David is the most mentioned entity in the story of his famous conquest against Goliath! 

The next one is for Solomon. """



### Text 2 - Text Mining 

# Find the most common words in David & Goliath
fdist = FreqDist(words2)
fdist.most_common(10)

fdist.plot(10)  

# Remove punctuation marks 
words2_no_punc = []

# Build a function to identify the punctuation marks 

for w in words2:
    if w.isalpha(): # if all the characters in the selected token are letters ... 
        words2_no_punc.append(w.lower())  # ...append into the empty list above 
        
        
# This is the text without punctuation marks 
print(len(words2_no_punc))   # No. of characters 
# print(type(words2_no_punc))
print(words2_no_punc)        # Text 1 without punctuations


# Plot the frequency distribution again 
fdist = FreqDist(words1_no_punc)
fdist.most_common(10)

fdist.plot(10)  

# Function to remove stopwords
clean_words2 = []

for w in words2_no_punc:
    if w not in sw:
        clean_words2.append(w)
        

# Let's see the text without the stop words 
print(len(clean_words2))
print(clean_words2)

# Run the frequency distribution graph one more time 
fdist = FreqDist(clean_words2)
fdist.plot(10)

wc = WordCloud(background_color='black', mask=crown_mask, max_words=1000).generate(text2)
plt.figure(figsize=(12,12))
plt.imshow(wc, interpolation = "bilinear")
plt.axis("off")

"""Great! The word 'son' appears the most, followed by king. This implies the king had the divine ability to make a decisive decision that would determine the fate of the baby boy's future, and he ultimately made the right decision courtesy of the wisdom of God operating in him."""