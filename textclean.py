import nltk
import re
import string
import unicodedata
import ftfy
from nltk.corpus import stopwords

nltk.download('stopwords')


stop_words = set(stopwords.words('english'))

def remove_stopwords(text):
    words = text.split()
    filtered_words = [word for word in words if word.lower() not in stop_words]
    return " ".join(filtered_words)

def standardize_terms(text, replacements):
    for key, value in replacements.items():
        text = text.replace(key, value)
    return text

text = """
Thís ís à próblemátic téxt fíle!! It contains    **extra spaces** ,,,,, special characters!!!💥🔥🚀
Some words are misspelleddd,   and encoding  issues   liké thís cäusé problëms.    
        
Prices are inconsistent:  $29.99, 29.99 USD, 29,99$.

Emails & phone numbers may be embedded: contact@domain.com, (123)-456-7890.

Repeated punctuations!!!!! should be removed, along with **random symbols** like @@,##.

stopwords like "the", "is", and "a" appear often.

HTML tags might be present: <div>This is inside a div</div>

And sometimes, contractions won't expand: "can't", "won't", "shouldn't".

Random numeric values: 123456, 98765, 2024.
"""

clean_text = ftfy.fix_text(text)
clean_text = unicodedata.normalize('NFKD', clean_text).encode('ascii', 'ignore').decode()
clean_text = re.sub(r'<[^>]+>', ' ', clean_text)
clean_text = re.sub(r"can't", "cannot", clean_text)
clean_text = re.sub(r"won't", "will not", clean_text)
clean_text = re.sub(r"shouldn't", "should not", clean_text)
clean_text = re.sub(r'([!?.,])\1+', r'\1', clean_text)
clean_text = re.sub(r'[^\w\s.@-]', ' ', clean_text)
clean_text = re.sub(r'\s+', ' ', clean_text).strip()

print(clean_text.lower())
