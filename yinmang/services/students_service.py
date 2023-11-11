from yinmang.repository.students_repository import StudentRepository
from yinmang.services.base_service import BaseService

class StudentService(BaseService):
    def __init__(self):
        self.students_repository = StudentRepository()
        super().__init__(self.students_repository)
