import requests

endpoint= "http://127.0.0.1:8000/api/products/1/update/"


data={"title": "Jai Ho Sitaaram","content":"Ram Ram Ji","price":200}
get_response=requests.put(endpoint,json=data) 

# API
# print("headers",get_response.headers)
# print("text",get_response.text)  
print("json",get_response.json())
# print(get_response.status_code) 
 


