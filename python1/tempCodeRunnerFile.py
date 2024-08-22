with open("resume.json") as file:
    resume=json.load(file)
    for key, value in resume.items():
        print(key, value)