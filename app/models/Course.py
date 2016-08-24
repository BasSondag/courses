
from system.core.model import Model

class Course(Model):
    def __init__(self):
        super(Course, self).__init__()
    
    def add_course(self, course):
        query = "INSERT INTO courses (title, description, created_at) VALUES (%s, %s, NOW())"
        data = [course['title'], course['description']]
        return self.db.query_db(query, data)

    def get_all_courses(self):
        query = "SELECT * FROM courses"
        return self.db.query_db(query)

    def get_course_by_id(self, course_id):
        query = "SELECT * FROM courses WHERE id = %s"
        data = [course_id]
        return self.db.query_db(query, data)

    def delete_course_by_id(self, course_id):
        query = " DELETE FROM courses WHERE id = %s"
        data =[course_id]
        return self.db.query_db(query, data)