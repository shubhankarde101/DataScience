# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 20:19:59 2020

@author: SHUBHANKAR
"""

import pickle
import numpy.testing
from pandas import testing
import numpy as np
from pandas.api.types import is_numeric_dtype, is_datetime64_dtype

col_names = pickle.load(open('test_file/col_names.pk', 'rb'))
df = pickle.load(open('question/dataframe.pk', 'rb'))
df.dtypes

with open('question/dataframe.pk', "wb") as file:
    pickle.dump(df, file)

def test_df_shape():
        assert df.shape == (3280, 19)

def test_num_cols():
        assert len(col_names) == len(df.columns)

def test_cols_names():
        cols =df.columns
        assert np.array_equiv(col_names, np.sort(cols))

def test_col_type():
        for col in col_names:
            assert is_numeric_dtype(df[col])

def test_index():
        assert is_datetime64_dtype(df.index)

def test_sanity_check_avg_wind_speed():
        mean = round(np.mean(df["2011-08-1":"2011-08-20"]["Average windspeed (mph)"]), 2)
        assert mean == 4.64

def test_sanity_check_std_min_temp():
        std1 = round(np.std(df["2011-04-20":"2012-01-1"]["Minimum temperature (°F)"]), 2)
        assert std1 == 12.34

def test_sanity_check_std_max_pressure():
        std2 = round(np.std(df["2011-04-20":"2012-01-1"]["Maximum pressure"]), 2)
        assert std2 == 0.27

def test_max_temp():
        max = round(np.max(df["2011-04-20":"2012-01-1"]["Maximum temperature (°F)"]), 2)
        assert max == 89.7

