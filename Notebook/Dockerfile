FROM jupyter/scipy-notebook

RUN pip install joblib

COPY test_df.csv ./test.csv

COPY inference.py ./inference.py
COPY random_forest.joblib ./random_forest.joblib
