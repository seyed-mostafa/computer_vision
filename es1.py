import csv
import numpy as np
import matplotlib.pyplot as plt

with open('FMEL_Dataset.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    print(fields)
    # for row in csvreader:
    #     print(row)