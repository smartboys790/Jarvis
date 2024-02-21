from config import key
import requests 



def chat1(query): 
    messages = []
    system_message = 'You are an AI Virtual Assistant. Your name is Jarvis. Shubham Gupta a Computer Engineering student has created. '
    message= {  'role': 'User','parts': [{'text': system_message+' '+query}]}
    messages.append(message)
    data = {'contents': messages }
    url= 'https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key='+key
    response=requests.post(url,json=data)

    t1= response.json()
    t1=t1.get('candidates')[0].get('content').get('parts')[0].get('text')
    t1=t1.replace('*','')
    # print(t1)

    return t1

