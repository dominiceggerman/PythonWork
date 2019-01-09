# Natural Language Processing with Python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.cross_validation import train_test_split
from sklearn.metrics import classification_report
from sklearn import pipeline
import nltk
import string

def textProcess(m):
    # 1. Remove punctuation
    # 2. Remove stop words
    # 3. Return list of clean words
    no_punc = [char for char in m if char not in string.punctuation]
    no_punc = "".join(no_punc)
    return[word for word in no_punc.split() if word.lower() not in stopwords.words("english")]

if __name__ == "__main__":
    # Download stopwords
    print("[First time] Download the 'stopwords' package (identifier).")
    nltk.download_shell()

    # Get messages
    messages = pd.read_csv("Natural Language Processing/SMSSpamCollection", sep="\t", names=["label", "message"])
    print(messages.describe())

    messages["length"] = messages["message"].apply(len)
    messages["message"].apply(textProcess)
    # Convert to vector
    bow_transform = CountVectorizer(analyzer=textProcess).fit(messages["message"])
    messages_bow = bow_transform.transform(messages["message"])
    # Sparsity (number of non-zero messages vs total messages)
    print("Sparsity:", (100 * messages_bow.nnz / (messages_bow.shape[0] * messages_bow.shape[1])))

    # Tfidf
    tfidf_transformer = TfidfTransformer().fit(messages_bow)
    tfidf_transformer.idf_[bow_transform.vocabulary_["university"]]
    messages_tfidf = tfidf_transformer.transform(messages_bow)

    # Train classifier
    spam_detect_model = MultinomialNB().fit(messages_tfidf, messages["label"])
    all_pred = spam_detect_model.predict(messages_tfidf)
    msg_train, msg_test, label_train, label_test = train_test_split(messages["message"], messages["label"], test_size=0)
    # Use pipeline to perform above
    pipe = pipeline([[
        ("bow", CountVectorizer(analyzer=textProcess)),
        ("tfidf", TfidfTransformer()),
        ("classifier", MultinomialNB())
    ]])
    pipe.fit(msg_train, label_train)
    pred = pipe.predict(msg_test)
    print(classification_report(label_test, pred))