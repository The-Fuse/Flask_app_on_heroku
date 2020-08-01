# Full Stack Coaching institute API Backend

## About
The Coaching institute a company that is responsible for  taking admission of students  for counselling by a teacher. A user needs to have appropriate permissions to get, post, patch or delete teachers and students in the database.

The app has counsellor who can get all details of teachers and students and search the students, but not change anything.
However, the viceprincipal have the permission to see all details of get any teacher and student data and also change any details or add more teachers or students but can't delete any teacher and students.
But Principal has all the permissions to change, add, update , search or delete any teacher or students data via correct endpoints.

The permission tokens are added under 'JWT Tokens' section of readme.

All the endpoints and their implementations are added under 'Endpoints' section of readme. However to use them, you have to use postman or curl.

## DEPLOYMENT
The app is hosted live on heroku at the URL: 
http://coaching123.herokuapp.com/

However, there is no frontend for this app yet, and it can only be presently used to authenticate using Auth0 by entering
credentials and retrieving a fresh token to use with curl or postman.

## THIRD-PARTY AUTHENTICATION
#### auth.py
Auth0 is set up and running. The following configurations are in a .env file which is exported by the app:
- The Auth0 Domain Name
- The Auth0 Client ID
The JWT token contains the permissions for the 'Principal', 'Viceprincipal', 'Counseller' roles.

### Installing Dependencies

#### Python

Install Python3.7 using official python docs.


#### PIP Dependencies from requirements.txt

You can install all required pip dependencies from requirements.txt using -

```
pip3 install -r requirements.txt
```

##### Other Dependencies Required

- Flask
- Flask-CORS
- SQLAlchemy

## Local Database setup

After creating the database, you can use the following commands to create required relations-
```
flask db init
flask db migrate
flask db upgrade
```


## Running the server

First export the required environment variables from setup.sh for that terminal using
```
source setup.sh
``` 

Then you can run the server from root directory using
```
python3 app.py
```

## Project Details:

The Coaching institute a company that is responsible for  taking admission of students  for counselling by a teacher

#### Models:

There are two models in the projects for teachers and students respectively-

- Teachers with attributes name and  age
- Students with attributes name, age and gender

#### Roles:

- Counsellor
    "get:students",
    "get:teachers"
    "search:students "
- Vice Principal
    "get:students"
    "get:teachers"
    "patch"students"
    "patch:teachers"
    "post:students"
    "post:teachers"
    "search:students"
- Principal
    "get:students"
    "get:teachers"
    "patch"students"
    "patch:teachers"
    "post:students"
    "post:teachers"
    "search:students"
    "delete:students"
    "delete:teacher"


## API DOCUMENTATION

### Endpoints

For using these endpoints, you have to send a jwt token with each request and with appropriate permissions to access that particular endpoints. I have already added tokens in the 'JWT tokens' section of this readme.
Since the application don't have a frontend, you can use curl or postman to use these endpoints.

- GET '/students' - used to get all students
- GET "/teachers" - used to get all teachers
- POST "/teachers" - used to add more teachers
- POST "/students" - used to add more students
- PATCH "/teachers/int:teacher_id"  -   used to change details of specific teacher details
- PATCH "/students/int:student_id"  -   used to change details of specific stydents details
- DELETE "/students/int:student_id" - used to delete a specific student data
- DELETE "/teachers/int:teacher_id" - used to delete a specific teacher
- POST "/search/students" - used to search a specific student with it's name as search term


##### GET '/teachers'

- Fetches a dictionary of teachers with key:value pair of total number of teachers.
- Request Arguments: None
- Permission: required
- Returns:
``` 
{
    "Teachers": [
        {
            "Name": "Rohit Kumar",
            "age": 20,
            "id": 1,
            "students": [
                {
                    "age": 44,
                    "gender": "Male",
                    "id": 1,
                    "name": "Duke Stark",
                    "teacher_id": 1
                }
            ]
        }
    ],
    "Total number of teachers": 1,
    "success": true
}
```


##### GET "/students"
- Fetches a dictionary of all students with key:value pair of total number of students
- Request Arguments: None
- Permission: required
- Returns:
```
{
    "Students": [
        {
            "age": 44,
            "gender": "Male",
            "id": 1,
            "name": "Duke Stark",
            "teacher_id": 1
        }
    ],
    "Total number of students": 1,
    "success": true
}
```

##### POST "/teachers"
- Adds a new teacher details to the database
- Request Arguments: required
    - name : name of the teacher
    - age : age of the teacher
- Permission: required
- Returns :
```
{
    "message": "Teacher details added successfully",
    "success": true,
    "teacher added": {
        "Name": "Rohit Kumar",
        "age": 20,
        "id": 1,
        "students": []
    }
}
```

##### POST "/students"
- Addmits a new student to the database
- Request Arguments: required
    - name : name of student
    - age : age of age of the student
    - gender : gender of student
    - teacher_id : teacher_id of teacher alloted
- Permission: required
- Returns :
```
{
    "message": "Student addmitted successfully",
    "student added": {
        "age": 44,
        "gender": "Male",
        "id": 1,
        "name": "Duke Stark",
        "teacher_id": 1
    },
    "success": true
}
```

##### PATCH "/teachers/int:teacher_id"
- Used to change details of a specific teacher details
- Request Parameters: Present
    teacher_id: teacher ID needed to be changed
- Returns :
```
{
    "message": "Teachers details updated successfull",
    "success": true,
    "teacher details changed to ": {
        "Name": Changed name,
        "age": 20,
        "id": null,
        "students": []
    }
}
```

##### PATCH "/students/int:student_id"
- Used to change details of a specific student
- Request Parameters: Present
    student_id: student ID needed to be changed
- Returns :
```
{
    "message": "update successfull",
    "student details changed to ": {
        "age": 18,
        "gender": "Female",
        "id": 1,
        "name": "Duke Stark",
        "teacher_id": 1
    },
    "success": true
}
```

##### DELETE "/teachers/int:teacher_id"
- Delete a specific teacher data from database
- Request Arguments: Present
    teacher_id: ID of the teacher
- Response Body:
```
{
    "deleted": 2,
    "success": true
}
```

##### DELETE "/students/int:student_id"
- Delete a specific student from database
- Request Arguments: Present
    student_id: ID of the student  
- Response Body:
```
{
    "deleted": 1,
    "success": true
}
```

##### POST "/search/students"
- Search a specific student from database
- Request Arguments: Present  
- Response Body:
```
{
    "message": "Students are found",
    "success": true
}
```


### JWT Tokens:

- Counsellor
```
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkVaS1B1MWFMekstX3RKcndJUENObSJ9.eyJpc3MiOiJodHRwczovL2Rldi1xazhlY3gyaC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWYxM2U5ZWZkZTNiNTkwMDE5MjRmOTNiIiwiYXVkIjoiY29hY2hpbmciLCJpYXQiOjE1OTUxNTI1NTMsImV4cCI6MTU5NTIzODk1MywiYXpwIjoiMkhHYU1NajdQQzNoNHFnbk1TUUJ6eWhIMDlNbUpmcUwiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDpzdHVkZW50cyIsImdldDp0ZWFjaGVycyIsInNlYXJjaDpzdHVkZW50cyJdfQ.rk6ka1N8d-DZ7tgf271Lj9STzU9zr9bBzKOtzfGUuFSP5GdCsk-bJxB9k2-97-bHSZX3cLnmlIRInn47dHuWBm4qT6M6aNwsIVd7kgKZPBBd2dnZa7Mn9d_ITWu2dR7zGKodAG3fejdInBaaxp0pV1BYdOZ212c6Ed7L0Z92f0gEgSgNFZ8SazVVKyxc3_DcYsS8rqulyjp38mittbQin-eXzBDUQQ1Q5jtAX5xHWfKdCDgwIpkXf3ZSjS7Hk0hdOKTIKS3F5xc8Q7XwFKmUXdONSFmA0ySRDsP_ScGr0p9ebZnc-qGJPC351_dQC-6ezNFvDG5cKHXeFQC8lH7stA
```

- Vice Principal
```
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkVaS1B1MWFMekstX3RKcndJUENObSJ9.eyJpc3MiOiJodHRwczovL2Rldi1xazhlY3gyaC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWYxM2VhNjFkZTNiNTkwMDE5MjRmOTQwIiwiYXVkIjoiY29hY2hpbmciLCJpYXQiOjE1OTUxNTI0ODIsImV4cCI6MTU5NTIzODg4MiwiYXpwIjoiMkhHYU1NajdQQzNoNHFnbk1TUUJ6eWhIMDlNbUpmcUwiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDpzdHVkZW50cyIsImdldDp0ZWFjaGVycyIsInBhdGNoOnN0dWRlbnRzIiwicGF0Y2g6dGVhY2hlcnMiLCJwb3N0OnN0dWRlbnRzIiwicG9zdDp0ZWFjaGVycyIsInNlYXJjaDpzdHVkZW50cyJdfQ.PCH0T6rs5bbcHySIpRxPhgcSO6gVR27qU0PavmHBnC_fWhwPMT2RnlGBH8Xl-bv0oNHpE_gH47SGoki9MpCVsy5YbFM_o6EaFLJX32igUUJPtb_tDT84xMrivtk18-OejH75HPETYgub0350cajrBkPQqJC-Kn_PhuAuToAcM1kLcNFtPVgaiblX_Ajg4m6OimQIWCGRpgKIV-jinqZwUO8G4O1g1R9LpkLDaZJ6v--rTqiy0XIN886s22lQ1K2S7GoHL-t4SnKtCVPXx2-Chx3A34HQ4Jcpp0Pp7eXZuKSyja2j9tmGxtK6rAe5wbmGfdtQ0pyjrESohZ-iw_EBXQ
```


- Principal
```
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkVaS1B1MWFMekstX3RKcndJUENObSJ9.eyJpc3MiOiJodHRwczovL2Rldi1xazhlY3gyaC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWYxM2VhMmM3ZmY2MGQwMDE5ZDY2NjA0IiwiYXVkIjoiY29hY2hpbmciLCJpYXQiOjE1OTUxNTIzNzMsImV4cCI6MTU5NTIzODc3MywiYXpwIjoiMkhHYU1NajdQQzNoNHFnbk1TUUJ6eWhIMDlNbUpmcUwiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTpzdHVkZW50cyIsImRlbGV0ZTp0ZWFjaGVycyIsImdldDpzdHVkZW50cyIsImdldDp0ZWFjaGVycyIsInBhdGNoOnN0dWRlbnRzIiwicGF0Y2g6dGVhY2hlcnMiLCJwb3N0OnN0dWRlbnRzIiwicG9zdDp0ZWFjaGVycyIsInNlYXJjaDpzdHVkZW50cyJdfQ.fQlsPeFOPzgaVDi5-EIgJ82_3XMQV6GqwV7LNFhaMYby8TwFdnLM-Yz6gIubYrG-h4ri6FkaGMP1z-653usyPi4aLZkkbKqHegnLTd2WNpXArWmxgv1Mepz-v-TIDduE5OioH423RhBbDFuG8VxA7y1HzLQ1UXqLCtFIZyDsbRt7Cc5Jo8hf_guJcadoZAVIVJvb_2ZyW7MM3_xzEPAWfufNhwqe1yR0Hk8EU_T8jzewZYq98_BD-BF4sEfwqDKi6QDdrRJuS8g2ekKXQlexGLk2K2m1G5SNDSma3j914YVpWrjEPdhVYfaSma_AKFtkYchIpEUDf6OaLoT0OHWFvQ
```

All of the above was expired
