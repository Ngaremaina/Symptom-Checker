import pandas as pd

#Reading the data
training = pd.read_csv('data/Training.csv')
testing  = pd.read_csv('data/Testing.csv')
cols     = training.columns
cols     = cols[:-1]
x        = training[cols]
y        = training['prognosis']
y1       = y


# Dimensionality Reduction for removing redundancies
reduced_data = training.groupby(training['prognosis']).max()

