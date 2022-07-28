import requests

tuts="https://www.youtube.com/watch?v=c708Nf0cHrs"

endpoint = "https://httpbin.org/status/200/"
# endpoint = "https://httpbin.org"

# endpoint = "https://httpbin.org/anything"
endpoint= "http://127.0.0.1:8000/"

endpoint= "http://127.0.0.1:8000/api/"

# get_response=requests.get(endpoint, data={"query":"Jai Shi Ram"}) # API

# get_response=requests.get(endpoint, data={"query":"Jai Shi Ram"}) # API
get_response=requests.get(endpoint) # API
# get_response=requests.get(endpoint, params={'abc':123}, json={"query": "jai hanuman"}) # API


print("headers",get_response.headers)
print("text",get_response.text)  
# print("json",get_response.json())

# print(get_response.status_code) 
 


