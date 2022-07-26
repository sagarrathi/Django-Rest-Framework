import requests

tuts="https://www.youtube.com/watch?v=c708Nf0cHrs"

endpoint = "https://httpbin.org/status/200/"
# endpoint = "https://httpbin.org"

# endpoint = "https://httpbin.org/anything"


# get_response=requests.get(endpoint, data={"query":"Jai Shi Ram"}) # API

# get_response=requests.get(endpoint, data={"query":"Jai Shi Ram"}) # API
get_response=requests.get(endpoint) # API

print(get_response.status_code) 
 


