import os

import nltk
import numpy as np

from main.models import LanguageProcessor

MODEL_FILE = 'language.npy'


def __setup_env():
    nltk.download('nps_chat')
    # other downloads


def initialize(data_path):
    if os.path.exists(f'{data_path}/{MODEL_FILE}'):
        LanguageProcessor.init(file=f'{data_path}/{MODEL_FILE}')
        return

    __setup_env()
    posts = nltk.corpus.nps_chat.xml_posts()[:10000]
    feature_sets = [(LanguageProcessor.dialogue_act_features(post.text), post.get('class')) for post in posts]
    size = int(len(feature_sets) * 0.1)
    train_set, test_set = feature_sets[size:], feature_sets[:size]
    classifier = nltk.NaiveBayesClassifier.train(train_set)
    np.save(f'{data_path}/{MODEL_FILE}', classifier)
    LanguageProcessor.init(classifier)
