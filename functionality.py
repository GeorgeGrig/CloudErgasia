from elasticsearch import Elasticsearch
import json
import status
import ast

# Get API key information
with open("key.json", "r") as read_file:
    data = json.load(read_file)

# Use correct ip and tls certificate if script is running locally or not
if status.is_elastic_local():
    ip = 'localhost'
    verify = True
else:
    ip = '192.168.1.12'
    verify = False

# Create the elastic client instance
client = Elasticsearch(
    f"https://{ip}:9200",
    ca_certs="ca.crt",
    verify_certs=verify,
    api_key=(data["id"], data["api_key"])
)


def create_query(rulia):
    rules = ''
    # If checkbox match all is checked, ignore all filters and return all results from elastic
    if not rulia.data['match_all']:
        # Create request dictionary based on form response
        for rule in rulia:
            rule_label = str(rule.label).split('">')[1].split('<')[0]
            # Ignore wildcard * and irrelevant form fields
            if  '*' not in rule.data and rule_label != 'Number of results' and rule_label != 'Source Index' and rule_label != 'Show all entries' and rule_label != 'Search' and rule_label != 'CSRF Token':
                rules = rules + \
                    f"{{'match': {{'{rule.description}': '{rule.data.strip()}'}}}},"
    # Create dictionary from string using the ast command
    myquery = ast.literal_eval(f"{{'bool': {{'filter': [{rules[:-1]}]}}}}")
    # Make the query to elasticsearch
    try:
        resp = client.search(index=rulia.index.data,
                         query=myquery, size=int(rulia.no_results.data))
    except:
        resp = False
    return resp
