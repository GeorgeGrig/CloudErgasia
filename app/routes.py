from flask import render_template, redirect
from app import app
from app.forms import LoginForm
import status
import functionality
app.config['SECRET_KEY'] = 'potatoes'
@app.route('/', methods=['GET', 'POST'])
def index():
    form = LoginForm()
    api_response = False
    q_size = 0
    elastic_local = status.is_elastic_local()
    docker_status = status.check_docker()
    elastic_status = status.check_elasticsearch_status()
    kibana_status = status.check_kibana_status()
    if form.validate_on_submit():
        api_response, q_size = functionality.create_query(form)
    return render_template('index.html', title='Home', form=form, q_size=q_size, api_response = api_response, elastic_local = elastic_local, docker_status=docker_status, elastic_status=elastic_status, kibana_status=kibana_status)