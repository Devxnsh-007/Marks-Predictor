import pandas as pd

def encode_data(df):

    if "gender" in df.columns:
        df["gender"] = df["gender"].map({
            "Male":1,
            "Female":0
        })

    if "parent_education" in df.columns:
        df["parent_education"] = df["parent_education"].map({
            "Middle School":0,
            "High School":1,
            "Bachelor":2,
            "Master":3,
            "PhD":4
        })

    if "internet_access" in df.columns:
        df["internet_access"] = df["internet_access"].map({
            "Yes":1,
            "No":0
        })

    if "extracurricular" in df.columns:
        df["extracurricular"] = df["extracurricular"].map({
            "Yes":1,
            "No":0
        })

    if "passed" in df.columns:
        df["passed"] = df["passed"].map({
            "Yes":1,
            "No":0
        })

    return df