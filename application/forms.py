from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError
from application.models import Events, Characters

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
    submit = SubmitField('Add Event')

    def validate_event(self, event):
        event = Events.query.filter_by(event=event.data).first()

        if event:
            raise ValidationError('Event already logged')

class CharacterForm(FlaskForm):
    name = StringField('Name',
            validators = [
                DataRequired(),
                ]
            )
    mother = StringField('Mother')
    father = StringField('Father')
    hair_colour = StringField('Hair Colour',
            validators = [
                DataRequired(),
                Length(min=3, max=30)
                ]
            )
    eye_colour = StringField('Eye Colour',
            validators = [
                DataRequired(),
                Length(min=3, max=30)
                ]
            )
    status = StringField('Alive or Deceased',
            validators = [
                DataRequired(),
                Length(min=3, max=30)
                ]
            )
    submit = SubmitField('Add Character')

    def validate_character(self, character):
        character = Characters.query.filter_by(character=name.data).first()

        if event:
            raise ValidationError('Character already logged')

