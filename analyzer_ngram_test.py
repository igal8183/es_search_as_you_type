import requests
import json

host = 'http://localhost:9200/'

index = 'companydatabase'

def analyzer_test():

    search = 'elvis pash'

    headers = {
        'Content-Type': 'application/json',
    }

    params = (
        ('pretty', ''),
    )

    data_standard = {
    "analyzer": "standard",
    "text": search
    }

    r = requests.post(host + index + '/_analyze', headers=headers,  params = params, data=json.dumps(data_standard), verify=True)
    print(f"standard analyzer: '{search}' - {','.join([i['token'] for i in r.json()['tokens']])}")

    data_ngram = {
    "analyzer": "autocomplete",
    "text": search
    }

    
    r = requests.post(host + index + '/_analyze', headers=headers,  params = params, data=json.dumps(data_ngram), verify=True)
    print(f"ngram: '{search}' - {','.join([i['token'] for i in r.json()['tokens']])}")


analyzer_test()