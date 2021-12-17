# -*- coding: utf-8 -*-

from imblearn.over_sampling import SMOTE
from imblearn.under_sampling import RandomUnderSampler
from imblearn.pipeline import Pipeline


class Resampling:
    def __init__(self):
        self.pipeline = self.mount_pipeline()

    @staticmethod
    def mount_pipeline(over_proportion=0.75):
        over = SMOTE(sampling_strategy=over_proportion, random_state=42)
        under = RandomUnderSampler(sampling_strategy = 'majority', random_state=42)
        steps = [('o', over), ('u', under)]
        return Pipeline(steps=steps)

    def apply_pipeline(self, X, y):
        new_x, new_y = self.pipeline.fit_resample(X, y)
        return new_x, new_y
