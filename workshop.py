#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 13:28:27 2022

@author: johan
"""
import numpy as np
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics

print_hints = True


# use standard dataset, select two newsgroups, do not shuffle (each run is same data)
corpus = fetch_20newsgroups(subset='all', categories=['comp.sys.ibm.pc.hardware', 'rec.autos'])



if print_hints:
    print("Imported {corpussize} records".format(corpussize=len(corpus.data)))


# show two messages to get a feel of the contents
if print_hints:
    print("One message is:")
    print("-----------------------------------------------------------------------------------")
    print(corpus.data[1])
    print("-----------------------------------------------------------------------------------")
    print("Another message is:")
    print("-----------------------------------------------------------------------------------")
    print(corpus.data[2])
    print("-----------------------------------------------------------------------------------")


#split the data into random 70% for training and remainiing 30% for model testing
training_data, testing_data, training_targets, testing_targets = train_test_split(corpus.data, corpus.target,test_size=0.3)
if print_hints:
    print("Split the dataset into {training_size} and {testing_size} documents.".format(training_size=len(training_targets),testing_size=len(testing_targets)))


# Transform the documents (words) into vectors (number)
my_stop_words = frozenset(["the", "any","some"])
vectorizer = TfidfVectorizer(stop_words=my_stop_words)

# let the vectorizer know what words to expect and use in the model
vectorizer.fit(training_data)
if print_hints:
    print("The vectorizer can now transform documents to vectors.")
    print("The vectorizer recognizes {vocabulary_size} words.".format(vocabulary_size=len(vectorizer.vocabulary_)))


#print("These words are",vectorizer.vocabulary_)

    print()

# transform the training_data and testing_data to vectors
training_vectors = vectorizer.transform(training_data)
testing_vectors = vectorizer.transform(testing_data)


# use a naive bayes model
classifier = MultinomialNB() 
classifier = RandomForestClassifier(n_estimators=200)


# train the model using the vectorized training corpus
if print_hints:
    print("Beginning to train the model")

classifier.fit(training_vectors,training_targets )

if print_hints:
    print("Finished training the model")


# now see if the 30% we kept aside work for the model.
predicted_results = classifier.predict(testing_vectors)

if print_hints:
    print()
    print()
    print("The message:")
    print("-----------------------------------------------------------------------------------")
    print(testing_data[0])
    print("-----------------------------------------------------------------------------------")
    print("The message is predicted to belong to ",predicted_results[0])
    print("The message should belong to ",testing_targets[0])
    if testing_targets[0] == predicted_results[0]:
        print("This is correctly predicted.")
    else:
        print("This is not correctly predicted.")
    print()
    print()
        

# we know the classification from testing_targets and will compare these to the predcited values
if print_hints:
    print("Accuracy:",metrics.accuracy_score(testing_targets, predicted_results))
    print("Precision:",metrics.precision_score(testing_targets, predicted_results))
    print("Recall:",metrics.recall_score(testing_targets, predicted_results))
    print()


# lets see this in action
sentence = "My new game card is not working."
print("The sentence for experimenting is :",sentence )
experiment_vector = vectorizer.transform([sentence])
print("The model predicts that the sentence belongs to class ", classifier.predict(experiment_vector))
print("The scores (percentages) per class are", classifier.predict_proba(experiment_vector))
print()


sentence = "I prefer a BMW over a Mercedes any day."
print("The sentence for experimenting is :",sentence )
experiment_vector = vectorizer.transform([sentence])
print("The model predicts that the sentence belongs to class ", classifier.predict(experiment_vector))
print("The scores (percentages) per class are", classifier.predict_proba(experiment_vector))
print()


sentence = "Does the new Honda have a sound system?."
print("The sentence for experimenting is :",sentence )
experiment_vector = vectorizer.transform([sentence])
print("The model predicts that the sentence belongs to class ", classifier.predict(experiment_vector))
print("The scores (percentages) per class are", classifier.predict_proba(experiment_vector))
print()




