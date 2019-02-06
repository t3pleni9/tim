import nltk
import numpy as np


class NotInitializedException(Exception):
    pass


class LanguageProcessor:
    __instance = None

    def __init__(self, classifier):
        self.__classifier = classifier

    def speech_class(self, message):
        return self.__classifier.classify(message.apply(self.dialogue_act_features))

    @staticmethod
    def dialogue_act_features(post):
        features = {}
        for word in nltk.word_tokenize(post):
            features['contains({})'.format(word.lower())] = True
        return features

    @classmethod
    def init(cls, classifier=None, file=None):
        if cls.__instance is None:
            if file:
                binary_classifier = np.load(file)
                classifier = binary_classifier.item()
            cls.__instance = LanguageProcessor(classifier)

    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            raise NotInitializedException('language instance not initialized')

        return cls.__instance
