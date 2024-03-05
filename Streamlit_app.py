import streamlit as st
#importing necessary libraries
import pandas as pd
import numpy as np
from random import sample
#import matplotlib.pyplot as plt
#%matplotlib inline
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
import seaborn as sns
from xgboost import plot_importance
from sklearn.pipeline import Pipeline
import xgboost as xgb
from sklearn.model_selection import GridSearchCV
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score,classification_report
from sklearn.compose import ColumnTransformer
from sklearn import preprocessing
from sklearn.preprocessing import MinMaxScaler
from sklearn.base import BaseEstimator,TransformerMixin



loaded_model=pickle.load(open('model.pkl','rb'))
def creditrating_prediction(data):
    
    prediction=loaded_model.predict(data)
    print(prediction)

def main():
 st.title("Credit Rating forecasting")
 uploaded_file = st.file_uploader("Choose a file")
 if uploaded_file is not None:
   df = pd.read_csv(uploaded_file)
   st.write(df)
   y_pred=loaded_model.predict(df)
  
   y_pred=pd.DataFrame(y_pred,columns=['Predicted-Status'])

   df=df.reset_index(drop=True)
   new_df=pd.concat([df,y_pred],axis=1,ignore_index=False)


#Write the Result to App
   st.write("Predicted Result") 
   st.write(new_df)
   st.success(creditrating_prediction(df))
  
if __name__=='__main__':
 main()
 
 
