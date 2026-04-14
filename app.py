from flask import Flask, request, jsonify #flask create server, #request get incoming data, #jsonify return json response
import json, os

from matcher import find_best_match
from logger import log_event

app = Flask(__name__) #create web server inst

def load_data():
    with open("data/students.json", "r") as f:
        students = json.load(f)
    with open("data/mentors.json", "r") as f:
        mentors = json.load(f)

    return students, mentors
@app.route("/")
def home():
    return "AI Mentor Matchmaker"
@app.route('/match', methods=['POST'])
def match_student():
    data = request.json
    student = data['student']

    students, mentors = load_data()
    match = find_best_match(student, mentors)
    log_event(str(student['name']) + " matched with " + str(match['name']))
    return jsonify({
        'student': student['name'],
        'matched_mentor': match['name']
    })

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)

