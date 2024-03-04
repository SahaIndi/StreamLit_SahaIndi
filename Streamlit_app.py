import streamlit as st
import pandas as pd
import pickle



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
 
 
