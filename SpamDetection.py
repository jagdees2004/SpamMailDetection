import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import streamlit as st
data = pd.read_csv(r"D:\spam\spam (1).csv")
data.drop_duplicates(inplace=True)
data["Category"]=data["Category"].replace(['ham','spam'],['Not Spam','Spam'])
mess=data['Message']
cat=data['Category']
(mess_train,mess_test,cat_train,cat_test)=train_test_split(mess,cat,test_size=0.2)
cv=CountVectorizer()
features=cv.fit_transform(mess_train)
model=MultinomialNB()
model.fit(features,cat_train)
features_test=cv.transform(mess_test)
#predict data
def predict(message):
    input_message=cv.transform([message])
    result=model.predict(input_message)
    return result


##STREAMLIT CODE
st.header('Spam Detection')
input_mess=st.text_input('Enter message here')
if st.button('validate'):
    output = predict(input_mess)
    if output[0]=='Spam':
        st.write('spam')
    else:
        st.write('Not Spam')    

