import numpy as np
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def display():
	glClear(GL_COLOR_BUFFER_BIT);
	glColor3f(1.0, 1.0, 1.0);
	glBegin(GL_POLYGON);
	glVertex2f(-0.5, -0.5);
	glVertex2f(-0.5, 0.5);
	glVertex2f(0.5, 0.5);
	glVertex2f(0.5, -0.5); 
	glEnd();
	glFlush();

def init():

  glClearColor(0, 0, 0, 0);

  glOrtho(-2.0, 2.0, -3.0, 3.0, -1.0, 1.0);

glutInit();
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);
glutInitWindowPosition(80, 80);
glutInitWindowSize(600, 600);
glutCreateWindow("A Simple Tetrahedron");
glutDisplayFunc(display);
init();
glutMainLoop();

