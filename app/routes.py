from flask import render_template
from app import app
import status

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    elastic_local = status.is_elastic_local()
    docker_status = status.check_docker()
    elastic_status = status.check_elasticsearch_status()
    kibana_status = status.check_kibana_status()
    return render_template('index.html', title='Home', user=user, elastic_local = elastic_local, docker_status=docker_status, elastic_status=elastic_status, kibana_status=kibana_status)