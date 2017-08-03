import methods

base_url = "https://dadosabertos.camara.leg.br/api/v2"
per_page = 55
current_page = 1

def parties_url(page = current_page, per_page = per_page):
    return "{base_url}/partidos/?pagina={page}&itens={per_page}".format(base_url = base_url, page = current_page, per_page = per_page)

print("Fetching {url}".format(url=parties_url()))

parties = []

request = methods.do_request(parties_url())
json_response = request.json()
methods.append_list(json_response, parties)

print("\nWe have {size} parties\n".format(size = len(parties)))

print("Writing file...\n")
methods.write_file(parties, 'partidos')

for party in parties:
    print("Getting {name} info".format(name = party["sigla"]))
    request = methods.get_party_info(party["id"])
    json_response = request.json()
    methods.save_party_info_into_file(json_response)
