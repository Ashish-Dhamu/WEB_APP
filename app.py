from flask import Flask, request, jsonify, json
from google_sheet import Student
app = Flask(__name__)
app.config["DEBUG"] = True


#C:\Users\ASHISH\Downloads\dhamu-python-dev-8a7f55b3e94c.json
@app.route("/")
def index():
    student = Student.find_by_id(5002)
    return json.dumps(student)

if __name__ == "__main__":
    app.run(port=3000)