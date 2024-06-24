import requests

def buscar_repositorios_populares(consulta, api_key):
    url = 'https://api.github.com/search/repositories'
    params = {'q': consulta, 'sort': 'stars', 'order': 'desc'}
    headers = {'Authorization': api_key}

    respuesta = requests.get(url, params=params, headers=headers)
    if respuesta.status_code == 200:
        return respuesta.json()['items']
    else:
        return []

if __name__ == "__main__":
    input_search = input("¿Que repositorios quieres buscar? ")
    api_key = input("Ingrese su api key: ")
    repositorios = buscar_repositorios_populares(input_search, api_key)
    for repo in repositorios:
        print(repo['name'], repo['html_url'])
