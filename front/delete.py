import requests

product_id=input("Id you want to delet?")

endpoint= f"http://127.0.0.1:8000/api/products/{product_id}/delete/"


data={"title": "Jai Ho Sitaaram","content":"Ram Ram Ji","price":200}
get_response=requests.delete(endpoint) 

# API
# print("headers",get_response.headers)
# print("text",get_response.text)  
print("delete",get_response.status_code, get_response.status_code==204)
# print(get_response.status_code) 
 


