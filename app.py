import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from flask_migrate import Migrate

from models import setup_db, Teachers, Students, db
from auth import requires_auth


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)


    '''
    Set up CORS. Allow '*' for origins.
    '''
    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

    '''
    Use the after_request decorator to set Access-Control-Allow
    '''
    @app.after_request
    def after_request(response):
        response.headers.add(
            'Access-Control-Allow-Headers',
            'Content-Type,Authorization,true')
        response.headers.add(
            'Access-Control-Allow-Methods',
            'GET,PATCH,POST,DELETE,OPTIONS')
        return response


    '''
    functions used to query
    '''
    def query_models(model):
        return model.query.all()

#  <----------------------------------------Students Section------------------------------------------------->
    '''
    function to json data from request
    '''
    def json_data_input(get_this):
        return request.json.get(get_this)

    '''
    Get all Students from database
    '''
    @app.route('/students', methods=['GET'])  # working fine
    @requires_auth('get:students')
    def get_all_students():

        try:
            all_students = query_models(Students)

            all_students_final = [term.format() for term in all_students]

            return jsonify({
                'Students': all_students_final,
                'Total number of students': len(all_students),
                'success': True
            })
        except Exception:
            abort(500)    
    '''
    Post a new student
    '''
    @app.route('/students', methods=['POST'])  # working fine
    @requires_auth('post:students')
    def addmission_of_new_student():
        try:
            name = json_data_input('name')
            age = json_data_input('age')
            gender = json_data_input('gender')
            teacher_id = json_data_input('teacher_id')

            if not (name and age and gender):
                return abort(400)

            new_student= Students(name, age, gender, teacher_id)
            new_student.insert()

            return jsonify({
                'success': True,
                'message': "Student addmitted successfully",
                'student added': new_student.format()
            })

        except Exception:
            abort(500)
    '''
    Change an students details
    '''
    @app.route('/students/<int:student_id>', methods=['PATCH'])  # working fine
    @requires_auth('patch:students')
    def change_student_details(student_id):
        try:
            student = Students.query.get(student_id)

            if not student:
                abort(400)

            name = json_data_input('name')
            age = json_data_input('age')
            gender = json_data_input('gender')
            teacher_id = json_data_input('teacher_id')

            student.name = name
            student.age = age
            student.gender = gender
            student.teacher_id = teacher_id

            updated_student = Students(name, age, gender, teacher_id)

            updated_student.update()

            return jsonify({
                "success": True,
                "message": "update successfull",
                "student details changed to ": updated_student.format()
            })
        except Exception:
            abort(500)    


    '''
    Delete a Students Details from database
    '''
    @app.route('/students/<int:student_id>', methods=['DELETE'])  # working fine
    @requires_auth('delete:students')
    def delete_student(student_id):
        try:
            student = Students.query.get(student_id)

            if student is None:
                return abort(404)
            else:
                student.delete()
                return jsonify({
                    'success': True,
                    'deleted': student_id
                })

        except Exception:
            abort(500)
    '''
    Search a student
    '''
    @app.route('/search/students', methods=['POST'])  # working fine
    @requires_auth('search:students')
    def search_student():

        student_name_to_search = request.json.get('searchTerm', '')

        if (student_name_to_search == ''):
            abort(422)

        studentFound = Students.query.filter(
            Students.name == student_name_to_search).all()

        if not studentFound:
            abort(404)

        return jsonify({
            'success': True,
            'message': 'Students are found',
        })

#  <----------------------------------------Teachers Section------------------------------------------------->

    '''
    Get all Teachers from database
    '''
    @app.route('/teachers', methods=['GET'])  # working fine
    @requires_auth('get:teachers')
    def all_teacher_details():
        try:
            all_teachers = query_models(Teachers)
            all_teachers = [term.format() for term in all_teachers]

            for teachers in all_teachers:
               teachers['students'] = [term.format() for term in teachers['students']]
            


            return jsonify({
                'Teachers': all_teachers,
                'Total number of teachers': len(all_teachers),
                'success': True
            })
        except Exception:
            abort(500)    
            

    '''
    Post a new teachers details
    '''
    @app.route('/teachers', methods=['POST'])  # working fine
    @requires_auth('post:teachers')
    def add_newteacher_detail():
        try:
            name = json_data_input('Name')
            age = json_data_input('age')

            if not (name and age):
                return abort(400)

            teachers_details = Teachers(name, age)
            teachers_details.insert()

            return jsonify({
                'success': True,
                'message': 'Teacher details added successfully',
                'teacher added': teachers_details.format()
            })
        except Exception:
            abort(500)    
      


    '''
    Change a Teachers details
    '''
    @app.route('/teachers/<int:teacher_id>', methods=['PATCH'])  # working fine
    @requires_auth('patch:teachers')
    def change_teacher_details(teacher_id):
        try:
            teacher = Teachers.query.get(teacher_id)

            if not teacher:
                abort(400)

            name = json_data_input('name')
            age = json_data_input('age')

            teacher.name = name
            teacher.age = age

            updated_teacher = Teachers(name, age)

            teacher.update()

            return jsonify({
                "success": True,
                "message": "Teachers details updated successfull",
                "teacher details changed to ": updated_teacher.format()
            })
        except Exception:
            abort(500)    


    '''
    Delete a Teacher from Database
    '''
    @app.route('/teachers/<int:teacher_id>', methods=['DELETE'])  # working fine
    @requires_auth('delete:teachers')
    def delete_teacher(teacher_id):
        try:

            teacher = Teachers.query.get(teacher_id)

            if teacher is None:
                return abort(404)
            else:
                teacher.delete()
                return jsonify({
                    'success': True,
                    'deleted': teacher_id
                })
        except Exception:
            abort(500)


    '''
    Error handlers for expected errors
    '''

    # Error handler for 404-Not found
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "Not found"
        }), 404

    # Error handler for 422-Unprocessable Entity
    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "Unprocessable Entity"
        }), 422

    # Error handler for 400-bad request
    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "Bad Request"
        }), 400

    # Error handler for 500-Internal Server Error
    @app.errorhandler(500)
    def internal_server_error(error):
        return jsonify({
            "success": False,
            "error": 500,
            "message": "Internal server error"
        }), 500

    return app


app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

#https://dev-qk8ecx2h.us.auth0.com/authorize?audience=coaching&scope=SCOPE&response_type=token&client_id=2HGaMMj7PC3h4qgnMSQBzyhH09MmJfqL&redirect_uri=https://127.0.0.1:5500//login-result