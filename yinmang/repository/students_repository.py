from yinmang.models import Students
from yinmang.repository.base_repository import BaseRepository

class StudentRepository(BaseRepository):
    def __init__(self):
        super().__init__(Students)