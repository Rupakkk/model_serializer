
import requests
import json


URL = "http://127.0.0.1:8000/stuinfo/"

def get_id(id=None):
    data= {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    r = requests.get(url= URL,data = json_data)    
    data = r.json()
    print(data)
    
# get_id(1)


def post_create():
    data = {
        'name': 'haWk',
        'age' : 1999,
        'address': 'china'

    }
    json_data = json.dumps(data)
    r = requests.post(url= URL,data = json_data)
    data = r.json()
    print(data)
# post_create()

def post_update():
    data = {
        'id': 7,
        'name': 'hari',
        'age' : 65,
        'address': 'kkkk'

    }
    json_data = json.dumps(data)
    r = requests.put(url= URL,data = json_data)
    data = r.json()
    print(data)


post_update()

def del_data(id):
    data ={'id':id}
    json_data = json.dumps(data)
    r = requests.delete(url = URL, data = json_data)
    data =  r.json()
    print(data)
# del_data(12)

    