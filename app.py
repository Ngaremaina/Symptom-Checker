import csv
import os

import pandas as pd
from flask import Flask, render_template, request

from checker.train import cols, DATA_DIR
from checker.model import le, clf

app = Flask(__name__)

# Question shown to the user -> symptom column in the training data
QUESTIONS = [
    ("headache", "Are you experiencing a headache?"),
    ("cough", "Are you experiencing any coughing?"),
    ("body_hotness", "Are you experiencing high fever?"),
    ("vomiting", "Are you experiencing vomiting?"),
    ("nausea", "Are you experiencing nausea?"),
    ("sweating", "Are you experiencing sweating?"),
    ("abdominal_pain", "Are you experiencing abdominal pains?"),
    ("fatigue", "Are you experiencing fatigue?"),
]

# Some column names in the CSV carry stray spaces, so match on the stripped name
column_for = {c.strip(): c for c in cols}


def get_precaution_dict():
    precautions = {}
    with open(os.path.join(DATA_DIR, 'Precautions.csv')) as csv_file:
        for row in csv.reader(csv_file, delimiter=','):
            precautions[row[0]] = [p for p in row[1:5] if p.strip()]
    return precautions


precaution_dictionary = get_precaution_dict()


def predict_disease(answers):
    features = pd.DataFrame([[0] * len(cols)], columns=cols)
    for symptom, present in answers.items():
        if present:
            features[column_for[symptom]] = 1
    return le.inverse_transform(clf.predict(features))[0]


@app.route("/", methods=["GET", "POST"])
def index():
    answers = {symptom: False for symptom, _ in QUESTIONS}
    disease = None
    precautions = []

    if request.method == "POST":
        answers = {symptom: request.form.get(symptom) == "yes" for symptom, _ in QUESTIONS}
        if any(answers.values()):
            disease = predict_disease(answers)
            precautions = precaution_dictionary.get(disease, [])

    return render_template(
        "index.html",
        questions=QUESTIONS,
        answers=answers,
        submitted=request.method == "POST",
        disease=disease,
        precautions=precautions,
    )


if __name__ == "__main__":
    app.run(debug=True)
