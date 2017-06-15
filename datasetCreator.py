import cv2 
import sqlite3

cam = cv2.VideoCapture(0)
detector=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def InsertndUpdate(id,name,department,gender,course_name):
    conn = sqlite3.connect("studentsFaceData.db")
    cmd = "SELECT * FROM students WHERE roll="+ str(id)
    cursor = conn.execute(cmd)
    existence = 0
    for row in cursor:
        existence = 1
    if(existence == 1):
        change = input('Roll number already exists do you want to replace it?(y/n):')
        if(change == 'y'):
            cmd = "UPDATE students SET name="+str(name)+" WHERE roll="+str(id)
        else:
            print("no change made")
            conn.close()
    else:
        cmd = "INSERT INTO students(roll,name,department,gender,studying) Values("+str(id)+","+str(name)+","+str(department)+","+str(gender)+","+str(course_name)+")"
    conn.execute(cmd)
    conn.commit()
    conn.close()


roll_no = input('enter the roll no: ')
name = input('Enter the name: ')
course_name = input("Enter Course name(B.E/B.sc..):")
department = input("Enter the department:")
gender = input("enter the gender:")
InsertndUpdate(roll_no,name,department,gender,course_name)


i = 0  

while 1:
    ret, img = cam.read()
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face = detector.detectMultiScale(gray_img, 1.3, 5)

    for (x,y,w,h) in face:
        cv2.rectangle( img, (x,y), (x+w,y+h), (255,255,0), 1)
        cv2.imwrite("face_data/students."+roll_no+'.'+str(i)+".jpg",gray_img[y:y+h,x:x+w])
        i += 1
        cv2.imshow('Data Creator',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    elif i>100:
        break

cam.release()
cam.destroyAllWindows()