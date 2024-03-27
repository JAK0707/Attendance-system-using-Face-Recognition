# ATTENDANCE TAKER PROGRAM USING FACE RECOGNITION
# MADE BY - JAIDITYA ABHINEET KAPOOR

import csv
import face_recognition
import cv2
import numpy as np
from datetime import datetime

# Accessing Camera
video_capture = cv2.VideoCapture(0)

# Load Known faces
dennis_image = face_recognition.load_image_file("Faces/dennis.jpg")
dennis_face_encoding = face_recognition.face_encodings(dennis_image)[0]

bjarne_image = face_recognition.load_image_file("Faces/bjarne.jpg")
bjarne_face_encoding = face_recognition.face_encodings(bjarne_image)[0]

guido_image = face_recognition.load_image_file("Faces/guido.jpg")
guido_face_encoding = face_recognition.face_encodings(guido_image)[0]

james_image = face_recognition.load_image_file("Faces/james.jpg")
james_face_encoding = face_recognition.face_encodings(james_image)[0]

jai_image = face_recognition.load_image_file("Faces/jai.jpg")
jai_face_encoding = face_recognition.face_encodings(jai_image)[0]

saif_image = face_recognition.load_image_file("Faces/saif.jpg")
saif_face_encoding = face_recognition.face_encodings(saif_image)[0]

psrana_image = face_recognition.load_image_file("Faces/psrana.jpg")
psrana_face_encoding = face_recognition.face_encodings(psrana_image)[0]

# Store all known face encodings and their corresponding names
known_face_encodings = [dennis_face_encoding, bjarne_face_encoding, guido_face_encoding, james_face_encoding, jai_face_encoding, saif_face_encoding]
known_face_names = ["Dennis", "Bjarne", "Guido", "James", "Jai", "Saif Sir", "PS Rana Sir"]

# List of programmers
programmers = known_face_names.copy()

# Initializing variables to store face locations and encodings
face_locations = []
face_encodings = []

# Get the current date and time
now = datetime.now()
current_date = now.strftime("%Y-%m-%d")

# Creating a CSV file for attendance data
f = open(f"{current_date}.csv", "w+", newline="")
lnwriter = csv.writer(f)

while True:
    # Read a frame from the camera
    _, frame = video_capture.read()
    # Resize the frame
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    # Recognize faces
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    # Loop through each detected face
    for face_encoding in face_encodings:
        # Compare the face encoding with known face encodings
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)

        if (matches[best_match_index]):
            # Get the name of the recognized face
            name = known_face_names[best_match_index]

        # Add a text if a person is present
            if name in known_face_names:
                font = cv2.FONT_HERSHEY_SIMPLEX
                bottom_left_corner_of_text = (10, 100)
                fontScale = 1.5
                fontColor = (255, 0, 0)
                thickness = 3
                lineType = 2
                cv2.putText(frame, name + " Present", bottom_left_corner_of_text, font, fontScale, fontColor, thickness,
                            lineType)

            # If a person is recognised then remove them from the list
            if name in programmers:
                programmers.remove(name)
                current_time = now.strftime("%H-%M-%S")
                lnwriter.writerow([name, current_time])

    # Displaying the attendance frame
    cv2.imshow("Attendance", frame)

    # Check for 'j' key press to exit the loop and end the program
    if cv2.waitKey(1) & 0xFF == ord('j'):
        break

# Release the camera and close all OpenCV windows
video_capture.release()
cv2.destroyAllWindows()

# Close the CSV file
f.close()