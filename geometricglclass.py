from extensoes.Dependencies import *
Global_Finder = {}


class World:
    Center = (0, 0, 0)

    def __init__(self, wsize: (0, 0, 0), quad_size=1):
        self.__wsize = wsize
        self.__quad = quad_size
        self.__quad_vector = None
        self.__matrix = None
        self.__pos = [0, 0, 0]
        self.__opos = self.__pos
        self.__gen_quad()

    def __gen_matrix(self):
        matrix = []
        for kl in range(2):
            matrix.append([])
            for z in range(self.__wsize[2]):
                for x in range(self.__wsize[0]):
                    self.__pos[0] = x
                    self.__pos[2] = z
                    self.__gen_quad()
                    matrix[-1].append(self.__quad_vector)
        self.__matrix = matrix.copy()
                
    def __gen_quad(self):
        self.__quad_vector = (0+self.__opos[0], 0+self.__opos[1], self.__quad+self.__opos[2]),\
                             (self.__quad+self.__opos[0], 0+self.__opos[1], 0+self.__opos[2]),\
                             (0+self.__opos[0], 0+self.__opos[1], 0+self.__opos[2]),\
                             (self.__quad+self.__opos[0], 0+self.__opos[1], self.__quad+self.__opos[2])

    def quad(self):
        return self.__quad_vector

    def matrix(self):
        return self.__matrix


class Ambiente:
    def __init__(self):
        


"""==================Naming========================"""


class Naming:
    NamingDict = {}

    def __init__(self, tip):
        self.tip = tip
        self.idx = 0
        self.name = self.__name_by_tip()

    def __new__(cls, tip):
        inst = super(cls.__class__, cls).__new__(cls)
        inst.__init__(tip)
        return inst.name

    def __name_by_tip(self):
        while self.__in_self_dict(self.tip):
            self.idx += 1
            self.tip = self.tip + str(f" ({self.idx})")
        self.NamingDict[self.tip] = self.idx
        return self.tip

    def __in_self_dict(self, tip_name):
        if tip_name in self.NamingDict:
            return True
        else:
            return False


"""==================Naming=End===================="""


"""==================Euler Angles========================"""


class Sin:
    def __init__(self, x):
        self.x = float("%.10f" % sin(radians(x)))

    def __new__(cls, x):
        inst = super(cls.__class__, cls).__new__(cls)
        inst.__init__(x)
        return inst.x


class Cos:
    def __init__(self, x):
        self.x = float("%.10f" % cos(radians(x)))

    def __new__(cls, x):
        inst = super(cls.__class__, cls).__new__(cls)
        inst.__init__(x)
        return inst.x


class Tan:
    def __init__(self, x):
        self.x = float("%.10f" % tan(radians(x)))

    def __new__(cls, x):
        inst = super(cls.__class__, cls).__new__(cls)
        inst.__init__(x)
        return inst.x


class ASin:
    def __init__(self, x):
        self.x = float("%.10f" % asin(radians(x)))

    def __new__(cls, x):
        inst = super(cls.__class__, cls).__new__(cls)
        inst.__init__(x)
        return inst.x


class ACos:
    def __init__(self, x):
        self.x = float("%.10f" % acos(radians(x)))

    def __new__(cls, x):
        inst = super(cls.__class__, cls).__new__(cls)
        inst.__init__(x)
        return inst.x


class ATan:
    def __init__(self, x):
        self.x = float("%.10f" % atan(radians(x)))

    def __new__(cls, x):
        inst = super(cls.__class__, cls).__new__(cls)
        inst.__init__(x)
        return inst.x


"""==================Euler Angles=End===================="""


class GObject:
    def __init__(self, tag, vpos, vaxis, geometry, name=Naming(OBJECT)):
        self.name = name
        self.tag = tag
        Global_Finder[tag] = self
        self.transform = Transform(self, vpos, vaxis)


class Transform:
    def __init__(self, this, vpos, vaxis):
        if len(vpos) == len(vaxis):
            self.position = self.__Position(this, vpos)
            self.rotation = self.__Rotation(this, vaxis)
        alert("Not Valid Transform")
        pass

    def __getattr__(self, item):
        pass

    class __Rotation:
        def __init__(self, this, vaxis):
            self.this = this
            self.ax, self.ay, self.az = vaxis

    class __Position:
        def __init__(self, this, vpos):
            self.this = this
            self.x, self.y, self.z = vpos

    class Rotate:
        class __Up:
            pass


class Geometry:
    def __init__(self):
        pass

    class Vertices:
        def __init__(self):
            self.vertex = None


"""==========================Vectors=========================================="""


class Vectors:
    def __init__(self, *args):
        self.__arg_len = len(args)
        self.__arg_tip = None
        self.__return = None
        if self.__arg_len == 1:
            self.__arg_tip = isinstance(args[0],Transform)
        elif self.__arg_len == 2:
            self.__arg_tip = type(self.Vector2)
            self.__return = self.Vector2(*args)
        elif self.__arg_len == 3:
            self.__arg_tip = type(self.Vector3)

    class Vector3:
        def __init__(self, transform):
            self.forward = self.__Forward(transform)

        class __Forward:
            def __init__(self, transform):
                self.uvec = CVector3U(transform.rotation)
                self.diretor = 0 # working..

    class Vector2:
        def __init__(self, *args):
            if len(args) == 1:
                transform = args[0]
                self.forward = self.__Forward(transform)
            elif len(args) == 2:
                self.x = args[0]
                self.y = args[1]

        class __Forward:
            def __init__(self, transform):
                self.uvec = CVector2U(transform.rotation)
                self.diretor = 0 # working..


class CVector3:
    def __init__(self, vec3):
        self.vec3 = vec3.x, vec3.y, vec3.z

    def __new__(cls, vec3):
        inst = super(cls.__class__, cls).__new__(cls)
        inst.__init__(vec3)
        return inst.vec3


class CVector2:
    def __init__(self, vec2):
        self.vec2 = vec2.x, vec2.y

    def __new__(cls, vec2):
        inst = super(cls.__class__, cls).__new__(cls)
        inst.__init__(vec2)
        return inst.vec2


class CVector3U:
    def __init__(self, vec3u):
        try:
            self.vec3u = vec3u.x/(vec3u.x**2+vec3u.y**2+vec3u.z**2)**0.5,\
                         vec3u.y/(vec3u.x**2+vec3u.y**2+vec3u.z**2)**0.5,\
                         vec3u.z/(vec3u.x**2+vec3u.y**2+vec3u.z**2)**0.5
        except ZeroDivisionError:
            self.vec3u = vec3u.x, vec3u.y, vec3u.z
        except ValueError as verr:
            alert(f'Invalid Value: {verr}')

    def __new__(cls, vec3u):
        inst = super(cls.__class__, cls).__new__(cls)
        inst.__init__(vec3u)
        return inst.vec3u


class CVector2U:
    def __init__(self, vec2u):
        try:
            self.vec2u = vec2u.x/(vec2u.x**2+vec2u.y**2+vec2u.z**2)**0.5,\
                         vec2u.y/(vec2u.x**2+vec2u.y**2+vec2u.z**2)**0.5,\
                         vec2u.z/(vec2u.x**2+vec2u.y**2+vec2u.z**2)**0.5
        except ZeroDivisionError:
            self.vec2u = vec2u.x, vec2u.y
        except ValueError as verr:
            alert(f'Invalid Value: {verr}')

    def __new__(cls, vec2u):
        inst = super(cls.__class__, cls).__new__(cls)
        inst.__init__(vec2u)
        return inst.vec2u


"""==========================Vectors=End======================================"""

# print(CVector2U(GObject('cube', (0, 0, 0), (90, 90, 60), None).transform.position))


class GeometricGLClass(QOpenGLWidget):
    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)
        self.world = World((30, 30, 30))
        self.grid = self.matrix(10)

    def initializeGL(self) -> None:
        glClearColor(0.1, 0.1, 0.1, 1)
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_LIGHT0)
        glEnable(GL_LIGHTING)
        glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
        glEnable(GL_COLOR_MATERIAL)
        pass

    def paintGL(self) -> None:
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glBegin(GL_TRIANGLES)
        glColor3f(1.0, 0.0, 0.0)
        glVertex3f(-0.5, -0.5, 0)
        glColor3f(0.0, 1.0, 0.0)
        glVertex3f(0.5, -0.5, 0)
        glColor3f(0.0, 0.0, 1.0)
        glVertex3f(0.0, 0.5, 0)
        glEnd()
        self.draw_matrix()
        glRotated(1, 1, 1, 1)

    def resizeGL(self, w: int, h: int) -> None:
        glViewport(0, 0, w, h)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(60, float(w / h), 0.01, 1000.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(0, 0, 10, 0, 0, 0, 0, 1, 0)
        pass

    def matrix(self, n):
        pos = [0, 0, 0]
        opos = pos
        quads = []
        for z in range(-n, n+1):
            for x in range(-n, n+1):
                pos[0] = x
                pos[2] = z
                quad = (1+opos[0], 0+opos[1], 0+opos[2]),\
                       (0+opos[0], 0+opos[1], 1+opos[2]),\
                       (1+opos[0], 0+opos[1], 1+opos[2]),\
                       (0+opos[0], 0+opos[1], 0+opos[2])
                quads.append(quad)
        return quads

    def draw_matrix(self):
        glColor3f(1.0, 1.0, 1.0)
        glBegin(GL_LINES)
        for quad in self.grid:
            glVertex3fv(quad[0])
            glVertex3fv(quad[1])
            glVertex3fv(quad[2])
            glVertex3fv(quad[3])
        glEnd()

    class Update:
        def __init__(self, obj):
            self.obj = obj








