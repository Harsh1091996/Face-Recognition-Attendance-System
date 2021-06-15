# Face-Recognition-Attendance-System
These project is part of the “Industrial Practice II” curriculum as final year project at [Presidency University](https://presidencyuniversity.in/). 

#### -- Project Status: [Completed]

## Objective<br>
Taking and tracking student’s attendance manually is a time consuming process. In order to make the
attendance system accurate I am developing a system that record student’s attendance automatically
without faculty member’s manual interference through Face Recognition Technique.

<h2> :floppy_disk: Project Files Description</h2>

<p>This Project includes 3 executable files, 6 HTML files  and 1 project documentation  as follows:</p>
<h4>Executable Files:</h4>
<ul>
  <li><b>1. addStudent.py</b> - Code for adding student details into database and generate face encodings.</li>
</ul>
<ul>
  <li><b>2. attendance.py</b> - Code for initializing attendance process using face recognition technique.</li>
</ul>
<ul>
  <li><b>3. mailsend.py</b> - Code for sending attendance sheet to the email address.</li>
</ul>

<h4>HTML Files:</h4>
<ul>
  <li><b>1. facelogin.html</b> - Login page .</li>
</ul>
<ul>
  <li><b>2. act.html</b> - Action page where three options are there a.) Enroll Student b.) Take attendance c.) Send attendance.</li>
</ul>
<ul>
  <li><b>3. registration.html</b> - Registration page where student need to register by entering their Name and ID </li>
</ul>
<ul>
  <li><b>4. registeredsuccess.html</b> - Registration success page where message will be displayed that Student registration successfully. </li>
</ul>
<ul>
  <li><b>5. attendance.html</b> - Attendance success page where message will be displayed that Attendance has been taken successfully. </li>
</ul>
<ul>
  <li><b>6. attendsent.html</b> - Attendance sent success page where message will be displayed that Attendance has been send successfully to registered email id. </li>
</ul>



<h4>Documentation:</h4>
<ul>
  <li><b>Face recognition based attendance system.pdf</b> - Includes the documentation of the project.</li>
</ul>

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

### Methods Used
* Histogram of oriented gradients(HOG)
* Deep Learning
* Machine Learning


### Technologies
* Python
* Numpy
* Face Recognition
* OpenCV
* Dlib
* Flask
* OpenPyxl


## Project Description
* Encode a picture using the HOG algorithm to create a simplified version of the image. Using this simplified image, find the part of the image that most looks like a generic HOG encoding of a face.
* Figure out the pose of the face by finding the main landmarks in the face. Once we find those landmarks, use them to warp the image so that the eyes and mouth are centered.
* Pass the centered face image through a neural network that knows how to measure features of the face. Save those 128 measurements.
* Looking at all the faces we’ve measured in the past, see which person has the closest measurements to our face’s measurements. That’s our match!



## Needs of this project

- Web app developer
- OpenCV and Face_Recognition module expert
- Database handling


![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

<h2> :clipboard: Execution Instruction</h2>
<p>The order of execution of the program files is as follows:</p>
<p><b>1) addStudent.py</b></p>
<p> addStudent.py contains the  code for registering the student into database</p>
<p><b>1) attendance.py</b></p>
<p> attendance.py contains the  code for initializing the attendance process</p>
<p><b>1) mailsend.py</b></p>
<p> mailsend.py contains the  code for sending the attendance to registered email id</p>

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

## Getting Started

1. Clone this repo (for help see this [tutorial](https://help.github.com/articles/cloning-a-repository/)).
2. Project documentation is being kept [here](https://github.com/Harsh1091996/Face-Recognition-Attendance-System/blob/main/Face%20recognition%20based%20attendance%20system.pdf) within this repo.    
3. All the codes of project is being kept [here](https://github.com/Harsh1091996/Face-Recognition-Attendance-System)
 




<!-- CREDITS -->
<h2 id="credits"> :scroll: Credits</h2>

Himanshu Sharma | Avid Learner | Data Scientist | Machine Learning Engineer | Deep Learning enthusiast

<p> <i> Contact me for Data Science Project Collaborations</i></p>


[![LinkedIn Badge](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/himan-10/)
[![GitHub Badge](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Harsh1091996)
[![Medium Badge](https://img.shields.io/badge/Medium-1DA1F2?style=for-the-badge&logo=medium&logoColor=white)](https://harshsharma1091996.medium.com/)
[![Resume Badge](https://img.shields.io/badge/resume-0077B5?style=for-the-badge&logo=resume&logoColor=white)](https://drive.google.com/file/d/1pyTvHo2Ec4xfCszL7YkHYAwWgFi5Uf2T/view?usp=sharing)

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)
<h2> :books: References</h2>
<ul>
  <li><p>Github, 'Install dlib and face_recognition on a Raspberry Pi'. [Online].</p>
      <p>Available: https://gist.github.com/ageitgey/1ac8dbe8572f3f533df6269dab35df65</p>
  </li>
  <li><p>Wikipedia.org, 'Face Recognition System'. [Online].</p>
      <p>Available: https://en.wikipedia.org/wiki/Facial_recognition_system</p>
  </li>
  <li><p>Youtube.com, 'Face Detection using HOG and DLib'. [Online].</p>
      <p>Available: https://www.youtube.com/watch?v=7kjxxP2N3lU</p>
  </li>
  <li><p>Adam Geitgey, 'Build Face Recognition System'. [Online].</p>
      <p>Available: https://medium.com/@ageitgey/machine-learning-is-fun-part-4-modern-face-recognition-with-deep-learning-c3cffc121d78</p>
  </li>
</ul>

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)
