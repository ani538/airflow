import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# To help with data visualization
import matplotlib.pyplot as plt
import seaborn as sns

def dataPreprocessing():
    # read the CSV file
    df = pd.read_csv("RawData/Job_Placement_Data.csv")

    