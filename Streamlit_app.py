import streamlit as st
import pandas as pd
import pickle

loaded_model=pickle.load(open('/Users/user/Documents/M.Tech Data Science-BITS Pilani/Fourth Semester/model_pickle','rb'))
def creditrating_prediction(data):
    
    prediction=loaded_model.predict(data)
    print(prediction)

def main():
 st.title("Credit Rating forecasting")
 uploaded_file = st.file_uploader("Choose a file")
 if uploaded_file is not None:
   df = pd.read_csv(uploaded_file)
   st.write(df)
   st.button('Predict credit rating of the financial institute')
   st.success(creditrating_prediction(df))
  
if __name__=='__main__':
 main()
 
 
