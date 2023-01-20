import requests

# endpoint = "https://httpbin.org/status/200/"
# endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8080/api/" #http://127.0.0.1:8000/ 

get_response = requests.post(endpoint,params={'abc':123}, json={'title':"This is a title","content":'Demo Text','price':'abcd' }) # HTTP Request
# print(get_response.text) # print raw text response
# print(get_response.status_code)

# HTTP Request -> HTML
# REST API HTTP Request -> JSON
# JavaScript Object Nototion ~ Python Dict
print(get_response.json())
# print(get_response.status_code)