import pandas as pd
import numpy as np


def clean_titanic(df):
    df = df.copy()
    bin_edges = [0, 18, np.inf]
    bin_labels = ["child", "adult"]
    df["age_group"] = pd.cut(
        df["Age"], bins=bin_edges, right=False, labels=bin_labels, ordered=False
    )

    df["age_group"] = df["age_group"].cat.add_categories("unknown")
    df["age_group"] = df["age_group"].fillna("unknown")

    df = df[["Name", "Pclass", "Fare", "Survived", "Sex", "age_group"]]
    df = df.rename(
        columns={
            "Name": "name",
            "Pclass": "p_class",
            "Fare": "fare",
            "Survived": "survived",
            "Sex": "sex",
        }
    )

    return df


def survival_rate_by_age_and_sex(df):
    df = df.copy()
    df = df.groupby(["age_group", "sex"])["survived"].mean()
    return df


def fare_summary_by_class(df):
    df = df.copy()
    df = df.groupby("Pclass")["Fare"].agg(["mean", "count", "max"])
    return df


def merge_titanic_with_pclass_lookup(df):
    df = df.copy()
    pclass_lookup = pd.DataFrame(
        {
            "Pclass": [1, 2, 3],
            "class_name": ["First", "Second", "Third"],
            "deck_level": ["Upper", "Middle", "Lower"],
        }
    )
    merged = pd.merge(df, pclass_lookup, on="Pclass", how="left")
    return merged


def main():
    df = pd.read_csv("titanic.csv")

    df_clean = clean_titanic(df)
    df_clean.to_csv("titanic_cleaned_by_pandas.csv", index=False)

    print(fare_summary_by_class(df))

    print(survival_rate_by_age_and_sex(df_clean))

    print("length of titanic before merge: {0}".format(len(df)))
    merged = merge_titanic_with_pclass_lookup(df)
    print("length of titanic after merge: {0}".format(len(merged)))
    print(merged.head())


if __name__ == "__main__":
    main()
