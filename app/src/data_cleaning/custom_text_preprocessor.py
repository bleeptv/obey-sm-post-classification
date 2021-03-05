import nltk
from nltk.stem import WordNetLemmatizer, PorterStemmer
from string import punctuation
from gensim.utils import simple_preprocess
from gensim.parsing.preprocessing import STOPWORDS
from gensim.parsing.preprocessing import strip_punctuation
from gensim.parsing.preprocessing import strip_non_alphanum

nltk.download('wordnet')
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

def lemmatize_stemming(input_text):
    
    """ Turn a word into it's original, dictionary form (i.e. turning fried into fry)
    
    Parameters
    ----------
    input_text : str
        The word to convert to a language dictionary equivalent 
    
     Returns
    -------
    str
        lemmatized input text converted to language dictionary original word
        
    """
        
    if lemmatizer.lemmatize(input_text).endswith('e'):
        return lemmatizer.lemmatize(input_text)
  
    return stemmer.stem(input_text)

def preprocess(input_text):
    
    """ Turn a word into it's original, dictionary form (i.e. turning fried into fry)
    
    Parameters
    ----------
    input_text : str
        The word to convert to a language dictionary equivalent 
    
     Returns
    -------
    list
        List of all the words in the input text
        
    """
    result = []
    stripped_text = strip_punctuation(input_text.lower()).split(" ")
    filtered_stripped_text = filter(None, stripped_text)
    
    for token in filtered_stripped_text:
        if token not in STOPWORDS and len(token) > 3:
            result.append(lemmatize_stemming(token))
    return result