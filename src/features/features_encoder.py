# -*- coding: utf-8 -*-

import joblib
from sklearn.preprocessing import OrdinalEncoder
from working_path import PROJECT_PATH


FEATURES = ["workclass", "marital_status", "occupation", "relationship", "sex", "race"]


def fit_encoder(dataset):
    encoder = OrdinalEncoder().fit(dataset[FEATURES])
    print(encoder)
    with open(f"{PROJECT_PATH}/models/features_encoder.pkl", "wb") as fout:
        joblib.dump(encoder, fout)
    return encoder


def transform_features_with_encoder(dataset):
    with open(f"{PROJECT_PATH}/models/features_encoder.pkl", "rb") as filein:
        encoder = joblib.load(filein)

    dataset.loc[:, FEATURES] = encoder.transform(dataset[FEATURES])
    return dataset
