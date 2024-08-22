import json
# task 5

with open("resume.json") as file:
    resume=json.load(file)
    for key, value in resume.items():
        print(key, value)


# task 6
# def read_resume():
#     with open("resume.json") as file:
#         resume=json.load(file)
#         for key, value in resume.items():
#             print(key, value)

# for _ in range(5):
#     read_resume()