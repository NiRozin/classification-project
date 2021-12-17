# -*- coding: utf-8 -*-
import numpy as np
from working_path import PROJECT_PATH


def add_new_features(dataset):
    dataset["capital_variation"] = dataset.capital_gain - dataset.capital_loss
    dataset["is_american"] = np.where(dataset.native_country == " United-States", 1, 0)
    return dataset


def drop_features(dataset, columns=["education", "capital_loss", "capital_gain", "native_country"]):
    return dataset.drop(columns=columns)


def make_target(dataset):
    dataset["target"] = np.where(dataset.salary.str.replace(" ", "") == "<=50K", 1, 0)
    return dataset


def drop_nan_values(dataset):
    return dataset.dropna().reset_index(drop=True)


def saving_data(dataset, filename, columns=[['age', 'workclass', 'fnlwgt', 'education_num', 'marital_status',
                                             'occupation', 'relationship', 'race', 'sex', 'hours_per_week',
                                             'capital_variation', 'is_american', 'target']]):
    dataset[columns].to_csv(f"{PROJECT_PATH}/data/processed/{filename}")
