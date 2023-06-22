************************ File Handling Test Task ****************************************
Note:
- please use the application in chrome browser

########################### Starting application ############################### 
-Requirements
1) need a python maching
2) install all package from requirements.txt file 
    -$ pip install -r requirements.txt
3) create new database or used the existing database with sample data already present
4) move to file_handler folder in terminal
5) run following command if you are using new database to make table changes to db
    -$ python manage.py makemigrations
    -$ python manage.py migrate
6) craete a user using django createsuperuser code or use the sample user's
    -$ python manage.py createsuperuser
    Sample user password
    - username: rahulkumar, password: rahulk5665
    - username: testuser, password: rahulk5665
    - username: admin, password: admin
7) run below code and start the application with your port number
    -$ python manage.py runserver 0.0.0.0:7000
8) visit http://localhost:7000/ and use the application

Note: 
- I have used django framework because in the question flask is not the mandatory framework
- I have implemented medifile file check for user level so that current user cannot access the file of other users
- Sample screenshot is present please check

######################### Question #########################

Objective:

Your task is to develop a simple, web-based file viewer application that allows users to upload, store, and view text and image files within 10 days.

The application should include the following features:

1. User Registration & Login: Allow users to create an account, login, and logout.

2. File Upload & Storage: Users should be able to upload text (.txt) and image files (.jpg, .png) to their account, view a list of uploaded files, and delete any file if needed.

3. File Viewing: Users should be able to view the uploaded text and image files in the browser without the need to download them.

4. Basic Security Measures: User data and files should be protected using basic security measures such as encrypted passwords and secure file transfer.
To assist you in this challenge, we have provided some sample images at Competition Details & Samples that you can use for testing purposes.

Technologies:

You can choose your preferred tech stack, but for simplicity, this project suggests:

- Frontend: HTML, CSS, JavaScript (or a simple framework like jQuery)
- Backend: Node.js with Express.js, or Python with Flask
- Database: SQLite or MongoDB
- File storage: Local file system (for simplicity, but keep in mind this isn't suitable for production)

Deliverables:

- Source code stored in a Git repository
- A README.md file in the repository detailing how to run the application locally, and any other relevant information about your submission.

Evaluation Criteria:

Your project will be evaluated based on the following:

- Fulfillment of the above requirements
- Quality of the code (Is it organized? Is it easy to understand?)
- Basic level of security practices
- Quality of the user interface (Is it easy to use? Is it responsive?)

Please note that early submissions will be given preference during evaluation. Therefore, if you are able to complete the challenge before the 10-day deadline, we strongly encourage you to submit it early.

########################## Thank you ####################################