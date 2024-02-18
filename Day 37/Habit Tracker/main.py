import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"

my_webpage = "https://pixe.la/@ayushsharma"
USERNAME = "ayushsharma"
TOKEN = "ljashcdkhsaliduchyo823e982y92ye9182eh12ehd"
params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
header = {
    "X-USER-TOKEN": TOKEN
}
GRAPH_ID = "qwerty123"
graph_config = {
    "id": GRAPH_ID,
    "name": "Daily reading page count graph",
    "unit": "page",
    "type": "int",
    "color": "momiji"

}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=header)
# print(response.text)


pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now().strftime("%Y%m%d")
print(today)
pixel_config = {
    "date": today,
    "quantity": "10"
}

# response = requests.post(url=pixel_endpoint, json=pixel_config, headers=header)
# print(response.text)
pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"

pixel_update_config = {
    "quantity": "100"
}

# response = requests.put(url=pixel_update_endpoint, json=pixel_update_config, headers=header)
# print(response.text)

pixel_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"


response = requests.delete(url=pixel_delete_endpoint, headers=header)
print(response.text)