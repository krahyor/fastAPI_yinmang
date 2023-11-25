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
import pandas as pd

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
    if upload_file.content_type:
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

@router.post("/import_student_file")
async def create_for_students_file(upload_file : UploadFile = File(...,description="Uploaded file Students")) -> list[ResponseStudents]:
    df = pd.read_excel(upload_file.file)
    student_show = []
    for _,row in df.iterrows():
        student = Students()
        first_name = row["ชื่อ"]
        last_name = row["นามสกุล"]
        weight = row["น้ำหนัก"]
        height = row["ส่วนสูง"]
        print(f"{first_name} {last_name} น้ำหนัก {weight} ส่วนสูง {height}")
        if upload_file :
            student.first_name = first_name
            student.last_name = last_name
            student.weight = weight
            student.height = height
            student.save()
            print("successful")
        student_show.append(student)
    return student_show