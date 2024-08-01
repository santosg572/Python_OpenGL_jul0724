from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class Point :
  x=0
  y=0
  def __init__(self, x = 0, y = 0): 
    self.x = 0
    self.y = 0 
  def midpoint(self, p):
     self.x = (self.x + p.x) / 2.0
     self.y = (self.y + p.y) / 2.0


def display():

  glClear(GL_COLOR_BUFFER_BIT);

  static Point vertices[] = {Point(0, 0), Point(200, 500), Point(500, 0)};

  static Point p = vertices[0];
  glBegin(GL_POINTS);
  for k = range(100000):
    p = p.midpoint(vertices[rand() % 3]);
    glVertex2f(p.x, p.y);
 
  glEnd();
  glFlush();


def init():

  glClearColor(0.25, 0.0, 0.2, 1.0);
  glColor3f(0.6, 1.0, 0.0);

  glMatrixMode(GL_PROJECTION);
  glLoadIdentity();
  glOrtho(0.0, 500.0, 0.0, 500.0, 0.0, 1.0);

glutInit();
glutInitDisplayMode (GLUT_SINGLE | GLUT_RGB);
glutInitWindowSize(500, 500);
glutInitWindowPosition(40, 40);
glutCreateWindow("Sierpinski Triangle");
glutDisplayFunc(display);
init();
glutMainLoop();


