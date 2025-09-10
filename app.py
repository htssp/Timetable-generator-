from flask import Flask, render_template, request
import random
import pandas as pd

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    timetable = []
    if request.method == "POST":
        courses = request.form.get("courses").split(",")
        rooms = request.form.get("rooms").split(",")
        timeslots = request.form.get("timeslots").split(",")

        courses = [c.strip() for c in courses if c.strip()]
        rooms = [r.strip() for r in rooms if r.strip()]
        timeslots = [t.strip() for t in timeslots if t.strip()]

        used_slots = set()
        random.shuffle(courses)

        for course in courses:
            assigned = False
            slot_list = timeslots[:]
            random.shuffle(slot_list)
            for slot in slot_list:
                for room in rooms:
                    if (slot, room) not in used_slots:
                        used_slots.add((slot, room))
                        timetable.append({"Course": course, "Room": room, "Timeslot": slot})
                        assigned = True
                        break
                if assigned:
                    break

    return render_template("index.html", timetable=timetable)

if __name__ == "__main__":
    app.run(debug=True)
