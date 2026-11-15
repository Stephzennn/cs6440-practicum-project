"""
Here we will implement the multi-linear regresson model.
"""

import numpy as np
import pandas as pd
import sklearn as skl
import matplotlib as mpl

import statsmodels.api as sm
import statsmodels.formula.api as smf


# Personal Model 

"""
Variable                          OR     95% CI        P
Age 50-64                         0.98   0.64-1.50     .93
Age >=65                          0.92   0.54-1.59     .77
Male                              0.99   0.70-1.41     .95
Parental history of diabetes      1.76   1.17-2.64     .006
BMI 25.0-29.9                     1.35   0.78-2.34     .28
BMI >=30.0                        2.50   1.45-4.30     .001
Blood pressure elevated/treated   1.65   1.10-2.46     .02
Low HDL-C                         2.57   1.75-3.77     <.001
Triglycerides >=150 mg/dL         1.78   1.22-2.59     .003
Fasting glucose 100-126 mg/dL     7.25   4.89-10.74    <.001
Intercept                        -5.517
"""

SimpleModelVariables = {
    "Age 50-64": np.log(0.98),
    "Age >=65": np.log(0.92),
    "Male": np.log(0.99),
    "Parental history of diabetes": np.log(1.76),
    "BMI 25.0-29.9": np.log(1.35),
    "BMI >=30.0": np.log(2.50),
    "Blood pressure elevated/treated": np.log(1.65),
    "Low HDL-C": np.log(2.57),
    "Triglycerides >=150 mg/dL": np.log(1.78),
    "Fasting glucose 100-126 mg/dL": np.log(7.25),
    "Intercept": -5.517}


SimpleModel = pd.DataFrame.from_dict(SimpleModelVariables, orient='index', columns=['Coefficient'])
SimpleModel

"""
# Dummy patient data (same values as frontend/src/sampleData.js)
from pathlib import Path
SAMPLE_PATH = Path(__file__).resolve().parents[2] / "data" / "sample_patient.json"
df = pd.read_json(SAMPLE_PATH)
print(df)


# Model inputs (binary features)
male = df["sex"] == "Male"
X = pd.DataFrame({
    "age_50_64": df["age"].between(50, 64),
    "age_65_plus": df["age"] >= 65,
    "male": male,
    "parental_history": df["family_history"] == "Yes",
    "bmi_25_29": (df["bmi"] >= 25) & (df["bmi"] < 30),
    "bmi_30_plus": df["bmi"] >= 30,
    "high_bp": (df["systolic_bp"] >= 130) | (df["diastolic_bp"] >= 85),
    "low_hdl": df["hdl"] < np.where(male, 40, 50),
    "high_tg": df["triglycerides"] >= 150,
    "ifg": (df["fasting_glucose"] >= 100) & (df["fasting_glucose"] < 126),
}).astype(int)
print(X)

features =["age_50_64", "age_65_plus", "male", "parental_history",
            "bmi_25_29", "bmi_30_plus", "high_bp", "low_hdl", "high_tg", "ifg"]

coef = SimpleModel["Coefficient"]
logit = coef["Intercept"] + X.values @ coef.drop("Intercept").values
risk = 1 / (1 + np.exp(-logit))
print(risk)  # 8-year diabetes risk
print(f"8-year diabetes risk: {risk[0] * 100:.1f}%")
"""


def framingham_risk(patient):
    """Return the 8-year diabetes risk (0 to 1) for one patient (dict)."""
    df = pd.DataFrame([patient])

    # Model inputs (binary features)
    male = df["sex"] == "Male"
    X = pd.DataFrame({
        "age_50_64": df["age"].between(50, 64),
        "age_65_plus": df["age"] >= 65,
        "male": male,
        "parental_history": df["family_history"] == "Yes",
        "bmi_25_29": (df["bmi"] >= 25) & (df["bmi"] < 30),
        "bmi_30_plus": df["bmi"] >= 30,
        "high_bp": (df["systolic_bp"] >= 130) | (df["diastolic_bp"] >= 85),
        "low_hdl": df["hdl"] < np.where(male, 40, 50),
        "high_tg": df["triglycerides"] >= 150,
        "ifg": (df["fasting_glucose"] >= 100) & (df["fasting_glucose"] < 126),
    }).astype(int)

    features =["age_50_64", "age_65_plus", "male", "parental_history",
                "bmi_25_29", "bmi_30_plus", "high_bp", "low_hdl", "high_tg", "ifg"]

    coef = SimpleModel["Coefficient"]
    logit = coef["Intercept"] + X.values @ coef.drop("Intercept").values
    risk = 1 / (1 + np.exp(-logit))
    return float(risk[0])  # 8-year diabetes risk


if __name__ == "__main__":
    # Dummy patient data (same values as frontend/src/sampleData.js)
    from pathlib import Path
    SAMPLE_PATH = Path(__file__).resolve().parents[2] / "data" / "sample_patient.json"
    df = pd.read_json(SAMPLE_PATH)
    print(df)

    risk = framingham_risk(df.iloc[0].to_dict())
    print(f"8-year diabetes risk: {risk * 100:.1f}%")
