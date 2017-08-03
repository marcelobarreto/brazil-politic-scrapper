import requests
import json

base_url = "https://dadosabertos.camara.leg.br/api/v2"
per_page = 55
current_page = 1

def deputies_url(page = current_page, per_page = per_page):
    return "{base_url}/deputados/?pagina={page}&itens={per_page}".format(base_url = base_url, page = current_page, per_page = per_page)

def get_last_page(response):
    return int(response["links"][3]["href"].split("pagina=")[1].split("&")[0])

def append_deputies(response):
    for deputy in response["dados"]:
        deputies.append(deputy)

def do_request():
    return requests.get(deputies_url())

def write_file(data):
    with open('deputies.json', 'w') as outfile:
        json.dump(data, outfile)

print "Fetching {url}...".format(url=base_url)

deputies = []

request = requests.get(deputies_url())
json_response = request.json()
last_page = get_last_page(json_response)

while current_page <= last_page:
    print "Now requesting page {page}".format(page = current_page)
    request = do_request()
    json_response = request.json()
    append_deputies(json_response)
    current_page += 1

print "\nWe have {size} deputies\n".format(size = len(deputies))

print "Writing file...\n"
write_file(deputies)

for deputy in deputies:
    print deputy["nome"]
