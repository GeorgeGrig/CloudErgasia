from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired

# Create search for fields
class SearchForm(FlaskForm):
    no_results = StringField(
        'Number of results', default="30", validators=[DataRequired()])
    index = StringField(
        'Source Index', default="packetbeat-7.16.0", validators=[DataRequired()])
    # custom_query = StringField('Number of results', default="30")
    destination_packets = StringField(
        'Destination packets', default="*", description="destination.packets")
    destination_port = StringField(
        'Destination port', default="*", description='destination.port')
    event_duration = StringField(
        'Event duration', default="*", description='event.duration')
    # timestamp = StringField('Time range here', default="*")
    network_bytes = StringField(
        'Network bytes', default="*", description='network.bytes')
    source_port = StringField(
        'Source port', default="*", description='source.port')
    match_all = BooleanField('Show all entries')
    submit = SubmitField('Search')
