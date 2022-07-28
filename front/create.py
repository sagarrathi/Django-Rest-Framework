import requests

endpoint= "http://127.0.0.1:8000/api/products/"


get_response=requests.post(endpoint,json={"title": "jai hanuman","price":100}) # API

# print("headers",get_response.headers)
# print("text",get_response.text)  
print("json",get_response.json())
# print(get_response.status_code) 
 


