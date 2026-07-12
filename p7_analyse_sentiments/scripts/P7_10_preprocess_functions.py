
# fonction de preprocessing

import re
import nltk
from nltk.corpus import wordnet
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer, SnowballStemmer


def preprocess(text,process=None):

    text = clean_text(text) # clean
    tokens = word_tokenize(text) # tokenize
    tokens = remove_stop_words(tokens) # stop words    
    
    if process == 'stem':
        tokens = stemmatize(tokens) #stemmatize
    elif process == 'lem':
        tokens = lemmatize(tokens) # lemmatize
        
    return " ".join(tokens)

 
def clean_text(text):
    text = re.sub(r'http\S+', '', text)
    text = re.sub(r'@\S+', '', text)
    text = re.sub('[^a-zA-Z0-9\s]','',text)
    text = str(text).lower()
    return text

def remove_stop_words(tokens):
    stop_words = stopwords.words("english")
    return [w for w in tokens if not w in stop_words]    

def stemmatize(tokens):
    stemmer = SnowballStemmer('english')
    return [stemmer.stem(item) for item in tokens] 
    
def lemmatize(tokens):

    lemmatizer = WordNetLemmatizer()
    nltk_tagged = nltk.pos_tag(tokens)  
    wordnet_tagged = map(lambda x: (x[0], nltk_pos_tagger(x[1])), nltk_tagged)

    lemmatized_tokens = []
    lemmatized_tokens = [lemmatizer.lemmatize(word, tag) if tag is not None else word for word, tag in wordnet_tagged ]
    
    return lemmatized_tokens


def nltk_pos_tagger(nltk_tag):
    """
    returns wordnet object from nltk tag
    """
    if nltk_tag.startswith('J'):
        return wordnet.ADJ
    elif nltk_tag.startswith('V'):
        return wordnet.VERB
    elif nltk_tag.startswith('N'):
        return wordnet.NOUN
    elif nltk_tag.startswith('R'):
        return wordnet.ADV
    else:          
        return None
