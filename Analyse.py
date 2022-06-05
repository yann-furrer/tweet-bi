# import data file
import pandas as pd
from pathlib import Path

path  = str(Path(__file__).parent)
dr = pd.read_csv(path+"/Data/tweet.csv")
df = dr
del df["Unnamed: 0"]
df

# convertion des tweets en anglais pour les rendrent compatible avec la librairie Textblob et nltk
import deepl 
# api payante donc je l'économise

def translate_text():
    for i in range(len(df["lang"])):
        if(df["lang"][i] != "en"):
            target_language = "EN-GB"
            translator = deepl.Translator("bf4f4966-63b7-5b7c-7d58-98dbe75cee0a:fx") 
            result = translator.translate_text(df["text"][i], target_lang=target_language) 
            df.at[i, "text"] = result.text


# tokenization of word, delete of unused word 
import re
from nltk.corpus import stopwords
from nltk import word_tokenize, PorterStemmer, WordNetLemmatizer
import nltk
nltk.download('averaged_perceptron_tagger')
def tokenization():
    lemmatizer  = WordNetLemmatizer()

    stop_words = set(stopwords.words("english"))

    filtered_sentence = []
    # tweet_list_tokenized will countain every tweet tokenized 
    tweet_list_tokenized = {}
    ps = PorterStemmer()
    deleted_word = ["//", "http", "https"]

    for i in range(len(df)):
        # df.at[i, "text"] = result.text
        df.at[i, "text"] = re.sub(r'(@\[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|^rt|http.+?', '', df["text"][i])
        
        tweet_text = df["text"][i]
        word_tokens = word_tokenize(tweet_text)
        

        for element in word_tokens:
            # check if word exist in list of library
            if element not in stop_words :
                
                filtered_sentence.append(element)
                # delete the inflect of verbs
                # filtered_sentence.append(lemmatizer.lemmatize(ps.stem(element)))
                filtered_sentence.append(lemmatizer.lemmatize(element))
                # ps.stem enlève tt les suffixes et préfixe
        # define the class of word : verb noun, adjective ...
        wordlist = [w for w in filtered_sentence if not w in stop_words]
        tagged = nltk.pos_tag(wordlist)
    
        # update new list wich contain every sentence of tweet with snetence tokenized and sorted 
        tweet_list_tokenized.update({i : tagged})
        filtered_sentence = []
        tagged = []
        wordlist = []
    return tweet_list_tokenized

# NER name entity recognition, search if words belong to an category like location countries...
import pandas as pd
import nltk
nltk.download('maxent_ne_chunker')
nltk.download('words')

def entity_recongnition(tweet_list_tokenized=tokenization()):
    named_entities = []
    type_entities = []


    for i in range(len(tweet_list_tokenized)):
            chunked_text = nltk.ne_chunk(tweet_list_tokenized[i])


        
            for text in chunked_text:
                if hasattr(text, 'label'):
                
                    named_entities.append(' '.join(c[0] for c in text.leaves()))
                    type_entities.append(text.label())

    dte = pd.DataFrame()
    dte.insert(loc=len(dte.columns), column='name entity', value= type_entities)   
    dte.insert(loc=len(dte.columns), column='type entity', value= named_entities)   

    dte.drop_duplicates(subset ="type entity",
                        keep = False, inplace = True)
    dte.to_json(path+"/Data/entity.json")

from flair.models import TextClassifier
from flair.data import Sentence
import json
# load tagger
def sentence_feeling():
    # sentence feeling 
    temp_array = []
    type_sentence = []
    df
    classifier = TextClassifier.load('sentiment')
    for y in range(len(df["text"])):
        sentence = Sentence(df["text"][y])
        classifier.predict(sentence)
    
        temp_sentence = str(sentence.labels[0])
        temp_type_of_sentence = str(sentence.labels[0])
        if("NEGATIVE" in temp_sentence):
        
            temp_array.append(float(temp_sentence[10:-1])*-1)
            type_sentence.append(str(temp_type_of_sentence[:8]))
            # print(str(temp_type_of_sentence[:8]))
        else:
            temp_array.append(float(temp_sentence[10:-1])*1)
        
            type_sentence.append(str(temp_type_of_sentence[:8]))


        # print(str(sentence.labels[0]))
    df.insert(loc=len(df.columns), column='sentiment type', value= type_sentence)   

    col = len(df.columns) + 1 
    df.insert(loc=len(df.columns), column='sentiment value', value= temp_array)

df.to_csv(path+'/Data/tweet_clean.csv')
print("analysis complete")