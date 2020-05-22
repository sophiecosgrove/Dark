# Dark
In fulfillment of the week 5 CRUD application project

# Requirements
To create a CRUD application of our choice that uses the technologies and methods we have learned up to this point namely: *A Kanban     board *A relational database to store at least two tables persistently and a model of their relationship *Clear documentation and a     risk assesment *A python based CRUD application made using best practices such as TDD *Test suites and automated tests for the           application. Must have a high coverage with consistent reports and evidence *A functioning front end *A version control system using     the Feature-Branch model *Code built through a CI server and deployed to a cloud based VM

# Solution 
I have designed a blog based on the Netflix show 'Dark'. The program is about timetravel, with the plot of the show becoming complicated. Therefore, I decided to make a website displaying the events in the show so that viewers can keep on track with the plot.
Users are able to create, retrieve, update and delete both characters and events using the website interface, which is then connected to an sql database where the information is stored. 

# Technologies Used
Kanban Board: Trello
Database: GCP SQL Server
Programming language: Python
Unit Testing with Python (Pytest)
Integration Testing with Python (Selenium)
Front-end: Flask (HTML), CSS, JavaScript
Version Control: Git
CI Server: Jenkins
Cloud server: GCP Compute Engine

# Trello Boards

# Architecture
## Initial design
![imageoferd1](https://github.com/sophiecosgrove/Dark/blob/master/erd%201.png)
## Final design 
![imageoferd2](https://github.com/sophiecosgrove/Dark/blob/master/erd%20after.png)
## Commentary 
Initially I had planned to have three tables, one for characters, one for events and one for years. I thought about including more details about the family of the character, as this is quite a central concept in the show due to different family members being present in each of the time frames. However, I reconsidered this would make both the code and database quite complex, as well as possibly making the experience for the user inputting the details less enjoyable. I also planned to have more fields for the events table, detailing who the person met, what happened and what was discovered, however I thought that this text might complicate the readability of the database and the site. Therefore, I decided to keep it more streamlined, having just the central points of where the character travelled from and to and the main implications of this travel. Additionally, I had planned to have a years table detailing the years that have been travelled to in the show and the status of the nuclear power plant at this time, as this is a central part of the storyline and the explanation for the time travel being possible. However, after consideration I decided that it wasn't necessary to have this as a table, as there wouldn't need to be as many entries, so it would make more sense to have this as a page designed by the admin that could remain fairly stable over time. ~ relationship



# System Level Design
## CI pipeline
![imageofcipipeline](https://github.com/sophiecosgrove/Dark/blob/master/CI%20pipelinepic.png)

# Testing
On my first initial implementation of pytest and with inputting a few basic get requests to display websites and one post function, the coverage was 44%, with the main problem being the routes page which was at 27%. After completing the get requests for all pages of the website and adding another post function for the characters database, the coverage went up to 67% overall and 55% for the routes.py. After sucessfully adding the update and delete functions for both the characters and events to the test code, the coverage went up to 89%. 
After updating the foreign key, the tests failed as it was necessary for there to be a character existing in the database before an event was added so that the event could have the character_id. I re-wrote the tests so that within each test session, if an event was being added/updated or deleted, there would always be a character for it to be able to link to.

The next step was to print the __repr__ functions in the models.py file, which brought the models.py coverage from 91% to 100%. After deleting a custom validator from the events form, which wasn't working due to their already being a working one above which was causing the code to skip over this function, the forms.py coverage went up from 91% to 100%. I also had an app.py file which was falsely repeated in the applications folder as well as being in the root of the project, so I removed this which improved the overall score to 94%.

After changing the code again to get rid of an error that was happening as a result of characters being deleted when they existed in events, it meant that one of the tests failed. The test needed to be changed to account for this. After this the coverage stands at 97%. 

# Risk assesment
## Initial
![imageofinitialriskassessment](https://github.com/sophiecosgrove/Dark/blob/master/risk%20assessment%20before.png)
final

# Bugs and Fixes

# Front end design
pics

# Future improvements
I could add photographs and these would help identification of the characters and also improve the experience of using the website.
A more detailed and graphically relevant time line would show events and their implications in a more structured and meaningful way. The show follows a very complicated plot, so a page for plot theories and latest developments in the plot would be useful and it would also allow for a more enjoyable experience of the website if users could exchange and contribute their own theories. As for the character fields that were omitted, in the future I could have a character profile that appears when the individual character is selected from the characters page. Here the details could be added by the admin so that it doesn't affect the users experience of the site but provides much more information.


# Authors
Sophie Cosgrove
