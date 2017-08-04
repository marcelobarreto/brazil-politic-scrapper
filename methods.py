import requests
import json as json

base_url = "https://dadosabertos.camara.leg.br/api/v2"

def get_last_page(response):
    return int(response["links"][3]["href"].split("pagina=")[1].split("&")[0])

def append_list(response, list):
    for i in response["dados"]:
        list.append(i)

def do_request(url):
    return requests.get(url)

def write_file(data, filename):
    with open('{filename}.json'.format(filename = filename), 'w') as outfile:
        json.dump(data, outfile, ensure_ascii = False, indent = 2)

def get_deputy_info(id):
    url = "{url}/deputados/{id}".format(url = base_url, id = id)
    return requests.get(url)

def save_deputy_info_into_file(data):
    filename = str.join('_', data["dados"]["nomeCivil"].split(' ')).lower()
    with open('deputados/{filename}.json'.format(filename = filename), 'w') as outfile:
        json.dump(data["dados"], outfile, ensure_ascii = False, indent = 2)

def get_party_info(id):
    url = "{url}/partidos/{id}".format(url = base_url, id = id)
    return requests.get(url)

def save_party_info_into_file(data):
    if (data.get("status") == 404):
        return

    filename = data["dados"]["sigla"].lower()
    with open('partidos/{filename}.json'.format(filename = filename), 'w') as outfile:
        json.dump(data["dados"], outfile, ensure_ascii = False, indent = 2)
