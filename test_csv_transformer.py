from csv_transformer import clean_row

def test_clean_row_child():
    row = {"Name": "John Doe", "Age": "10", "Pclass": "2", "Fare": "15.5"}
    expected = {"name": "John Doe", "p_class": 2, "fare": 15.5, "age_group": "child"}
    assert clean_row(row) == expected

def test_clean_row_adult():
    row = {"Name": "Jane Doe", "Age": "30", "Pclass": "1", "Fare": "100.0"}
    expected = {"name": "Jane Doe", "p_class": 1, "fare": 100.0, "age_group": "adult"}
    assert clean_row(row) == expected

def test_clean_row_unknown_age():
    row = {"Name": "Baby Doe", "Age": "", "Pclass": "3", "Fare": "5.0"}
    expected = {"name": "Baby Doe", "p_class": 3, "fare": 5.0, "age_group": "unknown"}
    assert clean_row(row) == expected

def test_clean_row_missing_fare():
    row = {"Name": "No Fare Doe", "Age": "25", "Pclass": "2", "Fare": ""}
    expected = {"name": "No Fare Doe", "p_class": 2, "fare": None, "age_group": "adult"}
    assert clean_row(row) == expected

def test_clean_row_missing_pclass():
    row = {"Name": "No Pclass Doe", "Age": "40", "Pclass": "", "Fare": "20.0"}
    expected = {"name": "No Pclass Doe", "p_class": None, "fare": 20.0, "age_group": "adult"}
    assert clean_row(row) == expected

def test_clean_row_padded_name():
    row = {"Name": "  Padded Name  ", "Age": "22", "Pclass": "1", "Fare": "50.0"}
    expected = {"name": "Padded Name", "p_class": 1, "fare": 50.0, "age_group": "adult"}
    assert clean_row(row) == expected