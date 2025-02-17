# read the data from data source and asve in data_raw for furthur process

import os

from get_data import read_params,get_data

import argparse

def load_and_save(config_path):

    config = read_params(config_path)

    df = get_data(config_path)

    new_cols = [col.replace(" ","_") for col in df.columns]

    raw_data_path = config["load_data"]["raw_dataset_csv"]

    df.drop("type",axis=1,inplace=True)

    df.dropna(inplace=True)

    new_cols.remove("type")

    print(new_cols)

    df.to_csv(raw_data_path, sep=",", index=False, header = new_cols)

    print(df.head())

if __name__ == "__main__":

    args = argparse.ArgumentParser()

    args.add_argument("--config",default="params.yaml")

    parsed_args = args.parse_args()

    print(parsed_args.config)

    data = load_and_save(config_path=parsed_args.config)