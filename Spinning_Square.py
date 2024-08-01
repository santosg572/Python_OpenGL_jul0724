from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

spinning = True;

FPS = 60;

currentAngleOfRotation = 0.0;

def reshape(w, h):
  glViewport(0, 0, w, h);
  aspect = w / h;
  glMatrixMode(GL_PROJECTION);
  glLoadIdentity();
  if w <= h: 
    glOrtho(-50.0, 50.0, -50.0/aspect, 50.0/aspect, -1.0, 1.0);
  else:
    glOrtho(-50.0*aspect, 50.0*aspect, -50.0, 50.0, -1.0, 1.0);
  


def display():
  glClear(GL_COLOR_BUFFER_BIT);
  glMatrixMode(GL_MODELVIEW);
  glLoadIdentity();
  glRotatef(currentAngleOfRotation, 0.0, 0.0, 1.0);
  glRectf(-25.0, -25.0, 25.0, 25.0);
  glFlush();
  glutSwapBuffers();


def timer(v):
  if spinning:
    currentAngleOfRotation += 1.0;
    if currentAngleOfRotation > 360.0:
      currentAngleOfRotation -= 360.0;
   
    glutPostRedisplay();
  
  glutTimerFunc(1000/FPS, timer, v);


def mouse(button, state, x, y):
  if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
    spinning = TRUE;
  elif button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
    spinning = FALSE;

glutInit();
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB);
glutInitWindowPosition(80, 80);
glutInitWindowSize(800, 500);
glutCreateWindow("Spinning Square");
glutReshapeFunc(reshape);
glutDisplayFunc(display);
glutTimerFunc(100, timer, 0);
glutMouseFunc(mouse);
glutMainLoop();
