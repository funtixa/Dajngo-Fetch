import os
import requests

def get_droplets():
    url = "https://my-burger-api.herokuapp.com/burgers"
    r = requests.get(url)
    droplets = r.json()
    droplet_list = []
    array_length = len(droplets)
    for i in range(array_length):
        droplet_list.append(droplets[i])
    return droplet_list


