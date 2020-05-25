import unittest
import time
from flask import url_for
from urllib.request import urlopen

from os import getenv
from flask_testing import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from application import app, db
from application.models import Characters, Events

class TestBase(LiveServerTestCase):

    def create_app(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = getenv('TEST_DB_URI')
        app.config['SECRET_KEY'] = getenv('TEST_SECRET_KEY')
        return app

    def setUp(self):
        """Setup the test driver and create test users"""
        test_character = 'start'
        test_character_name = "testcharacter"
        test_character_mother = "mother"
        test_character_father = "father"
        test_character_hair_colour = "hair colour"
        test_character_eye_colour = "eye colour"
        test_character_status = "status"

        test_event = 'start'
        test_event_season = 1
        test_event_episode = 1
        test_event_character = 'testcharacter'
        test_event_from_year = 2020
        test_event_to_year = 2050
        test_event_event = 'testevent'
        print("--------------------------NEXT-TEST----------------------------------------------")
        chrome_options = Options()
        chrome_options.binary_location = "/usr/bin/chromium-browser"
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(executable_path="/home/sophi/Dark/chromedriver", chrome_options=chrome_options)
        self.driver.get("http://localhost:5000")
        db.session.commit()
        db.drop_all()
        db.create_all()

    def tearDown(self):
        self.driver.quit()
        print("--------------------------END-OF-TEST----------------------------------------------\n\n\n-------------------------UNIT-AND-SELENIUM-TESTS----------------------------------------------")

    def test_server_is_up_and_running(self):
        response = urlopen("http://localhost:5000")
        self.assertEqual(response.code, 200)

class TestAddCharacter(TestBase):

    def test_character(self):
        """
        Test that a user can create an account using the registration form
        if all fields are filled out correctly, and that they will be 
        redirected to the login page
        """

        # Click register menu link
        self.driver.find_element_by_xpath("//*[@id='navbarToggle']/div[2]/a[2]").click()
        time.sleep(1)

        # Fill in registration form
        self.driver.find_element_by_xpath('//*[@id="name"]').send_keys(test_character_name)
        self.driver.find_element_by_xpath('//*[@id="mother"]').send_keys(
            test_character_mother)
        self.driver.find_element_by_xpath('//*[@id="father"]').send_keys(
            test_character_father)
        self.driver.find_element_by_xpath('//*[@id="hair_colour"]').send_keys(
            test_character_hair_colour)
        self.driver.find_element_by_xpath('//*[@id="eye_colour"]').send_keys(
            test_character_eye_colour)
        self.driver.find_element_by_xpath('//*[@id="status"]').send_keys(
            test_character_status)
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        time.sleep(2)

        # Assert that browser redirects to login page
        assert url_for('characters') in self.driver.current_url

        if __name__ == '__main__':
            unittest.main(port=5000)

class TestAddEvent(TestBase):

    def test_event(self):
        """
        Test that a user can create an account using the registration form
        if all fields are filled out correctly, and that they will be 
        redirected to the login page
        """

        # Click register menu link
        self.driver.find_element_by_xpath("/html/body/header/nav/div/div/div[2]/a[1]").click()
        time.sleep(1)

        # Fill in registration form
        self.driver.find_element_by_xpath('/html/body/div/div/form/input[2]').send_keys(
            test_event_season)
        self.driver.find_element_by_xpath('/html/body/div/div/form/input[3]').send_keys(
            test_event_episode)
        self.driver.find_element_by_xpath('/html/body/div/div/form/input[4]').send_keys(
            test_event_character)
        self.driver.find_element_by_xpath('/html/body/div/div/form/input[5]').send_keys(
            test_event_from_year)
        self.driver.find_element_by_xpath('/html/body/div/div/form/input[6]').send_keys(
            test_event_to_year)
        self.driver.find_element_by_xpath('/html/body/div/div/form/input[7]').send_keys(
            test_event_event)
        self.driver.find_element_by_xpath('/html/body/div/div/form/input[8]').click()
        time.sleep(1)

        # Assert that browser redirects to login page
        assert url_for('eventlog') in self.driver.current_url

        if __name__ == '__main__':
            unittest.main(port=5000)