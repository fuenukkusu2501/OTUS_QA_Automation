import requests

session = requests.Session()

session.headers = {"Autorization": "Special-key"}
session.verify = False

response = session.get("https://petstore.swagger.io/v2/pet/findByStatus")
response_post = session.post("https://petstore.swagger.io/v2/pet",
                              json={
                                  "name": "doggie",
                                  "photoUrls": []
                              })

print(response.text)
print(response_post.text)