from flask import render_template, redirect, url_for, flash, request
from application import app, db
from application.models import Events, Characters
from application.forms import EventForm, CharacterForm, UpdateEventForm, UpdateCharacterForm



@app.route('/')
@app.route('/home')
def home():
    eventData = Events.query.first()
    return render_template('home.html', title='Home Page', event=eventData)

@app.route('/characters')
def characters():
    characterData = Characters.query.all()
    return render_template('characters.html', title='Character Page', characters=characterData)

@app.route('/years')
def years():
    return render_template('years.html', title='Years Page')

@app.route('/eventlog')
def eventlog():
    eventData = Events.query.all()
    return render_template('eventlog.html', title='Event Log Page', events=eventData)

@app.route('/addevent', methods=['GET', 'POST'])
def addevent():
    form = EventForm()
    if form.validate_on_submit():
        eventData = Events(
                season = form.season.data,
                episode = form.episode.data,
                character = form.character.data,
                from_year = form.from_year.data,
                to_year = form.to_year.data,
                event = form.event.data
        )
        db.session.add(eventData)
        db.session.commit()
        flash('Your event has been added!', 'success')
        return redirect(url_for('eventlog'))
    else:
        print(form.errors)

    return render_template('addevent.html', title='Add an Event', form=form)

@app.route('/addcharacter', methods=['GET','POST'])
def addcharacter():
    form = CharacterForm()
    if form.validate_on_submit():
        characterData = Characters(
                name = form.name.data,
                mother = form.mother.data,
                father = form.father.data,
                hair_colour = form.hair_colour.data,
                eye_colour = form.eye_colour.data,
                status = form.status.data
                )
        db.session.add(characterData)
        db.session.commit()
        flash('Your character has been added!', 'success')
        return redirect(url_for('characters'))
    else:
        print(form.errors)

    return render_template('addcharacter.html', title='Add a Character', form=form)

@app.route('/event/<int:event_id>')
def event(event_id):
    event = Events.query.get_or_404(event_id)
    return render_template('event.html', title = event.id, event = event)

@app.route('/event/<int:event_id>/update', methods=['GET', 'POST'])
def update_event(event_id):
    event = Events.query.get_or_404(event_id)
    form = UpdateEventForm()
    if form.validate_on_submit():
        event.season = form.season.data
        event.episode = form.episode.data
        event.character = form.character.data
        event.from_year = form.from_year.data
        event.to_year = form.to_year.data
        event.event = form.event.data
        db.session.commit()
        flash('Event has been updated!', 'success')
        return redirect(url_for('event', event_id=event.id))
    elif request.method == 'GET':
        form.season.data = event.season
        form.episode.data = event.episode
        form.character.data = event.character
        form.from_year.data = event.from_year
        form.to_year.data = event.to_year
        form.event.data = event.event
    return render_template('addevent.html', title = 'Update Event', form = form)

@app.route("/event/<int:event_id>/delete", methods=['POST'])
def delete_event(event_id):
    event = Events.query.get_or_404(event_id)
    db.session.delete(event)
    db.session.commit()
    flash('Event has been deleted!', 'success')
    return redirect(url_for('eventlog'))

@app.route('/character/<int:character_id>')
def character(character_id):
    character = Characters.query.get_or_404(character_id)
    return render_template('character.html', title = character.id, character = character)

@app.route('/character/<int:character_id>/update', methods=['GET', 'POST'])
def update_character(character_id):
    character = Characters.query.get_or_404(character_id)
    form = UpdateCharacterForm()
    if form.validate_on_submit():
        character.name = form.name.data
        character.mother = form.mother.data
        character.father = form.father.data
        character.hair_colour = form.hair_colour.data
        character.eye_colour = form.eye_colour.data
        character.status = form.status.data
        db.session.commit()
        flash('Character has been updated!', 'success')
        return redirect(url_for('character', character_id=character.id))
    elif request.method == 'GET':
        form.name.data = character.name
        form.mother.data = character.mother
        form.father.data = character.father
        form.hair_colour.data = character.hair_colour
        form.eye_colour.data = character.eye_colour
        form.status.data = character.status
    return render_template('addcharacter.html', title = 'Update Character', form = form)

@app.route("/character/<int:character_id>/delete", methods=['POST'])
def delete_character(character_id):
    character = Characters.query.get_or_404(character_id)
    db.session.delete(character)
    db.session.commit()
    flash('Character  has been deleted!', 'success')
    return redirect(url_for('characters'))
