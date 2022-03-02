
import requests
import json

host = 'http://localhost:9200/'

index = 'companydatabase'

settings = {
            "index": {
            "max_ngram_diff": 20
        },
        "analysis": {
            "analyzer": {
                "autocomplete": {
                    "type": "custom",
                    "tokenizer": "standard",
                    "filter": [
                        "lowercase",
                        "autocomplete_filter"
                    ]
                },
            },
            "filter": {
                "autocomplete_filter": {
                    "type": "ngram",
                    "min_gram": 1,
                    "max_gram": 20
                }
            }
        }
    }

mappings = {
      "properties": {
        "full_name": {
            "type": "text",
            "analyzer": "autocomplete",
            "fields": {
                "keyword": {
                    "type": "keyword"
                }
            }
        },
        "Designation": {
          "type": "text"
        },
        "Salary": {
          "type": "text"
        },
        "DateOfJoining": {
          "type": "date",
          "format": "strict_date_optional_time||epoch_millis"
        },
        "Address": {
          "type": "text"
        },
        "Gender": {
          "type": "text"
        },
        "Age": {
          "type": "long"
        },
        "MaritalStatus": {
          "type": "text"
        },
        "Interests": {
          "type": "text"
        }
      }
}

def del_index():

    url = host + index
    r = requests.delete(url, verify=True)
    if r.status_code == 200:
        print(f'{index} - deleted successfully')
    else:
        print(r.text)



def apply_mapping():
    headers = {
        'Content-Type': 'application/json',
    }

    params = (
        ('pretty', ''),
    )

    templete = {"settings" : settings, "mappings" : mappings}

    
    r = requests.put(host + index, headers=headers, params=params, data=json.dumps(templete), verify=True)
    if r.status_code == 200:
        print(f'{index} - mapping applied successfully')
    else:
        print(r.text)



def index_data():
    print(f'{index} - inserting data...')
    headers = {
        'Content-Type': 'application/json',
    }
    data = open('Employees50K.json', 'rb').read()
    r = requests.put(f'{host + index}/_bulk', headers=headers,data=data, verify=True)

    if r.status_code == 200:
        print(f'{index} - data inserted successfully')
    else:
        print(r.text)


def count_documents():
    r = requests.get(f'{host + index}/_count', verify=True)

    if r.status_code == 200:
        print(f'{index} - There are {r.json()["count"]} documents in the index')
    else:
        print(r.text)


def get_indexes():
    r = requests.get(f'{host}_cat/indices?pretty', verify=True)

    print(r.text)


def analyzer_test():

    search = 'elvis'

    headers = {
        'Content-Type': 'application/json',
    }

    params = (
        ('pretty', ''),
    )

    data = {
    "analyzer": "autocomplete",
    "text": search
    }

    
    r = requests.post(host + index + '/_analyze', headers=headers,  params = params, data=json.dumps(data), verify=True)
    print(f"{search} - {','.join([i['token'] for i in r.json()['tokens']])}")




def search_test():
    headers = {
        'Content-Type': 'application/json',
    }


    params = (
        ('pretty', ''),
    )

    data = {
        "query": {
            "match": {
                "full_name": {
                    "query": "INNERT",
                    "analyzer": "standard"
                }
            }
        }
        }

    
    r = requests.post(host + index + '/_search', headers=headers,  params = params, data=json.dumps(data), verify=True)
    print(r.text)



del_index()
apply_mapping()
index_data()
count_documents()

#get_indexes()
#analyzer_test()
#search_test()
