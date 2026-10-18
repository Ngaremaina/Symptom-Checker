import os

import pandas as pd

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data')

#Reading the data
training = pd.read_csv(os.path.join(DATA_DIR, 'Training.csv'))
testing  = pd.read_csv(os.path.join(DATA_DIR, 'Testing.csv'))
cols     = training.columns
cols     = cols[:-1]
x        = training[cols]
y        = training['prognosis']
y1       = y


# Dimensionality Reduction for removing redundancies
reduced_data = training.groupby(training['prognosis']).max()
