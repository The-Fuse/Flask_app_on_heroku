# COACHING INSTITUTE
The Coaching institute a company that is responsible for  taking admission of students  for counselling by a teacher. A user needs to have appropriate permissions to get, post, patch or delete teachers and students in the database.

The app has counsellor who can get all details of teachers and students and search the students, but not change anything.
However, the viceprincipal have the permission to see all details of get any teacher and student data and also change any details or add more teachers or students but can't delete any teacher and students.
But Principal has all the permissions to change, add, update , search or delete any teacher or students data via correct endpoints.

The permission tokens are added under 'JWT Tokens' section of readme.

All the endpoints and their implementations are added under 'Endpoints' section of readme. However to use them, you have to use postman or curl, since the app doesn't have any frontend yet.

The app is hosted on heroku and the url for the same is as follows-
**Application URL - https://coaching123.herokuapp.com/ **

### JWT Tokens:

- Counsellor
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjJkVnBmeHE5RS0xS1paSlNTQVU5QiJ9.eyJpc3MiOiJodHRwczovL2Rldi1xOGI5c210aC51cy5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMDU2ODA5NDE5Njc3NjM2NjUzMTYiLCJhdWQiOlsibXlhcHAiLCJodHRwczovL2Rldi1xOGI5c210aC51cy5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNTk0OTYyNzE4LCJleHAiOjE1OTUwNDkxMTgsImF6cCI6IkpaTUMzNzBXYmNnNVphUW9LU0l4a1FPeW9iTVcwRVVvIiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsInBlcm1pc3Npb25zIjpbImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwic2VhcmNoOmFjdG9ycyIsInNlYXJjaDptb3ZpZXMiXX0.MuRbpTp6rXMdJgIbMtUMYv7zZUn2-785XQG2UqYQzz7mhsxMXgmJDECx66xK5AbSQuuVC_03NwYKvPjYwkOqvz5ggvDKRtzQNi8bylsLIXg1xI6Y1NJkAibTbaLyHBUuuC_jlcVdlDezFc4-ZCxNWlZGEqY64CAsFU3NxCXGMI14G-Uc4xLmgIqW2G7gLOiRq5-mJMcOMPq1IyKEslqS0JaXY4h-mbXZFoR7EWmdldxVjIIf7aTGnDx4ayBeZNdgPh3uTVHToBoyJWolQ9RDtDSEsuEEZt7TqNpp3XHKjbswB6DZbRptN6xeTfZ8OPc6e81B9AWkJbacGqQqaIu_EA

- Vice Principal
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjJkVnBmeHE5RS0xS1paSlNTQVU5QiJ9.eyJpc3MiOiJodHRwczovL2Rldi1xOGI5c210aC51cy5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMDU2MzkxNzEyMjUxMDQ4MjgyMzMiLCJhdWQiOlsibXlhcHAiLCJodHRwczovL2Rldi1xOGI5c210aC51cy5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNTk0OTYyNzgxLCJleHAiOjE1OTUwNDkxODEsImF6cCI6IkpaTUMzNzBXYmNnNVphUW9LU0l4a1FPeW9iTVcwRVVvIiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIiwic2VhcmNoOmFjdG9ycyIsInNlYXJjaDptb3ZpZXMiXX0.E3MHvC2HpYtrwBulxQbYFUs47x5xbFLIpxe6HBcUqwriBErn2LfqsLvqoRONoKgs-DbK8vftvXpYntNTNRJzflQPfiphgP3LgopNU0zg2r96YRAvYQM3GhKsYa2Lw6ix2MxPQH5NY4DjHVYy8qqKpXjcknfYolBqGbuiaqgIiEeisicTprqGSDf-GCZopcenvo_qZoCTBweqwSKOaWjoOLYJ5vF6jtPCc-TRUXmMwI_VezWyu-H8e0afNRMSKqRORJtS10tofcxY1uIvuBSEm5ChE2EFr93IWvglh6fx0U7evEa3dZM0TlBbmPtx-HWSECzTCxRr78lOwKevjtZXfA


- Principal
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjJkVnBmeHE5RS0xS1paSlNTQVU5QiJ9.eyJpc3MiOiJodHRwczovL2Rldi1xOGI5c210aC51cy5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMDE1Mzg4MDU0Nzc3MzQ4ODAyMDEiLCJhdWQiOlsibXlhcHAiLCJodHRwczovL2Rldi1xOGI5c210aC51cy5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNTk0OTYyODM3LCJleHAiOjE1OTUwNDkyMzcsImF6cCI6IkpaTUMzNzBXYmNnNVphUW9LU0l4a1FPeW9iTVcwRVVvIiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIiwic2VhcmNoOmFjdG9ycyIsInNlYXJjaDptb3ZpZXMiXX0.orSa4uybbWvQ2m4TO7wFZ0gaaovySi9D7RxyPWMRjAArzHRc8gtavGpq1Qmoc2_bjAtb8kN7yMRErXzPVqqfjIz7EEYm-Gxv3j3X94dnTcvRvyvcUXg3DZoUpTkvxzM1Au6cSeey0T_hHdY65INPwWu8L09-4gsNtqTiCMBZRpa-3fw-d3mm2KsraDHRfT_vECHTjrpoJT-sWqKMuF-eObKFWcFcV4qDMn6czCHsCAFxHHC7WGdZUDqggQzJzluBS4g_KWAHvRm-etYESM02PNtubIrxALLweuvmSE4aWcBXUEG-7NsJdijij96iKEGdgWng7C0zIqAXgq2-knnj2w

### Installing Dependencies

#### Python

Install Python3.7 using official python docs.

#### Virtual Environment (venv)

You can use virtual environment to keep all your python dependencies separate.
To setup virtual environment 
- Install virtual environment using
```
pip install virtualenv
```
- To create a virtual environment use
```
virtualenv name_of_virtualenv
```

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

