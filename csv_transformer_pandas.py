import pandas as pd
import numpy as np


def clean_titanic(df):
    bin_edges = [0, 18, np.inf]
    bin_labels = ["child", "adult"]
    df["age_group"] = pd.cut(df["Age"], bins=bin_edges, right=False, labels=bin_labels, ordered=False)

    df["age_group"] = df["age_group"].cat.add_categories("unknown")
    df["age_group"] = df["age_group"].fillna("unknown")

    df = df[["Name", "Pclass", "Fare", "age_group"]]
    df = df.rename(columns={"Name": "name", "Pclass": "p_class", "Fare": "fare"})

    return df

def main():
    df = pd.read_csv("titanic.csv")
    print(df)
    df = clean_titanic(df)
    df.to_csv("titanic_cleaned_by_pandas.csv", index=False)

if __name__ == "__main__":
    main()