import methods

base_url = "https://dadosabertos.camara.leg.br/api/v2"
per_page = 55
current_page = 1

def deputies_url(page = current_page, per_page = per_page):
    return "{base_url}/deputados/?pagina={page}&itens={per_page}".format(base_url = base_url, page = current_page, per_page = per_page)

print("Fetching {url}".format(url=deputies_url()))

deputies = []

request = methods.do_request(deputies_url())
json_response = request.json()
last_page = methods.get_last_page(json_response)

while current_page <= last_page:
    print("Now requesting page {page}".format(page = current_page))
    request = methods.do_request(deputies_url())
    json_response = request.json()
    methods.append_list(json_response, deputies)
    current_page += 1

print("\nWe have {size} deputies\n".format(size = len(deputies)))

print("Writing file...\n")
methods.write_file(deputies, 'deputados')

for deputy in deputies:
    print("Getting {name} info".format(name = deputy["nome"]))
    request = methods.get_deputy_info(deputy["id"])
    json_response = request.json()
    methods.save_deputy_info_into_file(json_response)
