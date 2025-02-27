import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

rotateAngle = 0.0
lightPos = [5.0, 8.0, 5.0, 1.0]
fogColor = [0.5, 0.5, 0.5, 1.0]

def makeShadowMatrix(light, plane):
    A, B, C, D = plane
    Lx, Ly, Lz, Lw = light
    dot = A * Lx + B * Ly + C * Lz + D * Lw

    shadowMat = [dot - A * Lx,  -A * Ly,  -A * Lz,  -A * Lw,
                -B * Lx,  dot - B * Ly,  -B * Lz,  -B * Lw,
                -C * Lx,  -C * Ly,  dot - C * Lz,  -C * Lw,
                -D * Lx,  -D * Ly,  -D * Lz,  dot - D * Lw]
    return shadowMat

def drawFloor():
    size = 10.0
    glBegin(GL_QUADS)
    glNormal3f(0.0, 1.0, 0.0)
    glColor3f(0.7, 0.7, 0.7)
    glVertex3f(-size, 0.0, -size)
    glVertex3f(size, 0.0, -size)
    glVertex3f(size, 0.0, size)
    glVertex3f(-size, 0.0, size)
    glEnd()

def drawObjects():
    glPushMatrix()
    glTranslatef(-2.0, 1.0, 0.0)
    glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, [1.0, 0.2, 0.2, 1.0])
    glutSolidSphere(1.0, 30, 30)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(2.0, 1.0, 0.0)
    glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, [0.2, 0.2, 1.0, 1.0])
    glutSolidCube(1.5)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.0, 1.0, 2.0)
    glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, [0.2, 1.0, 0.2, 1.0])
    glutSolidCube(1.0)
    glPopMatrix()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0.0, 5.0, 10.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
    glRotatef(rotateAngle, 0.0, 1.0, 0.0)
    glLightfv(GL_LIGHT0, GL_POSITION, lightPos)

    drawFloor()
    glEnable(GL_LIGHTING)
    drawObjects()

    floorPlane = [0.0, 1.0, 0.0, 0.0]
    shadowMat = makeShadowMatrix(lightPos, floorPlane)

    glDisable(GL_LIGHTING)
    glPushMatrix()
    glMultMatrixf(shadowMat)
    glColor3f(0.0, 0.0, 0.0)
    drawObjects()
    glPopMatrix()
    glEnable(GL_LIGHTING)

    glutSwapBuffers()

def reshape(w, h):
    if h == 0:
        h = 1
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, w / float(h), 1.0, 100.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def timer(value):
    global rotateAngle
    rotateAngle += 1.0
    if rotateAngle > 360.0:
        rotateAngle -= 360.0
    glutPostRedisplay()
    glutTimerFunc(16, timer, 0)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"OpenGL Scene with Lighting and Shadows (Python)")

    glEnable(GL_DEPTH_TEST)
    glEnable(GL_NORMALIZE)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)

    lightAmbient  = [0.2, 0.2, 0.2, 1.0]
    lightDiffuse  = [0.8, 0.8, 0.8, 1.0]
    lightSpecular = [1.0, 1.0, 1.0, 1.0]
    glLightfv(GL_LIGHT0, GL_AMBIENT,  lightAmbient)
    glLightfv(GL_LIGHT0, GL_DIFFUSE,  lightDiffuse)
    glLightfv(GL_LIGHT0, GL_SPECULAR, lightSpecular)

    glMaterialfv(GL_FRONT, GL_SPECULAR, [1.0, 1.0, 1.0, 1.0])
    glMaterialf(GL_FRONT, GL_SHININESS, 50.0)

    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE)

    glEnable(GL_FOG)
    glFogfv(GL_FOG_COLOR, fogColor)
    glFogf(GL_FOG_MODE, GL_EXP2)
    glFogf(GL_FOG_DENSITY, 0.05)
    glHint(GL_FOG_HINT, GL_NICEST)

    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutTimerFunc(0, timer, 0)

    glutMainLoop()

if __name__ == '__main__':
    main()
