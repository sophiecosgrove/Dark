import unittest

from flask import url_for
from flask_testing import TestCase

from application import app, db
from application.models import Events, Characters
from os import getenv

class TestBase(TestCase):
    def create_app(self):
        config_name = 'testing'
        app.config.update(SQLALCHEMY_DATABASE_URI=getenv('TEST_DB_URI'),
            SECRET_KEY=getenv('TEST_SECRET_KEY'),
            WTF_CSRF_ENABLED=False,
            DEBUG=True
            )
        return app

    def setUp(self):
        db.session.commit()
        db.drop_all()
        db.create_all()

        character = Characters(name="test", mother="testmother", father="testfather", hair_colour='testhair', eye_colour='testeye', status='teststatus')


        db.session.add(character)
        db.session.commit()

        event = Events( season=1, episode=1, character='test', from_year=1990, to_year=2020, event='test entry')
        db.session.add(event)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestViews(TestBase):
    def test_characters_view(self):
        response = self.client.get(url_for('characters'))
        self.assertEqual(response.status_code, 200)

    def test_home_view(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

    def test_addevent_view(self):
        response = self.client.get(url_for('addevent'))
        self.assertEqual(response.status_code, 200)
        
    def test_addcharacter_view(self):
        response = self.client.get(url_for('addcharacter'))
        self.assertEqual(response.status_code, 200)

    def test_eventlog_view(self):
        response = self.client.get(url_for('eventlog'))
        self.assertEqual(response.status_code, 200)

class TestPosts(TestBase):

    def test_add_new_character(self):
        response = self.client.post(
            '/addcharacter',
            data=dict(
                name='testname', 
                mother='testmother',
                father='testfather', 
                hair_colour='testhair',
                eye_colour='testeeye',
                status='teststatus'
            ),
            follow_redirects=True
            )
        self.assertIn(b'Your character has been added!', response.data)
        with self.client:
            response =self.client.get(url_for('character', character_id=1))
            self.assertEqual(response.status_code, 200)
        with self.client:
            response = self.client.get(url_for('update_character', character_id=1))
            self.assertEqual(response.status_code, 200)
            response = self.client.post(
                '/character/1/update',
            data=dict(
                name='testname', 
                mother='testmother',
                father='testfather', 
                hair_colour='testhairchange',
                eye_colour='testeeye',
                status='teststatus'
            ),
            follow_redirects=True
            )
            self.assertIn(b'Character has been updated!', response.data)
        with self.client: 
            response = self.client.post(
            '/addevent',
            data=dict(
                season=1, 
                episode=1,
                character= 'testname', 
                from_year=1990,
                to_year=2020,
                event='addeventpgtest'
            ),
            follow_redirects=True
            )
        self.assertIn(b'Your event has been added!', response.data)
        with self.client:
            response =self.client.get(url_for('event', event_id=1))
            self.assertEqual(response.status_code, 200)
        with self.client:
            response = self.client.get(url_for('update_event', event_id=1))
            self.assertEqual(response.status_code, 200)
            response = self.client.post(
                '/event/1/update',
                data=dict(
                season=1, 
                episode=1,
                character='testcharacter', 
                from_year=2020,
                to_year=2000,
                event='testevent'
            ),
            follow_redirects=True
            )
            self.assertIn(b'Event has been updated!', response.data)
        with self.client:
            response = self.client.get(url_for('delete_event', event_id=1))
            self.assertEqual(response.status_code, 405)
        with self.client:
            response = self.client.get(url_for('delete_character', character_id=1))
            self.assertEqual(response.status_code, 405)

''' class UpdatePosts(TestBase):
    d
        response = self.client.post(
            '/addcharacter',
            data=dict(
                name='testname', 
                mother='testmother',
                father='testfather', 
                hair_colour='testhair',
                eye_colour='testeeye',
                status='teststatus'
            ),
            follow_redirects=True
            )
        self.assertIn(b'Your character has been added!', response.data)
       
        with self.client:
            response = self.client.post(
            '/addevent',
            data=dict(
                season=1, 
                episode=1,
                character='addeventpgtest', 
                from_year=1990,
                to_year=2020,
                event='addeventpgtest'
            ),
            follow_redirects=True
            )
        self.assertIn(b'Your event has been added!', response.data) '''
        
        
    






