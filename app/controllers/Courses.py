
from system.core.controller import *

class Courses(Controller):
    def __init__(self, action):
        super(Courses, self).__init__(action)
        self.load_model('Course')

    def index(self):
        course = self.models['Course'].get_all_courses()
        return self.load_view('index.html',course = reversed(course))

    def  show(self, id):        
        course = self.models['Course'].get_course_by_id(id)
        return self.load_view('destroy.html',course = course)   

    def add(self):
        print "hello"
        if len(request.form['course_name'])< 16:
            flash('Course name needs to be longer than 15 caracters')
            return redirect('/')
        else:    
            course_details = {
                'title': request.form['course_name'],
                'description': request.form['description']
            }
            self.models['Course'].add_course(course_details)
            return redirect('/')

    def delete(self, id):
        self.models['Course'].delete_course_by_id(id)
        return redirect('/')  