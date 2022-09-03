import requests
from requests.exceptions import ConnectionError
import subprocess

def is_elastic_local():
    try:
        requests.get('https://localhost:9200', verify='ca.crt')
        return True
    except ConnectionError as e:
        return False

def check_kibana_status():
    container_name ='kibana'
    try:
        return str(subprocess.check_output("docker inspect --format='{{json .State.Health}}' " + container_name, shell=True)).split('"Status":"')[1].split('"',1)[0]
    except:
        return False

def check_elasticsearch_status():
    container_name ='elasticsearch'
    try:
        return str(subprocess.check_output("docker inspect --format='{{json .State.Health}}' " + container_name, shell=True)).split('"Status":"')[1].split('"',1)[0]
    except:
        return False

def check_docker():
    try:
        subprocess.check_output('docker ps', shell=True)
        return True
    except:
        return False