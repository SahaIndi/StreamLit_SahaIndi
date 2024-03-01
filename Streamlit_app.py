import streamlit as st
import pandas as pd

def main():
 st.title("Credit Rating forecasting")
 uploaded_file = st.file_uploader("Choose a file")
 if uploaded_file is not None:
   df = pd.read_csv(uploaded_file)
   st.write(dataframe)

if __name__=='__main__':
 main()
 
 
