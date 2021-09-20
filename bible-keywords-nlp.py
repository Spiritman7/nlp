## BIBLE KEYWORD EXTRACTION 


# 1. Spacy Method


import requests       # for API calls
import json           # for JSON manipulation 
import pandas as pd   # for data frame handling 
import spacy          # for nlp


# Import the English language model from spacy
nlp = spacy.load("en_core_web_lg")


book = "" 
chapter = ""
verse = ""
#text1 = ""
#text2 = ""


text1 = pd.DataFrame()
text2 = pd.DataFrame()
text3 = pd.DataFrame()

url = "https://getbible.net/json?passage="


# for some reason the API doesn't return true JSON responses, so insert the below
end = "&raw=true"   # place the raw data into JSON format ()

# The 1st Scripture reading
def get_text1():
    global book, chapter, verse, text1 # replace these variables with the previously used ones
    try:
        book = "Proverbs"
        chapter = "3"
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
        print("End of " + book + chapter)
    except json.decoder.JSONDecodeError:
        print("That's all the verses in " + book + " " + chapter + ".")
        
        
        

# The 2nd Scripture reading
def get_text2():
    global book, chapter, verse, text2 # replace these variables with the previously used ones
    try:
        book = "Psalms"
        chapter = "119"
        # verse = input("Enter the verse:")
        verse_int = 1         # Begin with verse 1
        #text1 = pd.DataFrame()
        text2 = []
        while True:           # If the above is successful....apply the following steps:
            verse = str(verse_int) # Convert the verse no into string format
            url_response = url + book + chapter + ":" + verse + end + "&version=web"
            response = requests.get(url_response).json()
            verse_upper = response["book"][0]["chapter"]   # digging through the nested JSON
            verse_lower = verse_upper[verse]["verse"]     # same as above
            print("Verse " + verse + ": " + verse_lower)
            verse_int = verse_int + 1    # increment the verse by 1 (move to the next verse)
            #text1.append("Verse " + verse + ": " + verse_lower)
            text2.append(verse_lower)        # eliminating the verse no is for my NLP project (I'll include it in another time) 
    except KeyError:
        print("End of" + book + chapter)
    except json.decoder.JSONDecodeError:
        print("That's all the verses in " + book + " " + chapter + ".")
        
        
# The 3rd Scripture reading
def get_text3():
    global book, chapter, verse, text3 # replace these variables with the previously used ones
    try:
        book = "Proverbs"
        chapter = "8"
        # verse = input("Enter the verse:")
        verse_int = 1         # Begin with verse 1
        #text1 = pd.DataFrame()
        text3 = []
        while True:           # If the above is successful....apply the following steps:
            verse = str(verse_int) # Convert the verse no into string format
            url_response = url + book + chapter + ":" + verse + end + "&version=web"
            response = requests.get(url_response).json()
            verse_upper = response["book"][0]["chapter"]   # digging through the nested JSON
            verse_lower = verse_upper[verse]["verse"]     # same as above
            print("Verse " + verse + ": " + verse_lower)
            verse_int = verse_int + 1    # increment the verse by 1 (move to the next verse)
            #text1.append("Verse " + verse + ": " + verse_lower)
            text3.append(verse_lower)        # eliminating the verse no is for my NLP project (I'll include it in another time) 
    except KeyError:
        print("End of" + book + chapter)
    except json.decoder.JSONDecodeError:
        print("That's all the verses in " + book + " " + chapter + ".")


# Return the Scriptures 
get_text1()
get_text2()
get_text3()


# Convert the lists to string objects (NLP tokenizers only accept string format)
string1=' '.join([str(item) for item in text1])
string2=' '.join([str(item) for item in text2])
string3=' '.join([str(item) for item in text3])


doc1 = nlp(string1)
doc2 = nlp(string2)
doc3 = nlp(string3)


print(doc1.ents)
print(doc2.ents)
print(doc3.ents) 


# 2. YAKE Method (Yet Another Keyword Extractor)

import yake
import matplotlib as mlt
import matplotlib.pyplot as plt


kw_extractor = yake.KeywordExtractor()  
language = "en"
max_ngram_size = 3
deduplication_threshold = 0.9
numOfKeywords = 20
custom_kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim = deduplication_threshold, top=numOfKeywords, features = None)
keywords = custom_kw_extractor.extract_keywords(string1)

for kw in keywords:
    print(kw)
    
    
# 3. BERT Method 

