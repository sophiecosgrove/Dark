from flask import render_template, redirect, url_for
from application import app, db
from application.models import Events, Characters
from application.forms import EventForm, CharacterForm



@app.route('/')
@app.route('/home')
def home():
    eventData = Events.query.first()
    return render_template('home.html', title='Home Page', event=eventData)

@app.route('/characters')
def characters():
    characterData = Characters.query.all()
    return render_template('characters.html', title='Character Page')

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
        
        return redirect(url_for('characters'))
    else:
        print(form.errors)

    return render_template('addcharacter.html', title='Add a Character', form=form)
