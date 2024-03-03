import streamlit as st
import pandas as pd
import pickle
numpy==1.22.0
pandas==1.3.4
plotly==5.5.0
streamlit==1.3.0
scikit-learn==0.24.2

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
   st.button('Predict credit rating of the financial institute')
   st.success(creditrating_prediction(df))
  
if __name__=='__main__':
 main()
 
 
