from typing import Union

from yinmang.schemas.student_schema import ResponseStudents, BaseStudents
from yinmang.services import StudentService
from fastapi import APIRouter,Depends
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get("/")
def read_root():
    return {"Hello": "World"}

@router.post("/create", response_model=ResponseStudents)
async def create_student(student: BaseStudents,StudentsService = Depends(StudentService)) :
    student = StudentsService.add(student)
    return student