import streamlit as st
import pandas as pd
import os, requests, json

# define the web service url
ws_url = 'http://bcd03477-9054-457e-b222-7816d7df7c82.francecentral.azurecontainer.io/score'    


def send_datas(datas):
    headers = {"Content-Type": "application/json", 'Accept': 'text/plain'}
    request_url = ws_url
    resp = requests.post(request_url, datas, headers=headers)
    return resp


def format_text_to_send(text_to_send):
    datas_to_send={}
    datas_to_send['data'] = {'text': [text_to_send]}
    return json.dumps(datas_to_send)


def sentiment_result(res):
    if res == '[[0]]':
        return 'négatif'
    elif res == '[[1]]':
        return 'positif'
    else:
        return 'inconnu'


def sentiment_analysis(input_data):
    formatted_text_to_send = format_text_to_send(input_data)    
    result_ws = send_datas(formatted_text_to_send)

    if result_ws.status_code == 200:
        sentiment_res = sentiment_result(result_ws.text)
        st.markdown('Le sentiment est ' + sentiment_res)
    else:
        st.markdown('Error : ' + str(result_ws.status_code) + ' - ' + str(result_ws.text))


st.title('Analyse de sentiment')

form1 = st.form(key='sentiment-form1')
user_input = form1.text_area('Entrer le texte')
submit1 = form1.form_submit_button('Envoyer')

if (submit1):
    if user_input != '':
        sentiment_analysis(user_input)



form2 = st.form(key='sentiment-form2')
sentence = form2.selectbox("Sélectionner un texte: ", 
                            ['',
                            'It is raining', 
                            'I am happy', 
                            'I love AI',
                            'I hate bugs']
                            ) 
submit2 = form2.form_submit_button('Envoyer')

if (submit2):
    if sentence != '':
        sentiment_analysis(sentence)



