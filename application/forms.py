from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError
from application.models import Events

class EventForm(FlaskForm):
    season = IntegerField('Season',
            validators = [
                DataRequired(),
            ]
        )
    episode = IntegerField('Episode',
            validators = [
                DataRequired(),
            ]
        )
    character = StringField('Character Name',
            validators = [
                DataRequired(),
                Length(min=2, max=100)
            ]
        )
    from_year = IntegerField('Travelled from',
            validators = [
                DataRequired(),
            ]
        )
    to_year = IntegerField('Travelled to',
            validators = [
                DataRequired(),
            ]
        )
    event = StringField('Event',
            validators = [
                DataRequired(),
                Length(min=5, max=500)
            ]
        )
    submit = SubmitField('Add Event!')

    def validate_event(self, event):
        event = Events.query.filter_by(event=event.data).first()

        if event:
            raise ValidationError('Event already logged')
