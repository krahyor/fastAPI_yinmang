from typing import Union

from yinmang.schemas.student_schema import ResponseStudents, BaseStudents
from yinmang.services import StudentService
from fastapi_pagination import Page
from fastapi import APIRouter,Depends
from fastapi.responses import JSONResponse
from fastapi_pagination.ext.mongoengine import paginate

router = APIRouter()

@router.get("/",response_model=Page[ResponseStudents])
async def index(student_service: StudentService = Depends(StudentService)):
    student = student_service.get_list()
    return paginate(student)

@router.post("/create", response_model=ResponseStudents)
async def create_student(student: BaseStudents,StudentsService = Depends(StudentService)) :
    student = StudentsService.add(student)
    return student

@router.patch("/update/{student_id}",response_model=ResponseStudents)
async def update_student(student_id: str,student: BaseStudents,student_service: StudentService = Depends(StudentService)):
    student = student_service.patch(student_id,student)
    return student

@router.delete("/delete/{student_id}", response_model=BaseStudents)
async def delete_student(student_id: str ,student_service : StudentService = Depends(StudentService)):
    student = student_service.delete_by_id(id=student_id)
    return student