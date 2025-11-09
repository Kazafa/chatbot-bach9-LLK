#import requests


#api = open("api_key.txt").read()
#api= 

endpoint = f'https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={"AIzaSyDJMsL9l-HJPlBnGS7jxgv6fIMctMqsR2Ybaaiman"}'

headers  = {
    "Content-type" : "application/json"
}


data_input = input ( "Silahkan Masukan pertanyaan Anda : ")
data = {
    "contents": [ {
        "parts": [{
            "text" : data_input
        }]
    }]   
}

response = requests.post(endpoint, headers=headers, json=data)
if response.status.code == 200:
    response_data= response.json ()
    print ("Respon Bot = \n", repons_data,['candidates'][0]['content']['parts'][0]['text'])
else :
    print("Error",response.status_code)

