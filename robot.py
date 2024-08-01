from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import serial

class program:
 def __init__(self):

    self.name = "Arm"
    self.X = 0.0
    self.Y = 0.0
    self.Z = 0.0
    self.scale = 1.0
    self.wrist_angle = 0.0
    self.finger_angle = 0.0
    #self.axis_spin = [0, 0, 0]


 def run(self):
    self.Z = 5.0
    glShadeModel(GL_FLAT)
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(700, 700)
    glutCreateWindow(self.name)
    self.init()
    glutDisplayFunc(self.display)
    glutReshapeFunc(self.reshape)
    glutKeyboardFunc(self.keyboard)
    glutMainLoop()


 def reshape(self, w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(50.0, w / h, 1.0, 10.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslatef(0.0, 0.0, -6.0)

 def init(self):
    glEnable(GL_DEPTH_TEST)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(50.0, 1.0, 1.0, 10.0)
    glMatrixMode(GL_MODELVIEW)
    gluLookAt(self.X, self.Y, 5.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)




 def arm(self):
    glPushMatrix();

    glTranslatef(-1.2, 0, 0);

    glColor3f(1, 0, 1);
    glTranslatef(0.6, -0.05, 0);
    glPushMatrix();
    glScalef(1, 0.3, 0.6);
    glutWireCube(1);

    glPopMatrix();

    glTranslatef(0.65, 0.05, 0.0);
    glRotatef(self.wrist_angle, 0, 0, 1);
    glPushMatrix();
    glScalef(0.1, 0.1, 0.2);
    glutWireSphere(1, 10, 10);
    glPopMatrix();

    #= == > finger
    glColor3f(0.65, 0.05, 0.0);
    glTranslatef(0.2, 0.15, 0.15);

    glPushMatrix();
    glScalef(0.3, 0.1, 0.1);

    glutWireCube(1);
    glTranslatef(0, 0.05, -1.8);
    glutWireCube(1);
    glTranslatef(0, 0.05, -1.8);
    glutWireCube(1);
    glTranslatef(-0.3, -3.1, 1.75);
    glutWireCube(1);

    glPopMatrix();

    glPushMatrix();


    glTranslatef(0.17, 0, 0);
    glRotatef(self.wrist_angle , 0, 0, 1);    ########
    glTranslatef(0.17, 0, 0);

    glScalef(0.3, 0.1, 0.1);
    glutWireCube(1);

    glTranslatef(0, 0.05, -1.8);
    glutWireCube(1);
    glTranslatef(0, 0.05, -1.8);
    glutWireCube(1);

    glPopMatrix();

    glPushMatrix();

    glTranslatef(0.1, -0.15, -0.1);
    glRotatef(self.finger_angle, 0, 0, 1);
    glTranslatef(0.1, -0.15, -0.1);

    glScalef(0.3, 0.1, 0.1);
    glutWireCube(1);

    glPopMatrix();

    glPopMatrix();


 def display(self):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluLookAt(self.X, self.Y, self.Z, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
    self.arm()
    glutPostRedisplay()
    glutSwapBuffers()



class serialpy:
 '''def __init__(self):
    self.arduino = serial.Serial('/dev/ttyACM0', 9600, timeout=1)

  data = self.arduino.readline()[:-2]'''



if __name__ == '__main__':
 app = program()
 app.run()


