import numpy as np
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def display():
  glClear(GL_COLOR_BUFFER_BIT);

  glColor3f(1.0, 1.0, 1.0);
  glBegin(GL_LINES);

  for i in np.arange(-2.5, 2.5,0.25):
    glVertex3f(i, 0, 2.5); glVertex3f(i, 0, -2.5);
    glVertex3f(2.5, 0, i); glVertex3f(-2.5, 0, i);

  glEnd();

  glBegin(GL_TRIANGLE_STRIP);
  glColor3f(1, 1, 1); glVertex3f(0, 2, 0);
  glColor3f(1, 0, 0); glVertex3f(-1, 0, 1);
  glColor3f(0, 1, 0); glVertex3f(1, 0, 1);
  glColor3f(0, 0, 1); glVertex3f(0, 0, -1.4);
  glColor3f(1, 1, 1); glVertex3f(0, 2, 0);
  glColor3f(1, 0, 0); glVertex3f(-1, 0, 1);
  glEnd();

  glFlush();

def init():

  glClearColor(0.1, 0.39, 0.88, 1.0);
  glColor3f(1.0, 1.0, 1.0);

  glEnable(GL_CULL_FACE);
  glCullFace(GL_BACK);

  glMatrixMode(GL_PROJECTION);
  glLoadIdentity();
  glFrustum(-2, 2, -1.5, 1.5, 1, 40);

  glMatrixMode(GL_MODELVIEW);
  glLoadIdentity();
  glTranslatef(0, 0, -3);
  glRotatef(50, 1, 0, 0);
  glRotatef(70, 0, 1, 0);

glutInit();
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);
glutInitWindowPosition(80, 80);
glutInitWindowSize(800, 600);
glutCreateWindow("A Simple Tetrahedron");
glutDisplayFunc(display);
init();
glutMainLoop();

