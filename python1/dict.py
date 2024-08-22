student = {
    "name" : "abhishek verma",
    "age" : 20,
    "hobbies":["playing","reading","coding"],
    "isstudent" : True,
    "sampletuple" : (1,2,3),
    "sampleset" : {1,2,3},
    "sampledict" : {"name":"john","age" : 21}
}
print(student)
print(student["name"])
print(student["sampledict"])

keys = ["name","age","isstudent","sampletuple","sampleset","hoobies","sampledict"]

for key in keys:
    if key in student:
        print(key,student[key])
    else:
        print(f"{key} is not present")

for index,hobby in enumerate(student["hobbies"]):
    print(index,hobby)
