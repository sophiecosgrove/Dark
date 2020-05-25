# Dark
In fulfillment of the week 6 project.

# Requirements
* To create a CRUD application which utilises the technologies and methods we have learned up to this point, such as; 
* A Kanban style board, with full expansion on user stories, use cases and tasks needed to complete the project. It can also contain a record of any risks or issues faced,
* A relational database with at least two tables which share a relationship,
* Clear documentation from a design phase describing the architecture used for the project as well as a detailed Risk Assessment,
* A functional CRUD application created in Python, following best practices and design principles,
* Test suites and automated tests for the application. Must have a high coverage with consistent reports and evidence,
* A functioning front end and integrated APIs, using flask,
* A version control system using the Feature-Branch model, 
* Code built through a CI server and deployed to a cloud based VM.

# Solution 
I have designed a blog based on the Netflix show 'Dark'. The program is about timetravel, with the plot of the show becoming complicated. Therefore, I decided to make a website displaying the events in the show so that viewers can keep on track with the plot.
Users are able to create, retrieve, update and delete both characters and events using the website interface, which is then connected to an sql database where the information is stored. 

# Technologies Used
* Kanban Board: Trello
* Database: GCP SQL Server
* Programming language: Python
* Unit Testing with Python (Pytest)
* Integration Testing with Python (Selenium)
* Front-end: HTML, Bootstrap CSS.
* Version Control: Git
* CI Server: Jenkins
* Cloud server: GCP Compute Engine

# Trello Boards
* I planned my Trello boards and tasks around the technology and activities that were taking place throughout the week in training. My first trello board was very conceptual, outlining the requirements for the project such as, user stories and MoSCoW as well as tasks to complete. Over the course of my Kanban plotting, I found it helpful to add class tasks onto the board as we completed them if I knew that they were relevant to my project, this helped me to keep on track of tasks and plan my time effectively.
![imageoftrello1](https://github.com/sophiecosgrove/Dark/blob/master/images/Trello1.png)
![imageoftrello1.5](https://github.com/sophiecosgrove/Dark/blob/master/images/Trello1.5.png)
* Once we started to learn flask, I was able to keep up with learning through practicing on our class blog and then also applying it to my project throughout the day. I found it helpful to add reminders onto my Trello board to do these exercises.I also began to add in issues I was facing or concerns I encountered which I then went back to and appended the solution I adopted to address them. 
![imageoftrello2](https://github.com/sophiecosgrove/Dark/blob/master/images/Trello2.png)
![imageoftrello2.5](https://github.com/sophiecosgrove/Dark/blob/master/images/Trello2.5.png)
* My final Trello documents that I have not managed to get integration testing set up. I did write some tests however I have not automated it through jenkins. There is also one constraint that I have not managed to fix, this has been added to my future risk considerations below.
![imageoftrello3](https://github.com/sophiecosgrove/Dark/blob/master/images/Trello3.png)
![imageoftrello3.5](https://github.com/sophiecosgrove/Dark/blob/master/images/Trello3.5.png)

# Architecture
## Initial design
![imageoferd1](https://github.com/sophiecosgrove/Dark/blob/master/images/erd%201.png)
## Final design 
![imageoferd2](https://github.com/sophiecosgrove/Dark/blob/master/images/erd%20after.png)
## Commentary 
Initially I had planned to have three tables, one for characters, events and years. I thought about including more details about the family of the character, as this is quite a central concept in the show due to different family members being present in each of the time frames. However, I reconsidered this as it would make both the code and database quite complex, as well as possibly making the experience for the user inputting the details less enjoyable. I also planned to have more fields for the events table, detailing who the person met, what happened and what was discovered, however I thought that this text might complicate the readability of the database and the site. Therefore, I decided to keep it more streamlined, having just the central points of where the character travelled from and to and the main implications of this travel. I also added in the columns for season and episode, as I thought it would be more functional to have the events logged as the user encounters them throughout the plot of the show rather than ordered chronologically.  Additionally, I had planned to have a years table detailing the years that have been travelled to in the show and the status of the nuclear power plant at this time, as this is a central part of the storyline. However, after consideration I decided that it wasn't necessary to have this as a table, as there wouldn't need to be as many entries, so it would make more sense to have this as a page designed by the admin that could remain fairly stable over time.
## Relationships
0 to Many - A character can never travel through time, so never appear in the event log, or they can travel multiple times and appear many times in the event log.
1 to 1 - One event can only have one character.
1 to Many - A year could appear either once or many times in the eventlog, but to exist in the years table the year will have been implicated in an event so therefore the minimum amount is one.
1 to 1 - One event can only have one year that is visited.



# System Level Design
## CI pipeline
![imageofcipipeline](https://github.com/sophiecosgrove/Dark/blob/master/images/CI%20pipelinepic.png)
* Code was developed, tested and pushed to github. The code is then pulled by Jenkins and a build is created, deploying the website into the live environment. - Webhook. Gunicorn SystemDservice is used to establish the persistence of the website being hosted, it is successfully set up to manage the background processes to automate the delivery of the website as much as possible.

# Testing
## Unit Testing 
* On my first initial implementation of pytest and with inputting a few basic get requests to display websites and one post function, the coverage was 53%, with the main problem being the routes page which was at 27%. 
![imageofcov53](https://github.com/sophiecosgrove/Dark/blob/master/images/cov53.png)
* After completing the get requests for all pages of the website, the overall percentage was 59% with the routes page being at 37%.
![imageofcov59](https://github.com/sophiecosgrove/Dark/blob/master/images/cov59.png)
* Through adding another post function for the add characters page, the coverage went up to 71% overall and 60% for the routes.py.
![imageofcov71](https://github.com/sophiecosgrove/Dark/blob/master/images/cov71.png)
* After adding the update and delete functions for both the characters and events to the test code, the coverage went up to 89%.
![imageofcov89](https://github.com/sophiecosgrove/Dark/blob/master/images/covreport89.png)
* After updating the foreign key in models.py, the tests failed as it was necessary for there to be a character existing in the database before an event was added so that the event could have the character_id. I re-wrote the tests and entered a character in before an event with the corresponding character id.
* The next step was to print the __repr__ functions in the models.py file, which brought the models.py coverage from 91% to 100%. After deleting a custom validator from the events form, which wasn't working due to there already being a working one above which was causing the code to skip over this function, the forms.py coverage went up from 91% to 100%. This meant the overall coverage was 96%, with the routes being 93%.
![imageofcov96](https://github.com/sophiecosgrove/Dark/blob/master/images/cov96.png)
* After changing the code again to ensure that if a character is deleted, all corresponding events are also deleted. The coverage went up to 97%.
![imageofcov97](https://github.com/sophiecosgrove/Dark/blob/master/images/cov97.png)
* Finally, after rewriting the delete function for the events, the coverage went up to 99% with one line missing from routes. 
![imageofcov99](https://github.com/sophiecosgrove/Dark/blob/master/images/cov99.png)
* The missing line of code is triggered when a character is deleted and all corresponding events must be deleted, however when ran through the tests, it appears that the page for the event that should have been deleted with the character is still accessible. When trying this through the website it is not, however the webpage does sometimes need to be refreshed after the character has been deleted, therefore this might be causing a slight issue with the test. I also added an action = 'POST' to the get request as I was aware that perhaps the page was being accessed but the deletion was not being submitted, however this did not appear to change anything.


# Risk assesment
## Initial
![imageofinitialriskassessment](https://github.com/sophiecosgrove/Dark/blob/master/images/risk%20assessment%20before.png)
* Initial risks consisted of mainly theoretical considerations as I was approaching the project from a planning and conceptual perspective rather than technical. I was mainly concerned with the project not being completed as I was not experienced in the tools and methods we would be using. However I have completed the project and gained confidence in the skills that we have learnt and I feel that I have successfully applied them. The other risks detailed in the register were based on theoretical use of the website, and what I presumed would affect the usability. These risks are still therefore applicable and thus appear in my future considerations.
## Future Risk Considerations
![finalriskassessment](https://github.com/sophiecosgrove/Dark/blob/master/images/futurerisks.png)
* Future risk considerations are what I consider to be encountered by users if they use the website. Should the website go into deployment, these are the issues that I would need to address. 

# Front end design
The use of a layout.html was used to provide a base template for all pages of the website. Jinja2 syntax was used to extend the layout onto each page. Each page was passed through the route function as a render template. I created the front-end design using HTML and some Bootstrap CSS, making use of their container, colours, text colours, alert and button classes. I used a static file to store the custom CSS classes.
![imageofhomepage](https://github.com/sophiecosgrove/Dark/blob/master/images/Homepage.png)
![imageofcharacterpage](https://github.com/sophiecosgrove/Dark/blob/master/images/CharacterPage.png)
![imageofeventpage](https://github.com/sophiecosgrove/Dark/blob/master/images/EventLog.png)
![imageofcharacteradded](https://github.com/sophiecosgrove/Dark/blob/master/images/addcharacter.png)
![imageofeventadded](https://github.com/sophiecosgrove/Dark/blob/master/images/addevent.png)

# Acceptance Criteria
* I am satisfied that the MVP for this project was met.
## User Stories
* A user can successfully create, review, update and delete events and characters on the website. If there is a problem with their entry such that the data entered is not valid, they will be notified. In addition, if they attempt to enter a character which is already in the database, they will get a message. This means that the user can fulfill the user stories.
## MoSCow
The must have criteria for this project was met - A database with two tables: Events and Characters with essential columns for each so that the user can understand the show. Full CRUD functionality. 
The should have criteria was also met - Relations between family members, what years they existed in, characteristics, alive yes or no. This means that the information on the website is meaningful and will aid the user in understanding the plot of the show.
The could have criteria was not met as it was beyond the criteria for the project. - A years table. 
The wont have criteria was also not met as it was beyond the criteria for the project - images of the characters at different stages of their lives. 

# Future improvements
I could add photographs and these would help identification of the characters and also improve the experience of using the website.
A more detailed and graphically relevant time line would show events and their implications in a more structured and meaningful way. The show follows a very complicated plot, so a page for plot theories and latest developments in the plot would be useful and it would also allow for a more enjoyable experience of the website if users could exchange and contribute their own theories. As for the character fields that were omitted, in the future I could have a character profile that appears when the individual character is selected from the characters page. Here the details could be added by the admin so that it doesn't affect the users experience of the site but provides much more information.


# Authors
Sophie Cosgrove
