from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Student(BaseModel):
    id: int
    name: str
    email: str

students = [
    Student(id=1, name="Maria Silva", email="maria.silva@pucpr.edu.br"),
    Student(id=2, name="Carlos Santos", email="carlos.santos@pucpr.edu.br"),
    Student(id=3, name="Jéssica Machado", email="jessica.machado@pucpr.edu.br")
]

@app.post("/students/", response_model=Student)
def create_student(student: Student):
    # Checks whether the student already exists
    for existing_student in students:
        if existing_student.id == student.id:
            raise HTTPException(status_code=400, detail="Student already exists")
    
    students.append(student)
    return student

@app.get("/students/", response_model=List[Student])
def read_students(skip: int = 0, limit: int = 10):
    return students[skip : skip + limit]

@app.get("/students/{student_id}", response_model=Student)
def read_student(student_id: int):
    for student in students:
        if student.id == student_id:
            return student
    raise HTTPException(status_code=404, detail="Student not found")

@app.put("/students/{student_id}", response_model=Student)
def update_student(student_id: int, updated_student: Student):
    for index, student in enumerate(students):
        if student.id == student_id:
            students[index] = updated_student
            return updated_student
    raise HTTPException(status_code=404, detail="Student not found")

@app.delete("/students/{student_id}", response_model=Student)
def delete_student(student_id: int):
    for index, student in enumerate(students):
        if student.id == student_id:
            deleted_student = students.pop(index)
            return deleted_student
    raise HTTPException(status_code=404, detail="Student not found")

# Running the application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
