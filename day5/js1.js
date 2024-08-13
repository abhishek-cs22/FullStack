const username=["user1","user2","u2","u3","u4",{"key1": "value1"},"u5"];
console.log(username[5].key1);
console.log(username[5]["key1"]);
const resume = {
    "name": "Abhishek verma",
    "course": "Btech",
    "branch": "cs",
    "age": "20",
    "contactnumbers": [
      {
        "type": "mobile",
        "label": "contact number",
        "number": 979529492
      },
      {
        "type": "mobile",
        "label": "whatsapp number",
        "number": 9555417242
      }
    ],
    "currentAddress": {
      "houseno": 287,
      "city": "ayodhya",
      "dist": "faizabad",
      "pincode": 224209,
      "state": "up",
      "country": "india"
    },
    "education": {
      "10th": 2020,
      "12th": 2022
    },
    "skills": {
      "programminglanguages": "java,c,c++,python",
      "other": "html, css , js"
    }
  }
console.log(resume)  
console.log(resume.skills)
const resumePreTag = document.getElementById("resume")
resumePreTag.innerText = JSON.stringify(resume,null,2)
console.log(resume.contactnumbers[1])