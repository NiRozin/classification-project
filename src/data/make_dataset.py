# -*- coding: utf-8 -*-
import io
import os
import requests
import pandas as pd
from working_path import PROJECT_PATH


def download_dataset(request_url, download_filename, output_filename, columns_name):
    output = f"{PROJECT_PATH}/data/raw/{output_filename}"
    if os.path.exists(output):
        print("arquivo já existe")
        return

    dataset_response = get_data_by_url(url=request_url.format(download_filename))
    dataset_as_df = setup_data_response_as_dataframe(data_response=dataset_response, columns=columns_name)
    dataset_as_df.to_csv(output, index=False)


def get_data_by_url(url):
    return requests.get(url).content


def setup_data_response_as_dataframe(data_response, columns):
    return pd.read_csv(io.BytesIO(data_response), names=columns)


if __name__ == "__main__":
    columns = ["age", "workclass", "fnlwgt", "education", "education_num",
               "marital_status", "occupation", "relationship", "race", "sex",
               "capital_gain", "capital_loss", "hours_per_week", "native_country",
               "salary"]
    dataset_url = "http://archive.ics.uci.edu/ml/machine-learning-databases/adult/{}"

    download_dataset(request_url=dataset_url, download_filename="adult.data",
                     output_filename="train_data.csv")
    download_dataset(request_url=dataset_url, download_filename="adult.test",
                     output_filename="train_data.csv")
