# -*- coding: utf-8 -*-

import argparse
import pickle
import sklearn
import numpy as np
import pandas as pd
from sklearn.metrics import classification_report
from sklearn.model_selection import GridSearchCV


method_import = {"random_forest": "from sklearn.ensemble import RandomForestClassifier",
                 "naive_bayes": "from sklearn.naive_bayes import MultinomialNB",
                 "neighbors": "from sklearn.neighbors import KNeighborsClassifier",
                 "tree": "from sklearn.tree import DecisionTreeClassifier",
                 "mlp": "from sklearn.neural_network import MLPClassifier",
                 "svm": "from sklearn.svm import SVC",
                 "logistic": "from sklearn.linear_model import LogisticRegression"}


parameters = {"random_forest": {"random_state": [42], "n_estimators": (10, 20, 50), "max_depth": (3, 5, 10, 15)},
              "naive_bayes": {},
              "neighbors": {},
              "tree": {},
              "mlp": {},
              "svm": {},
              "logistic":{"max_iter": [1000]}}


class Modeling:
    def __init__(self, data, method, to_pred="target"):
        self.set_model_method_as_global(method_name=method)
        self.x = data.drop(columns=to_pred)
        self.y = data[to_pred]

    @staticmethod
    def set_model_method_as_global(method_name):
        exec(f"{method_import[method_name]} as model_method", globals())

    def searching_parameters(self, method, cv=10):
        gs_clf = GridSearchCV(model_method(), parameters[method],
                              cv=cv, n_jobs=-1)
        gs_clf.fit(self.x, self.y)

        return gs_clf.best_params_

    def training(self, parameters):
        model = model_method(**parameters)
        model.fit(self.x, self.y)
        self.test(model, self.x, self.y)
        return model

    @staticmethod
    def test(classifier, x, y):
        y_pred = classifier.predict(x)
        print("Classification Report:", classification_report(y, y_pred), sep="\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("-m", "--method", type=str,
                        help='Classification method',
                        required=True)

    args = parser.parse_args()

    df = pd.read_csv("../../data/processed/training_data_balanced.csv")
    ml = Modeling(df, args.method)
    prts = ml.searching_parameters(args.method)
    print(prts)
    ml.training(parameters=prts)
