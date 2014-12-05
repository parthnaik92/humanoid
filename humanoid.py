#201001185-Parth Naik
import sys
import math
import Image
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

TORSO_RADIUS=0.1
TORSO_HEIGHT=0.4

HEAD_RADIUS = 0.1

UPPER_ARM_HEIGHT=0.2
UPPER_ARM_WIDTH=0.07

LOWER_ARM_HEIGHT=0.2
LOWER_ARM_WIDTH=0.05

UPPER_LEG_HEIGHT=0.2
UPPER_LEG_WIDTH=0.08

LOWER_LEG_HEIGHT=0.2
LOWER_LEG_WIDTH=0.06

SHOLDER_WIDTH = 0.2
HIP_WIDTH = 0.2

HEADX=0.1
HEADY=TORSO_HEIGHT

LUAX=-1.0 * SHOLDER_WIDTH / 2
RUAX=SHOLDER_WIDTH / 2
LUAY=RUAY=TORSO_HEIGHT
LLAY=RLAY=LOWER_ARM_HEIGHT

LULX=-1.0 * HIP_WIDTH / 2
RULX=HIP_WIDTH / 2
LULY=RULY=0
LLLY=RLLY=LOWER_LEG_HEIGHT

t0=0.0
t1=0.0
t2=0.0
t3=90.0
t4=0.0
t5=90.0
t6=0.0
t7=180.0
t8=0.0
t9=180.0
t10=0.0

def display():
  glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
  
  glMatrixMode(GL_PROJECTION)
  glLoadIdentity()
  
  # set camera FOV=20 degree, aspect=1.0, near=1.0(0.0 will cause error), far=100.9
  gluPerspective(20, 1.0, 1.0, 100.0)
  
  glMatrixMode(GL_MODELVIEW)
  glLoadIdentity()
  # Place camera at (2,2,2), to direction (0, 0.2, 0), rotation around Z axis 0 degree(up Y)
  gluLookAt(2.0, 2.0, 2.0, 0.0, 0.2, 0.0, 0.0, 1.0, 0.0)

  #TORSO
  glEnable(GL_TEXTURE_2D)
  materials(brass_amb, brass_diff, brass_spec, brass_shin)
  glRotatef(t0, 0.0, 1.0, 0.0)
  torso()
  glPushMatrix()

  #HEAD
  #cyan()
  glTranslatef(0.0, HEADX, 0.0)
  glRotatef(1.0, 1.0, t1, 0.0)
  glRotatef(t2, 0.0, 1.0, 0.0)
  glTranslatef(0.0, HEADY, 0.0)
  head()

  #nose
  #yellow()
  glTranslatef(0.0, 0.0, HEAD_RADIUS)
  nose()

  #eyes
  magenta()
  glTranslatef(HEAD_RADIUS/2, HEAD_RADIUS/2, 0.0)
  nose()

  glTranslatef(-HEAD_RADIUS, 0.0, 0.0)
  nose()
  
  #LEFT UPPER ARM
  glEnable(GL_TEXTURE_2D)
  glPopMatrix()
  glPushMatrix()
  red()
  glTranslatef(LUAX, LUAY, 0.0)
  glRotatef(t3, 1.0, 0.0, 0.0)
  upper_arm()

  #LEFT LOWER ARM
  materials(brass_amb, brass_diff, brass_spec, brass_shin)
  green()
  glTranslatef(0.0, LLAY, 0.0)
  glRotatef(t4, 1.0, 0.0, 0.0)
  lower_arm()

  #RIGHT UPPER ARM
  materials(brass_amb, brass_diff, brass_spec, brass_shin)
  glPopMatrix()
  glPushMatrix()
  blue()
  glTranslatef(RUAX, RUAY, 0.0)
  glRotatef(t5, 1.0, 0.0, 0.0)
  upper_arm()

  #RIGHT UPPER ARM
  cyan()
  glTranslatef(0.0, RLAY, 0.0)
  glRotatef(t6, 1.0, 0.0, 0.0)
  lower_arm()

  #LEFT UPPER LEG
  glPopMatrix()
  glPushMatrix()
  magenta()
  glTranslatef(LULX, LULY, 0.0)
  glRotatef(t7, 1.0, 0.0, 0.0)
  upper_leg()

  #LEFT LOWER LEG
  yellow()
  glTranslatef(0.0, LLLY, 0.0)
  glRotatef(t8, 1.0, 0.0, 0.0)
  lower_leg()

  #RIGHT UPPER LEG
  glPopMatrix()
  glPushMatrix()
  pink()
  glTranslatef(RULX, RULY, 0.0)
  glRotatef(t9, 1.0, 0.0, 0.0)
  upper_leg()

  #RIGHT LOWER LEG
  gray()
  glTranslatef(0.0, RLLY, 0.0)
  glRotatef(t10, 1.0, 0.0, 0.0)
  lower_leg()

  glPopMatrix()
  #glutSwapBuffers()
  glFlush()

def torso():
  glPushMatrix()
  glRotatef(-90.0, 1.0, 0.0, 0.0)
  gluCylinder(p, TORSO_RADIUS, TORSO_RADIUS, TORSO_HEIGHT, 10, 10)
  glPopMatrix()

def head():
  glPushMatrix()
  glRotatef(-90.0, 1.0, 0.0, 0.0)
  glutSolidSphere(HEAD_RADIUS, 10, 10)
  glPopMatrix()
  
def upper_arm():
  glPushMatrix()
  glTranslatef(0.0, 0.5*UPPER_ARM_HEIGHT, 0.0)
  glScalef(UPPER_ARM_WIDTH, UPPER_ARM_HEIGHT, UPPER_ARM_WIDTH)
  glutSolidCube(1.0)
  glPopMatrix()

def lower_arm():
  glPushMatrix()
  glTranslatef(0.0, 0.5*UPPER_ARM_HEIGHT, 0.0)
  glScalef(LOWER_ARM_WIDTH, LOWER_ARM_HEIGHT, LOWER_ARM_WIDTH)
  glutSolidCube(1.0)
  glPopMatrix()

def upper_leg():
  glPushMatrix()
  glTranslatef(0.0, 0.5*LOWER_ARM_HEIGHT, 0.0)
  glScalef(UPPER_LEG_WIDTH, UPPER_LEG_HEIGHT, UPPER_LEG_WIDTH)
  glutSolidCube(1.0)
  glPopMatrix()

def lower_leg():
  glPushMatrix()
  glTranslatef(0.0, 0.5*LOWER_ARM_HEIGHT, 0.0)
  glScalef(LOWER_LEG_WIDTH, LOWER_LEG_HEIGHT, LOWER_LEG_WIDTH)
  glutSolidCube(1.0)
  glPopMatrix()

def nose():
  glPushMatrix()
  glRotatef(-90.0, 1.0, 0.0, 0.0)
  glutSolidSphere(HEAD_RADIUS/5, 10, 10)
  glPopMatrix() 
  
def red():
  glColor3f(1.0, 0.0, 0.0)
def green():
  glColor3f(0.0, 1.0, 0.0)
def blue():
  glColor3f(0.0, 0.0, 1.0)
def cyan():
  glColor3f(0.0, 1.0, 1.0)
def magenta():
  glColor3f(1.0, 1.0, 0.0)
def yellow():
  glColor3f(1.0, 0.0, 1.0)
def pink():
  glColor3f(1.0, 0.5, 0.5)
def gray():
  glColor3f(0.7, 0.7, 0.7)
  
def mykey(key, x, y):
  global t0, t1, t2, t3, t4, t5, t6, t7, t8, t9, t10
  if key=='d': # TORSO
    t0 = t0 + 10.0
  elif key=='D':
    t0 = t0 - 10.0
  elif key=='e': # HEAD 1
    t1 = t1 + 10.0
  elif key=='E':
    t1 = t1 - 10.0
  elif key=='r': # HEAD 2
    t2 = t2 + 10.0
  elif key=='R':
    t2 = t2 - 10.0
  elif key=='s': # LUA
    t3 = t3 + 10.0
  elif key=='S':
    t3 = t3 - 10.0
  elif key=='a': # LLA
    t4 = t4 + 10.0
  elif key=='A':
    t4 = t4 - 10.0
  elif key=='f': # RUA
    t5 = t5 + 10.0
  elif key=='F':
    t5 = t5 - 10.0
  elif key=='g': # RLA
    t6 = t6 + 10.0
  elif key=='G':
    t6 = t6 -10.0
  elif key=='x': # LUL
    t7 = t7 + 10.0
  elif key=='X':
    t7 = t7 - 10.0
  elif key=='z': # LLL
    t8 = t8 + 10.0
  elif key=='Z':
    t8 = t8 -10.0
  elif key=='c': # RUL
    t9 = t9 + 10.0
  elif key=='C':
    t9 = t9 - 10.0
  elif key=='v': # RLL
    t10 = t10 + 10.0
  elif key=='V':
    t10 = t10 - 10.0
  elif key=='q':
    sys.exit()
  elif key=='Q':
    sys.exit()

  print ("params: "), t0, t1, t2, t3, t4, t5, t6, t7, t8, t9, t10
  glutPostRedisplay()

def materials(amb, diff, spec, shin):
  glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, amb)
  glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, diff)
  glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, spec)
  glMaterialfv(GL_FRONT_AND_BACK, GL_SHININESS, shin)
  
glutInit( sys.argv )
#glutInitDisplayMode( GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH )
glutInitDisplayMode( GLUT_RGBA | GLUT_SINGLE | GLUT_DEPTH )
glutInitWindowSize( 500, 500 )
glutInitWindowPosition(0,0)
glutCreateWindow( 'Humanoid' )
glutDisplayFunc( display )
glutKeyboardFunc(mykey)

glEnable(GL_DEPTH_TEST) #hidden-usrface removal
glEnable(GL_CULL_FACE) #don't draw back side surface
glCullFace(GL_BACK) #don't draw back side surface

### TEXTURE
glEnable(GL_TEXTURE_2D)
# generate continuous one texture
# different format from C, void glGenTexture(n, *name)
texture=glGenTextures(1)

# use the generated texture
glBindTexture(GL_TEXTURE_2D, texture)

# read texture data from .bmp file ising Image library
image=Image.open("texture.jpg")
if len(image.getbands())!=4:
  image=image.convert("RGBA")
size=image.size

# generate texture from array image.tostring() inside current texture 'texture'
glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, size[0], size[1], 0, GL_RGBA, GL_UNSIGNED_BYTE, image.tostring())

# set texture options, repeat same pattern
glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)

# set texture options, enlarge and shrink
glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)

# set texture options, slow but good image
glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)

# enable auto generation of texture coordinate in s and t direction
glEnable(GL_TEXTURE_GEN_S)
glEnable(GL_TEXTURE_GEN_T)

# setup OBJECT_LINEAR ot EYE_LINEAR for auto texture coord generation
#glTexGeni(GL_S, GL_TEXTURE_GEN_MODE, GL_OBJECT_LINEAR)
#glTexGeni(GL_T, GL_TEXTURE_GEN_MODE, GL_OBJECT_LINEAR)
glTexGeni(GL_S, GL_TEXTURE_GEN_MODE, GL_EYE_LINEAR)
glTexGeni(GL_T, GL_TEXTURE_GEN_MODE, GL_EYE_LINEAR)

# Not successfull yet
#planes = 0.5, 0.0, 0.0, 0.5
#planet = 0.0, 0.5, 0.0, 0.5
#glTexGenfv(GL_S, GL_OBJECT_LINEAR, planes)
#glTexGenfv(GL_T, GL_OBJECT_LINEAR, planet)

### Lighting
glEnable(GL_LIGHTING) #use lighting
glEnable(GL_LIGHT0) #use a light 0
glEnable(GL_LIGHT1) #use a light 1

# light 0
light0_pos = 10.0, 10.0, 10.0, 0.0
diffuse0 = 0.5, 0.5, 0.5, 1.0
specular0 = 0.5, 0.5, 0.5, 1.0
ambient0 = 0.8, 0.8, 0.8, 1.0

glMatrixMode(GL_MODELVIEW)
glLightfv(GL_LIGHT0, GL_POSITION, light0_pos)
glLightfv(GL_LIGHT0, GL_DIFFUSE, diffuse0)
glLightfv(GL_LIGHT0, GL_SPECULAR, specular0)
glLightfv(GL_LIGHT0, GL_AMBIENT, ambient0)

# light 1
light1_pos = 0.0, 0.0, 10.0, 0.0
diffuse1 = 0.8, 0.8, 0.8, 1.0
specular1 = 0.2, 0.2, 0.2, 1.0
ambient1 = 0.2, 0.2, 0.2, 1.0

glLightfv(GL_LIGHT1, GL_POSITION, light1_pos)
glLightfv(GL_LIGHT1, GL_DIFFUSE, diffuse1)
glLightfv(GL_LIGHT1, GL_SPECULAR, specular1)
glLightfv(GL_LIGHT1, GL_AMBIENT, ambient1)

# Material
brass_amb = 0.83, 0.02, 0.03, 1.0
brass_diff = 0.12, 0.69, 0.11, 1.0
brass_spec = 0.99, 0.91, 0.81, 1.0
brass_shin = 20.0

p_amb = 0.3, 0.0, 0.0, 1.0
p_diff = 0.6, 0.0, 0.0, 1.0
p_spec = 0.8, 0.6, 0.6, 1.0
p_shin = 32.8

# create new Quadric 'p' for gluCylinder and set texture for it
p=gluNewQuadric()
gluQuadricDrawStyle(p, GLU_FILL)
gluQuadricNormals(p, GLU_SMOOTH)
#gluQuadricTexture(p, GL_TRUE)

glutMainLoop()

