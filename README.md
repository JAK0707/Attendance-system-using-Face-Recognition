# Attendance-system-using-Face-Recognition

<h1>Face Recognition Attendance System</h1>

This project is a simple face recognition attendance system implemented in Python using OpenCV and Face Recognition libraries. The system captures video from a webcam, detects faces in the video feed, and compares them with known faces to mark attendance. Detected faces are labeled with the corresponding names if they match any known faces.

<h2>Features</h2>
    <ul>
        <li>Real-time face detection and recognition.</li>
        <li>Automatic attendance marking for recognized faces.</li>
        <li>Simple graphical interface showing attendance status.</li>
    </ul>

  <h2>Installation</h2>
    <ol>
        <li>Clone the repository to your local machine:</li>
    </ol>
    <code>git clone https://github.com/JAK0707/face-recognition-attendance.git</code>
    <ol start="2">
        <li>Install the required dependencies:</li>
    </ol>
    <code>pip install -r requirements.txt</code>
    <ol start="3">
        <li>Ensure you have a webcam connected to your system.</li>
    </ol>

  <h2>Usage</h2>
    <ol>
        <li>Add images of individuals whose attendance you want to track in the <code>Faces</code> directory. Make sure the file names correspond to the names of the individuals.</li>
        <li>Run the <code>main.py</code> script:</li>
    </ol>
    <code>python main.py</code>
    <ol start="3">
        <li>The system will start capturing video from your webcam. Detected faces will be labeled with the corresponding names if they match any known faces.</li>
        <li>Press the 'j' key to exit the program and save the attendance data to a CSV file named with the current date.</li>
    </ol>

   <h2>Configuration</h2>
    <ul>
        <li>You can adjust the face recognition model parameters or webcam settings in the <code>main.py</code> script according to your requirements.</li>
        <li>Customize the font, color, and position of attendance labels in the code as needed.</li>
    </ul>

  <h2>Contributors</h2>
    <ul>
        <li><a href="https://github.com/JAK0707">Your Name</a></li>
    </ul>

   

