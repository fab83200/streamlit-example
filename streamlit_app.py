#!pip install -q lime
#!pip install -q streamlit

#COLAB
from google.colab import drive                                                  # NEEDED
drive.mount('/content/gdrive');      

import streamlit as st
import pandas as pd
import numpy as np
import random

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression

from sklearn.metrics import accuracy_score
from lime import lime_tabular
import streamlit.components.v1 as components


title_text = 'LIME Explainer Dashboard for credit score'

st.markdown(f"<h2 style='text-align: center;'><b>{title_text}</b></h2>", unsafe_allow_html=True)
st.text("")


# This is the main train table, with TARGET
application_train_url = "/content/gdrive/MyDrive/Colab_Notebooks/Project7/application_train.csv"
app_train = pd.read_csv(application_train_url, sep=",")
for tr in app_train.describe(include='object').columns:
    app_train[tr]=app_train[tr].fillna((app_train[tr].mode()))
for ci in app_train.describe().columns:
    app_train[ci]=app_train[ci].fillna((app_train[ci].median()))


# This is the main test table, without TARGET
application_test_url = "/content/gdrive/MyDrive/Colab_Notebooks/Project7/application_test.csv"
app_test = pd.read_csv(application_test_url, sep=",")
for te in app_test.describe(include='object').columns:
    app_test[te]=app_test[te].fillna((app_test[te].mode()))
for tt in app_test.describe().columns:
    app_test[tt]=app_test[tt].fillna((app_test[tt].median()))
