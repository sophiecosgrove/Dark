from flask import render_template, redirect, url_for
from application import app, db
from application.models import Events
from application.forms import EventForm



@app.route('/')
@app.route('/home')
def home():
    eventData = Events.query.first()
    return render_template('home.html', title='Home Page', event=eventData)

@app.route('/characters')
def characters():
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

    return render_template('addevent.html', title='Add An Event', form=form)


