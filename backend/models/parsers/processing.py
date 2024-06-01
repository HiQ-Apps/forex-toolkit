import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')

# Initialize stemmer
stemmer = PorterStemmer()
stop_words = set(stopwords.words('english'))

# Custom phrases dictionary
custom_phrases = {
    "fed": ["rate cut", "interest hike", "monetary policy"],
    "ecb": ["rate decision", "economic outlook"],
    "inflation": ["increasing", "decreasing", "stable"]
}

def replace_custom_phrases(text, custom_phrases):
    for key, phrases in custom_phrases.items():
        for phrase in phrases:
            # Replace phrase with a single token (e.g., fed_rate_cut)
            text = re.sub(r'\b' + re.escape(phrase) + r'\b', key + '_' + '_'.join(phrase.split()), text)
    return text

def preprocess_text(text):
    # Replace custom phrases
    text = replace_custom_phrases(text, custom_phrases)
    
    # Remove non-alphanumeric characters
    text = re.sub(r'\W', ' ', text)
    
    # Tokenize
    tokens = nltk.word_tokenize(text)
    
    # Convert to lower case and remove stop words
    tokens = [token.lower() for token in tokens if token.lower() not in stop_words]
    
    # Stemming
    tokens = [stemmer.stem(token) for token in tokens]
    
    return ' '.join(tokens)

def vectorize_text(texts):
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(texts)
    return X, vectorizer
