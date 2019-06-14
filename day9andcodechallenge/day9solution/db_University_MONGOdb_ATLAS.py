
import pymongo

# connecting mongoDB Atlas and accessing database
client = pymongo.MongoClient("mongodb+srv://himanshu:Database%40123@cluster0-ktyqe.mongodb.net/test?retryWrites=true&w=majority")
mydb = client.University

# to add student in Students collection on mongoDB cloud
def add_student(name,age,roll_no,branch):
    unique_student = mydb.students.find_one({"Roll No.":roll_no})
    if unique_student:
        return "Student already exists"
    else:
        mydb.students.insert_one(
            {
            "Name" : name,
            "Age" : age,
            "Roll No" : roll_no,
            "Branch" : branch
            })
    return "Student added successfully"

# Storing data
add_student('Himanshu',21,'A045','CS')
add_student('Ashish',20,'A019','CS')
add_student('Kritika',19,'A053','CS')
add_student('Divya',19,'A036','CS')
add_student('Hitesh',20,'A046','CS')
add_student('Lakshya',20,'A056','CS')
add_student('Aditya',21,'A08','CS')
add_student('Akshay',20,'A06','CS')
add_student('Abhishek',21,'A01','CS')
add_student('Kushal',21,'A052','CS')

# to fetch all students in Students collection on mongoDB cloud
def fetch_all_student():
    student_collection = mydb.students.find()
    for document in student_collection:
        print(document)

fetch_all_student()