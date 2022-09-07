from elasticsearch import Elasticsearch
import json
import status
import ast

with open("key.json", "r") as read_file:
    data = json.load(read_file)

if status.is_elastic_local():
    ip = 'localhost'
    verify=True
else:
    ip = '192.168.1.12'
    verify=False

# Create the client instance
client = Elasticsearch(
    f"https://{ip}:9200",
    ca_certs="ca.crt",
    verify_certs=verify, #Use this when not running inside vm
    api_key=(data["id"], data["api_key"])
)

def create_query(rulia):
    rules = ''
    print(rulia.data['match_all'])
    if not rulia.data['match_all']:
        for rule in rulia:
            rule_label = str(rule.label).split('">')[1].split('<')[0]
            if rule.data != '*' and rule_label != 'Number of results' and rule_label != 'Source Index' and rule_label != 'Show all entries' and rule_label != 'Search'and rule_label != 'CSRF Token':
                # print(rule.label)
                # print(rule.data)
                rules = rules + f"{{'match': {{'{rule.description}': '{rule.data}'}}}},"
    myquery = ast.literal_eval(f"{{'bool': {{'filter': [{rules[:-1]}]}}}}")
    # print(myquery)
    resp = client.search(index=rulia.index.data, query= myquery, size=int(rulia.no_results.data))
    return resp