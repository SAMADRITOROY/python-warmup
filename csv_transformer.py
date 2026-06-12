import csv

def clean_row(row):
    age_as_string = row["Age"]
    age_as_float = float(age_as_string) if age_as_string else None

    p_class_as_string = row["Pclass"]
    p_class_as_int = int(p_class_as_string) if p_class_as_string else None

    fare = row["Fare"]
    fare_as_float = float(fare) if fare else None
    
    if age_as_float is None:
        age_group = "unknown"
    elif age_as_float < 18:
        age_group = "child"
    else:
        age_group = "adult"

    return {
        "name": row["Name"].strip(),
        "p_class": p_class_as_int,
        "fare": fare_as_float,
        "age_group": age_group
    }

cleaned_rows = []

def main():
    with open("titanic.csv", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            cleaned_row = clean_row(row)
            cleaned_rows.append(cleaned_row)

    with open("titanic_cleaned.csv", "w", newline="") as f:
        fieldnames = ["name", "p_class", "fare", "age_group"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(cleaned_rows)

if __name__ == "__main__":
    main()


