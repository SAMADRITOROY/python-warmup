from csv_transformer_pandas import clean_titanic, titanic_with_pclass_details
import pandas as pd
from pandas import testing
from pandas.api.types import CategoricalDtype
import numpy as np


def test_clean_titanic():
    input_df = pd.DataFrame(
        {
            "PassengerId": [1, 2, 3, 15],
            "Name": [
                "Braund, Mr. Owen Harris",
                "Cumings, Mrs. John Bradley (Florence Briggs Thayer)",
                "Heikkinen, Miss. Laina",
                "Vestrom, Miss. Hulda Amanda Adolfina",
            ],
            "Sex": ["male", "female", "female", "female"],
            "Age": [22, 38, 26, 14],
            "Pclass": [3, 1, 3, 3],
            "Fare": [7.25, 71.2833, 7.925, 7.8542],
            "Survived": [0, 1, 1, 0],
        }
    )

    expected_df = pd.DataFrame(
        {
            "name": [
                "Braund, Mr. Owen Harris",
                "Cumings, Mrs. John Bradley (Florence Briggs Thayer)",
                "Heikkinen, Miss. Laina",
                "Vestrom, Miss. Hulda Amanda Adolfina",
            ],
            "p_class": [3, 1, 3, 3],
            "fare": [7.25, 71.2833, 7.925, 7.8542],
            "survived": [0, 1, 1, 0],
            "sex": ["male", "female", "female", "female"],
            "age_group": ["adult", "adult", "adult", "child"],
        }
    )
    cat_type = CategoricalDtype(categories=["child", "adult", "unknown"], ordered=False)
    expected_df["age_group"] = expected_df["age_group"].astype(cat_type)

    testing.assert_frame_equal(expected_df, clean_titanic(input_df))


def test_clean_titanic_with_empty_age():
    input_df = pd.DataFrame(
        {
            "PassengerId": [1, 2, 3, 15],
            "Name": [
                "Braund, Mr. Owen Harris",
                "Cumings, Mrs. John Bradley (Florence Briggs Thayer)",
                "Heikkinen, Miss. Laina",
                "Vestrom, Miss. Hulda Amanda Adolfina",
            ],
            "Sex": ["male", "female", "female", "female"],
            "Age": [22, 38, np.nan, 14],
            "Pclass": [3, 1, 3, 3],
            "Fare": [7.25, 71.2833, 7.925, 7.8542],
            "Survived": [0, 1, 1, 0],
        }
    )

    expected_df = pd.DataFrame(
        {
            "name": [
                "Braund, Mr. Owen Harris",
                "Cumings, Mrs. John Bradley (Florence Briggs Thayer)",
                "Heikkinen, Miss. Laina",
                "Vestrom, Miss. Hulda Amanda Adolfina",
            ],
            "p_class": [3, 1, 3, 3],
            "fare": [7.25, 71.2833, 7.925, 7.8542],
            "survived": [0, 1, 1, 0],
            "sex": ["male", "female", "female", "female"],
            "age_group": ["adult", "adult", "unknown", "child"],
        }
    )
    cat_type = CategoricalDtype(categories=["child", "adult", "unknown"], ordered=False)
    expected_df["age_group"] = expected_df["age_group"].astype(cat_type)

    testing.assert_frame_equal(expected_df, clean_titanic(input_df))


def test_titanic_with_pclass_details_with_pclasses_in_original_equal_lookup():
    input_df = pd.DataFrame(
        {
            "PassengerId": [1, 2, 10],
            "Name": [
                "Braund, Mr. Owen Harris",
                "Cumings, Mrs. John Bradley (Florence Briggs Thayer)",
                "Nasser, Mrs. Nicholas (Adele Achem)",
            ],
            "Pclass": [3, 1, 2],
        }
    )

    expected_df = pd.DataFrame(
        {
            "PassengerId": [1, 2, 10],
            "Name": [
                "Braund, Mr. Owen Harris",
                "Cumings, Mrs. John Bradley (Florence Briggs Thayer)",
                "Nasser, Mrs. Nicholas (Adele Achem)",
            ],
            "Pclass": [3, 1, 2],
            "class_name": ["Third", "First", "Second"],
            "deck_level": ["Lower", "Upper", "Middle"],
        }
    )

    testing.assert_frame_equal(expected_df, titanic_with_pclass_details(input_df))


def test_titanic_with_pclass_details_pclasses_in_original_one_more_than_lookup():
    input_df = pd.DataFrame(
        {
            "PassengerId": [1, 2, 10],
            "Name": [
                "Braund, Mr. Owen Harris",
                "Cumings, Mrs. John Bradley (Florence Briggs Thayer)",
                "Nasser, Mrs. Nicholas (Adele Achem)",
            ],
            "Pclass": [3, 1, 4],
        }
    )

    expected_df = pd.DataFrame(
        {
            "PassengerId": [1, 2, 10],
            "Name": [
                "Braund, Mr. Owen Harris",
                "Cumings, Mrs. John Bradley (Florence Briggs Thayer)",
                "Nasser, Mrs. Nicholas (Adele Achem)",
            ],
            "Pclass": [3, 1, 4],
            "class_name": ["Third", "First", np.nan],
            "deck_level": ["Lower", "Upper", np.nan],
        }
    )

    testing.assert_frame_equal(expected_df, titanic_with_pclass_details(input_df))


def test_titanic_with_pclass_details_pclasses_in_original_one_less_than_lookup():
    input_df = pd.DataFrame(
        {
            "PassengerId": [1, 2],
            "Name": [
                "Braund, Mr. Owen Harris",
                "Cumings, Mrs. John Bradley (Florence Briggs Thayer)",
            ],
            "Pclass": [3, 1],
        }
    )

    expected_df = pd.DataFrame(
        {
            "PassengerId": [1, 2],
            "Name": [
                "Braund, Mr. Owen Harris",
                "Cumings, Mrs. John Bradley (Florence Briggs Thayer)",
            ],
            "Pclass": [3, 1],
            "class_name": ["Third", "First"],
            "deck_level": ["Lower", "Upper"],
        }
    )

    testing.assert_frame_equal(expected_df, titanic_with_pclass_details(input_df))
