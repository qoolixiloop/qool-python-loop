#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#used corpora as data input
from nltk.corpus import names
from nltk.corpus import movie_reviews
from nltk.corpus import brown

#used functionality for ML
import operator
import random
import nltk
from nltk.classify import apply_features

#feature extractor functions
def gender_features(word):
    """
        The first step in creating a classifier is deciding what features of the input are relevant,
        and how to encode those features. For this example, we’ll start by just looking at the
        final letter of a given name. The following feature extractor function builds a dic-
        tionary containing relevant information about a given name.

        The dictionary that is returned by this function is called a feature set and maps from
        features’ names to their values.  Feature names are case-sensitive strings that typically
        provide a short human-readable description of the feature. Feature values are values
        with simple types, such as Booleans, numbers, and strings.
        """
    return {'last_letter': word[-1]}

def gender_features2(name):
    """
        Typically, feature extractors are built through a process of trial-and-error, guided by
        intuitions about what information is relevant to the problem. It’s common to start with
        a “kitchen sink” approach, including all the features that you can think of, and then
        checking to see which features actually are helpful.
        A feature extractor that overfits gender features. The featuresets returned by this feature
        extractor contain a large number of specific features, leading to overfitting for the relatively small
        Names Corpus.
        """
    features = {}
    features["firstletter"] = name[0].lower()
    features["lastletter"] = name[-1].lower()
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        features["count(%s)" % letter] = name.lower().count(letter)
        features["has(%s)" % letter] = (letter in name.lower())
    return features

def gender_features3(word):
    """
        We adjust our feature extractor to include features for two-letter suffixes
        """

    return {'suffix1': word[-1:],'suffix2': word[-2:]}


def document_features(document, word_features):
    """
        A feature extractor for document classification, whose features indicate whether or not
        individual words are present in a given document.
        """
    document_words = set(document)
    features = {}
    for word in word_features:
        #features[key]=value, key=word, value=True/False
        features['contains(%s)' % word] = (word in document_words)
    return features

def pos_features(word, common_suffixes):
    """
        feature extractor function that checks a given word for common suffixes
        """
    features = {}
    for suffix in common_suffixes:
        # features[key]=value, key=suffix, value=True/False
        features['endswith(%s)' % suffix] = word.lower().endswith(suffix)
    return features

def pos_features2(sentence, i):
    """
        A part-of-speech classifier whose feature detector examines the context in which a word
        appears in order to determine which part-of-speech tag should be assigned. In particular, the identity
        of the previous word is included as a feature.
        """
    features = {"suffix(1)": sentence[i][-1:],
                "suffix(2)": sentence[i][-2:],
                "suffix(3)": sentence[i][-3:]}
    if i == 0:
        features["prev-word"] = "<START>"
    else:
        features["prev-word"] = sentence[i-1]
    return features

def pos_features3(sentence, i, history):
    """
        we must augment our feature
        extractor function to take a history argument, which provides a list of the tags that
        we’ve predicted for the sentence so far . Each tag in history corresponds with a word
        in sentence. But note that history will only contain tags for words we’ve already clas-
        sified, that is, words to the left of the target word. Thus, although it is possible to look
        at some features of words to the right of the target word, it is not possible to look at
        the tags for those words (since we haven’t generated them yet)
        """
    features = {"suffix(1)": sentence[i][-1:],
                "suffix(2)": sentence[i][-2:],
                "suffix(3)": sentence[i][-3:]}
    if i == 0:
        features["prev-word"] = "<START>"
        features["prev-tag"] = "<START>"
    else:
        features["prev-word"] = sentence[i-1]
        features["prev-tag"] = history[i-1]
    return features

class ConsecutivePosTagger(nltk.TaggerI):
    """
        Class inherits from nltk.TaggerI
        We can proceed to build our sequence classifier .
        During training, we use the annotated tags to provide the appropriate
        history to the feature extractor, but when tagging new sentences, we generate the his-
        tory list based on the output of the tagger itself.
        """
    def __init__(self, train_sents):
        """
                from training sentences
                determine feature set or train set (no instance variable)
                determine history set orpos-tags set (no instance variable)
                use it as classifier input into NaiveBayesClassifier
                """
        #feature set
        train_set = []
        for tagged_sent in train_sents:
            # list of tokens of one sentence
            untagged_sent = nltk.tag.untag(tagged_sent)
            history = []
            # i= index of token in sentence, word=token, tag= POS-tag
            for i, (word, tag) in enumerate(tagged_sent):
                featureset = pos_features3(untagged_sent, i, history)
                train_set.append( (featureset, tag) )
                history.append(tag)
        # classifier
        self.classifier = nltk.NaiveBayesClassifier.train(train_set)

    def tag(self, sentence):
        """"
                Method to predict tags for tokens of a new sentence
                Used by the inherited method: evaluate
                """
        #print "from tag method"
        history = []
        for i, word in enumerate(sentence):
            #print "sentence, i, history, word",sentence, i, history, word
            featureset = pos_features3(sentence, i, history)
            tag = self.classifier.classify(featureset)
            history.append(tag)
        return zip(sentence, history)

# Main
if __name__ == "__main__":
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "6.1 Supervised Classification" \
          "Classification is the task of choosing the correct class " \
          "label for a given input. In basic classification tasks, " \
          "each input is considered in isolation from all other inputs, " \
          "and the set of labels is defined in advance. A classifier is " \
          "called supervised if it is built based on training corpora " \
          "containing the correct label for each input."
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "call feature extractor function"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print gender_features('Shrek')
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "access one file in the corpus"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    infile = 'male.txt'
    fin = names.open(infile)
    print fin.read().strip()[1:100]
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "access the plaintext; outputs pure string of all files"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print names.raw().strip()[1:100]
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "E X A M P L E 1: Gender Identification"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "Gender Identification. " \
          "Now that we’ve defined a feature extractor, we need to prepare " \
          "a list of examples and corresponding class labels." \
          "(access just tokens/words in the corpus (list of strings), " \
          "add a feature (male/female) and store into list of tuples)"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    names_ = ([(name, 'male') for name in names.words('male.txt')] +
             [(name, 'female') for name in names.words('female.txt')])
    print names_[1:10]
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "shuffle the list of tuples"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    random.shuffle(names_)
    print names_[1:10]
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "Next, we use the feature extractor to process the names data, " \
          "and divide the resulting list of feature sets into a training " \
          "set and a test set. The training set is used to train a new " \
          "“naive Bayes” classifier."
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    featuresets = [(gender_features(n), g) for (n,g) in names_]
    train_set, test_set = featuresets[500:], featuresets[:500]
    classifier = nltk.NaiveBayesClassifier.train(train_set)
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "feature set"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print featuresets[1:10]
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "train set"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print train_set[1:10]
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "test set"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print test_set[1:10]
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "classifier"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print classifier
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "let’s test it out on some names that did not appear in" \
          " its training data"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print classifier.classify(gender_features('Neo'))
    print classifier.classify(gender_features('Trinity'))
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "We can systematically evaluate the classifier on a much larger " \
          "quantity of unseen data"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print nltk.classify.accuracy(classifier, test_set)
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "Finally, we can examine the classifier to determine which " \
          "features it found most effective for distinguishing the " \
          "names’ genders. This listing shows that the names in the " \
          "training set that end in a are female 38 times more often " \
          "than they are male, but names that end in k are male 31 times " \
          "more often than they are female. These ratios are known as " \
          "likelihood ratios, and can be useful for comparing different " \
          "feature-outcome relationships."
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    classifier.show_most_informative_features(5)
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "When working with large corpora, constructing a single list " \
          "that contains the features of every instance can use up a " \
          "large amount of memory. In these cases, use the function " \
          "nltk.classify.apply_features, which returns an object that " \
          "acts like a list but does not store all the feature sets " \
          "in memory"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    train_set = apply_features(gender_features, names_[500:])
    test_set = apply_features(gender_features, names_[:500])
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "train set"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print train_set[1:10]
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "test set"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print test_set[1:10]
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "E X A M P L E 2: Choosing the Right Features"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "Choosing the Right Features. " \
          "Example: A feature extractor that overfits gender features." \
          "—if you provide too many features, then the algorithm will" \
          " have a higher chance of relying on idiosyncrasies of your" \
          " training data that don’t generalize well to new examples." \
          " This problem is known as overfitting, and can be especially" \
          " problematic when working with small training sets"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print gender_features2('John')
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "accuracy is about 1% lower than the accuracy of a classifier" \
          " that only pays attention to the final letter of each name"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    featuresets = [(gender_features2(n), g) for (n, g) in names_]
    train_set, test_set = featuresets[500:], featuresets[:500]
    classifier = nltk.NaiveBayesClassifier.train(train_set)
    print nltk.classify.accuracy(classifier, test_set)
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "Once an initial set of features has been chosen, a very " \
          "productive method for refining the feature set is error " \
          "analysis. First, we select a development set, containing " \
          "the corpus data for creating the model. This development " \
          "set is then subdivided into the training set and the " \
          "dev-test set." \
          "The training set is used to train the model, " \
          "and the dev-test set is used to perform error analysis. " \
          "The test set serves in our final evaluation of the system."
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    train_names_ = names_[1500:]
    devtest_names_ = names_[500:1500]
    test_names_ = names_[:500]
    train_set = [(gender_features(n), g) for (n, g) in train_names_]
    devtest_set = [(gender_features(n), g) for (n, g) in devtest_names_]
    test_set = [(gender_features(n), g) for (n, g) in test_names_]
    classifier = nltk.NaiveBayesClassifier.train(train_set)
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "train set"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print train_set[1:10]
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "development set"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print devtest_set[1:10]
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "test set"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print test_set[1:10]
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "classifier"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print classifier
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "Using the dev-test set, we can generate a list of the " \
          "errors that the classifier makes when predicting name " \
          "genders"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    errors = []
    for (name, tag) in devtest_names_:
        guess = classifier.classify(gender_features(name))
        if guess != tag:
            errors.append((tag, guess, name))
    for (tag, guess, name) in sorted(errors)[1:10]:  # doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
        print 'correct=%-8s guess=%-8s name=%-30s' %(tag, guess, name)
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "Rebuilding the classifier with the new feature extractor, " \
          "we see that the performance on the dev-test dataset " \
          "improves by almost three percentage points." \
          "once we’ve used the dev-test set to help us develop the model, " \
          "we can no longer trust that it will give us an accurate idea " \
          "of how well the model would perform on new data. It is " \
          "therefore important to keep the test set separate, and unused," \
          " until our model development is complete"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    train_set = [(gender_features3(n), g) for (n, g) in train_names_]
    devtest_set = [(gender_features3(n), g) for (n, g) in devtest_names_]
    test_set = [(gender_features3(n), g) for (n, g) in test_names_]
    classifier = nltk.NaiveBayesClassifier.train(train_set)
    print nltk.classify.accuracy(classifier, devtest_set)
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "At that point, we can use the test set to evaluate how well" \
          " our model will perform on new input values"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print nltk.classify.accuracy(classifier, test_set)
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "E X A M P L E 3: Document Classification"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "Document Classification. " \
          "corpora where documents have been labeled with categories." \
          " Using these corpora, we can build classifiers that will " \
          "automatically tag new documents with appropriate category " \
          "labels. First, we construct a list of documents, labeled " \
          "with the appropriate categories (here: category=pos/neg )"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "length: ",len(movie_reviews.fileids())
    documents = [(list(movie_reviews.words(fileid)), category)
        for category in movie_reviews.categories()
        for fileid in movie_reviews.fileids(category)]
    random.shuffle(documents)
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "print two documents in data structure" \
          "[([text-tokens],category=pos/neg)," \
          "([text-tokens],category=pos/neg),...]"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "documents[0:2]"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "access elements (and part of it) in a list of tuples"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    for text, cat in documents[0:10]:
        if cat == u'pos':
            print cat, text[1:10]
    for text, cat in documents[0:10]:
        if cat == u'neg':
            print cat, text[1:10]
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "To limit the number of features that the classifier needs " \
          "to process, we begin by constructing a list of the 2,000 " \
          "most frequent words in the OVERALL corpus"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
    print (all_words.items())[1:10]
    print (all_words.keys())[1:10]
    print (all_words.values())[1:10]
    word_features = all_words.keys()[:2000]
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print " We can then define a feature extractor that simply checks " \
          "whether each of these words is present in a given document."
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    features = document_features(movie_reviews.words('pos/cv957_8737.txt'),
                            word_features)
    print features.items()[1:10]
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "...whether each of these words is present in EACH of the " \
          "given documents. "
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    featuresets = [(document_features(d,word_features), c)
                   for (d, c) in documents]
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "print elements in data structure" \
          "[({text-tokens of document 1:True/False},category=pos/neg)," \
          "({text-tokens of document 2:True/False},category=pos/neg),...]"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "length: ", len(featuresets)
    for text_dict, cat in featuresets[0:10]:
        if cat == u'pos':
            print cat, text_dict.items()[1:5]
    for text, cat in documents[0:10]:
        if cat == u'neg':
            print cat, text_dict.items()[1:5]
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "Now that we’ve defined our feature extractor, we can use " \
          "it to train a classifier to label new movie reviews"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    train_set, test_set = featuresets[100:], featuresets[:100]
    classifier = nltk.NaiveBayesClassifier.train(train_set)
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "At that point, we can use the test set to evaluate how well" \
          " our model will perform on new input values"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print nltk.classify.accuracy(classifier, test_set)
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "Apparently in this corpus, a review that mentions triple " \
          "is almost 8 times more likely to be negative than positive, " \
          "while a review that mentions fabric is about 6 times more " \
          "likely to be positive. " \
          "(for each run something else; because of random shuffle" \
          "of documents at the beginning, the documents in the " \
          "training set differ for ech run)"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    classifier.show_most_informative_features(5)
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "E X A M P L E 4: Part-of-Speech Tagging"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "Part-of-Speech Tagging. " \
          "In Chapter 5, we built a regular expression tagger that " \
          "chooses a part-of-speech tag for a word by looking at the " \
          "internal makeup of the word. However, this regular expression " \
          "tagger had to be handcrafted. Instead, we can train a classifier " \
          "to work out which suffixes are most informative. Let’s begin " \
          "by finding the most common suffixes"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    suffix_fdist = nltk.FreqDist()
    for word in brown.words():
        word = word.lower()
        suffix_fdist[(word[-1:])] += 1
        suffix_fdist[(word[-2:])] += 1
        suffix_fdist[(word[-3:])] += 1
    #list of keys (use suffix_fdist or suffix_fdist.keys())
    suffix_fdist_sorted = sorted(suffix_fdist.keys(), key=suffix_fdist.get,
                                 reverse=True)
    for key in suffix_fdist_sorted[:10]:
        print key, suffix_fdist[key]
    common_suffixes = suffix_fdist_sorted[:10]
    #list of tuples (use suffix_fdist.items())
    suffix_fdist_sorted = sorted(suffix_fdist.items(),key=operator.itemgetter(1),
                                 reverse=True)
    for items in suffix_fdist_sorted[:10]:
        print items
    common_suffixes_tuple = suffix_fdist_sorted[:10]
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "most common suffixes (keys of dictionary) and" \
          "their frequency distribution (dictionary)"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print common_suffixes[:10]
    print common_suffixes_tuple[:10]
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "Now that we’ve defined our feature extractor, we can use it " \
          "to generate a features set from tagged words in corpus "
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    tagged_words = brown.tagged_words(categories='news')[:5000]
    print "length of tagged words set: ", len(tagged_words)
    print tagged_words[:10]
    featuresets = [(pos_features(n, common_suffixes), g)
                   for (n, g) in tagged_words]
    print "length of features set: ", len(featuresets)
    for text_dict, cat in featuresets[0:10]:
        print cat, text_dict.items()[1:5]
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "... and train a new “decision tree” classifier"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    size = int(len(featuresets) * 0.1)
    train_set, test_set = featuresets[size:], featuresets[:size]
    classifier = nltk.DecisionTreeClassifier.train(train_set)
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "accuracy"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print nltk.classify.accuracy(classifier, test_set)
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "classify new word"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print classifier.classify(pos_features('cats', common_suffixes))
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "One nice feature of decision tree models is that they are " \
          "often fairly easy to interpret. We can even instruct NLTK " \
          "to print them out as pseudocode."
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print classifier.pseudocode(depth=4)
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "E X A M P L E 5: Exploiting Context"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "Exploiting Context. " \
          " contextual features often provide powerful clues about " \
          "the correct tag—for example, when tagging the word fly, " \
          "knowing that the previous word is a will allow us to " \
          "determine that it is functioning as a noun, not a verb." \
          "In order to accommodate features that depend on a word’s " \
          "context, we must revise the pattern that we used to define " \
          "our feature extractor. Instead of just passing in the word " \
          "to be tagged, we will pass in a complete (untagged) sentence, " \
          "along with the index of the target word."
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print pos_features2(brown.sents()[0], 6)
    print pos_features2(brown.sents()[0], 7)
    print pos_features2(brown.sents()[0], 8)
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "Now that we’ve defined our feature extractor, we can use it " \
          "to generate a features set from UNTAGGED sentences in corpus " \
          "Data structure of brown.tagged_sents():" \
          "[ [(sentence1-token1,POS-tag), (sentence1-tokens2,POS-tag),...]" \
          "  [(sentence2-token1,POS-tag), (sentence2-tokens2,POS-tag),...]" \
          "  ... ]"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    tagged_sents = brown.tagged_sents(categories='news')[0:5]
    print "length of tagged sentence set: ", len(tagged_sents)
    print tagged_sents[:3]
    featuresets = []
    for tagged_sent in tagged_sents:
        #list of tokens of one sentence
        untagged_sent = nltk.tag.untag(tagged_sent)
        #print "untagged sentece", untagged_sent
        # i= index of token in sentence, word=token, tag= POS-tag
        for i, (word, tag) in enumerate(tagged_sent):
            #print "i, (word tag)", i, word, tag
            featuresets.append(
                (pos_features2(untagged_sent, i), tag))
    print "length of features set: ", len(featuresets)
    for features, tag in featuresets[0:10]:
        print tag, features
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "... and train a new “decision tree” classifier"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    size = int(len(featuresets) * 0.1)
    train_set, test_set = featuresets[size:], featuresets[:size]
    classifier = nltk.NaiveBayesClassifier.train(train_set)
    print nltk.classify.accuracy(classifier, test_set)
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "E X A M P L E 6: Sequence Classification"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "Sequence Classification. " \
          "In order to capture the dependencies between related " \
          "classification tasks, we can use joint classifier models, " \
          "which choose an appropriate labeling for a collection " \
          "of related inputs. In the case of part-of-speech tagging, " \
          "a variety of different sequence classifier models can be " \
          "used to jointly choose part-of-speech tags for all the " \
          "words in a given sentence." \
          "One sequence classification strategy, known as consecutive " \
          "classification or greedy sequence classification, is to " \
          "find the most likely class label for the first input, " \
          "then to use that answer to help find the best label for " \
          "the next input. The process can then be repeated until " \
          "all of the inputs have been labeled. "
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    tagged_sents = brown.tagged_sents(categories='news')[:500]
    size = int(len(tagged_sents) * 0.1)
    train_sents, test_sents = tagged_sents[size:], tagged_sents[:size]
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "create new object of own class ConsecutivePosTagger." \
          "The initialization creates the features set and uses " \
          "the training sentence for the NaiveBayesClassifier." \
          "The method evaluate makes predictions on test sentences."
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    tagger = ConsecutivePosTagger(train_sents)
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "evaluate"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print tagger.evaluate(test_sents)
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "E X A M P L E 7: Other Methods for Sequence Classification"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "Other Methods for Sequence Classification" \
          "One shortcoming of this approach is that we commit to " \
          "every decision that we make. For example, if we decide " \
          "to label a word as a noun, but later find evidence that " \
          "it should have been a verb, there’s no way to go back " \
          "and fix our mistake. One solution to this problem is " \
          "to adopt a transformational strategy instead. " \
          "Transformational joint classifiers work by creating an " \
          "initial assignment of labels for the inputs, and then " \
          "iteratively refining that assignment in an attempt to " \
          "repair inconsistencies between related inputs."
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "Another solution is to assign scores to all of the possible " \
          "sequences of part-of-speech tags, and to choose the sequence " \
          "whose overall score is highest. This is the approach taken " \
          "by Hidden Markov Models. Hidden Markov Models are similar " \
          "to consecutive classifiers in that they look at both the " \
          "inputs and the history of predicted tags. However, rather " \
          "than simply finding the single best tag for a given word, " \
          "they generate a probability distribution over tags. These " \
          "probabilities are then combined to calculate probability " \
          "scores for tag sequences, and the tag sequence with the " \
          "highest probability is chosen. Unfortunately, the number " \
          "of possible tag sequences is quite large. Given a tag set " \
          "with 30 tags, there are about 600 trillion (3010) ways to " \
          "label a 10-word sentence. In order to avoid considering " \
          "all these possible sequences separately, Hidden Markov " \
          "Models require that the feature extractor only look at " \
          "the most recent tag (or the most recent n tags, where n " \
          "is fairly small)."
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print ""
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"


