import re
from typing import List, Any
import pandas as pd
import numpy as np


def first_word_within_quotes(string):
    pattern = r'"name": "([A-z].*?)"'
    word_list: list[Any] = re.findall(pattern, string)
    return word_list[0] if word_list != [] else np.nan


def is_dictionary_column(df):
    return [df[col].name for col in df.select_dtypes('O').columns if df[col][0].__contains__('{')]


def first_word_within_quotes_dataframe(df):
    for col in is_dictionary_column(df):
        df[col] = df[col].apply(first_word_within_quotes)
    return df


def drop_singles(df, cols):
    """
    Drop all the rows with a unique count of 1
    :param df:
    :param cols: column names
    :return:
    """
    for i in df[cols].unique():
        if (len(df.loc[(df[cols] == i)]) == 1) or (len(df.loc[(df[cols] == i)]) == 2):
            df.drop((df.loc[df[cols] == i]).index, inplace=True)
