from typing import Union,Any
from pydantic import BaseModel

from yinmang.schemas.student_schema import ResponseStudents, BaseStudents
from yinmang.services import StudentService
from fastapi_pagination import Page
from fastapi import APIRouter,Depends,UploadFile,File
from fastapi_pagination.ext.mongoengine import paginate
from yinmang.models import Files , Students

import datetime
import json

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

@router.post("/upload")
async def upload_file(upload_file : UploadFile = File(...,description="Uploaded file")) :
    files = Files()
    if upload_file.content_type in ['png', 'jpg', 'jpeg']:
        files.file = upload_file.file
        files.status = "completed"
        files.file_name = upload_file.filename
        files.save()
        return {"file_name":upload_file.filename, "status": "completed"}
    return {"Fail":"Failure"}

@router.get("/student", response_model=list[ResponseStudents])
async def students() -> list[ResponseStudents] :
    students = Students.objects()
    return students

@router.get("/student/{student_id}" ,response_model=ResponseStudents)
async def get_students(student_id:str)-> ResponseStudents :
    student = Students.objects.get(id=student_id)
    return student
