from elasticsearch import Elasticsearch
import json
import status

with open("key.json", "r") as read_file:
    data = json.load(read_file)

ELASTIC_PASSWORD = "some_password"
ELASTIC_USERNAME ='elastic'

if status.is_elastic_local():
    ip = 'localhost'
    verify=True
else:
    ip = '192.168.1.9'
    verify=False

# Create the client instance
client = Elasticsearch(
    f"https://{ip}:9200",
    ca_certs="ca.crt",
    verify_certs=verify, #Use this when not running inside vm
    # basic_auth=(ELASTIC_USERNAME, ELASTIC_PASSWORD)
    api_key=(data["id"], data["api_key"])
)

# Successful response!
# print(client.info())
myquery = {
  "query": {
    "bool": {
      "must": {
        "match": {      
          "_id": 'bnNe2oIBSKjFtKDgBQ1n'
        }
      }
    }
  }
}
myquery = {
  "query": {
    "bool": {
      "must": {
        "match": {      
          "destination.port": '5044'
        }
      }
    }
  }
}
myquery = {
  "query": {
    "bool": {
      "must": {
        "match": {       
          "destination.packets": '1569'
        }
      }
    }
  }
}

myquery = {
  "query": {
    "bool": {
      "must": {
        "match": {       
          "destination.packets": '1569'
        }
      },
      "must": {
        "match": {      
          "_id": 'bnNe2oIBSKjFtKDgBQ1n'
        }
      }
    }
  }
}

myquery = {
  "query": {
    "wildcard": {
        "_id": 'bnNe2oIBSKjFtKDgBQ1n'
    }
  }
}

myquery = {
  "query": {
    "bool":{
        "filter": [
            # {"match": {"destination.packets": '1569'}},
            # {"match": {"_id": 'bnNe2oIBSKjFtKDgBQ1n'}}
        ]
    }
  }
}
myquery = {
"bool":{
    "filter": [
        # {"match": {"destination.packets": '1569'}},
        # {"match": {"_id": 'bnNe2oIBSKjFtKDgBQ1n'}}
    ]
}
}
# myquery={"query": {"match_all": {}}}
# resp = client.search(index="packetbeat-7.16.0", body=myquery, size=999)
resp = client.search(index="packetbeat-7.16.0", query= myquery, size=999)
print("Got %d Hits:" % resp['hits']['total']['value'])
for hit in resp['hits']['hits']:
    print("%(agent)s %(host)s: %(tags)s" % hit["_source"])
# print(res)
