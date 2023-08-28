import requests
from datetime import datetime

username = "YOUR_USERNAME"
token = "YUOR_TOKEN"
graph_id = "GRAPH_ID"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": token,
    "username": username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)
graph_endpoint = f"{pixela_endpoint}/{username}/graphs"
graph_config = {
    "id": "graph1",
    "name": "Audio Book",
    "unit": "mn",
    "type": "int",
    "color": "shibafu"
}
headers = {
    "X-USER-TOKEN": token
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
date = datetime(year=2023, month=8, day=15)
date_format = date.strftime("%Y%m%d")
post_pixel_endpoint = f"{pixela_endpoint}/{username}/graphs/{graph_id}"
pixel_config = {
    "date": date_format,
    "quantity": "20",
}

# response = requests.post(url=post_pixel_endpoint, json=pixel_config, headers=headers)
# print(response.text)

update_delete_pixel_endpoint = f"{pixela_endpoint}/{username}/graphs/{graph_id}/{date_format}"
update_config = {
    "quantity": "25"
}

# response = requests.put(url=update_pixel_endpoint, json=update_config, headers=headers)
# print(response.text)

response=requests.delete(url=update_delete_pixel_endpoint,headers=headers)
print(response.text)

