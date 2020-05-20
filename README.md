# Dark
In fulfillment of the week 5 CRUD application project

Requirements
To create a CRUD application of our choice that uses the technologies and methods we have learned up to this point namely: *A Kanban board *A relational database to store at least two tables persistently and a model of their relationship *Clear documentation and a risk assesment *A python based CRUD application made using best practices such as TDD *Test suites and automated tests for the application. Must have a high coverage with consistent reports and evidence *A functioning front end *A version control system using the Feature-Branch model *Code built through a CI server and deployed to a cloud based VM

Solution 
I have designed a blog based on the Netflix show 'Dark'. The program is about timetravel, with the plot of the show becoming complicated. Therefore, I decided to make a website displaying the events in the show so that viewers can keep on track with the plot.
Users are able to create, retrieve, update and delete both characters and events using the website interface, which is then connected to an sql database where the information is stored. 

Technologies Used
Kanban Board: Trello
Database: GCP SQL Server
Programming language: Python
Unit Testing with Python (Pytest)
Integration Testing with Python (Selenium)
Front-end: Flask (HTML), CSS, JavaScript
Version Control: Git
CI Server: Jenkins
Cloud server: GCP Compute Engine

Trello Boards

Architecture
Initial design - erd1 
Erd2
final design, why, how it changed

system level design - CI pipeline

Testing
On my first initial implementation of pytest and with inputting a few basic get requests to display websites and one post function, the coverate was 44%, with the main problem being the routes page which was at 27%. After completing the get requests for all pages of the website and adding another post function for the characters database, the coverage went up to 67% overall and 55% for the routes.py. After sucessfully adding the update and delete functions for both the characters and events to the test code, the coverage went up to 89%. The next step was to print the __repr__ functions in the models.py file, which brought the models.py coverage from 91% to 100%. After deleting a custom validator from the events form, which wasn't working due to their already being a working one above which was causing the code to skip over this function, the forms.py coverage went up from 91% to 100%. I also had an app.py file which was falsely repeated in the applications folder as well as being in the root of the project, so I removed this which improved the overall score to 94%.

Risk assesment
initial - discuss
final

Bugs and Fixes

Front end design
pics

Future improvements
I could add photographs and these would help identification of the characters and also improve the experience of using the website.
A more detailed and graphically relevant time line would show events and their implications in a more structured and meaningful way. The show follows a very complicated plot, so a page for plot theories and latest developments in the plot would be useful and it would also allow for a more enjoyable experience of the website if users could exchange and contribute their own theories. 


Authors
Sophie Cosgrove
