import numpy as np
import pandas as pd

def split_dataframe(dataframe, split_probability):
    """
    Splits dataframe in two following
    parameters
    dataframe : whole dataframe we want to split in two sets.
    split_probability : .
    returns a tuple with two dataframes, the first one containing (split_probability*100)% of the elements
    and the second one containing the rest of the elements
    This function depends on the Pandas and numpy
    """
    random_frame = pd.DataFrame(np.random.randn(len(dataframe)))
    first_split_indexes = np.random.rand(len(dataframe)) < split_probability
    return dataframe[first_split_indexes], dataframe[~first_split_indexes]