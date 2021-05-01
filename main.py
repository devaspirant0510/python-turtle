import turtle as t
class Base:
    def __init__(self,x_pos:int,y_pos:int,width:int,height:int,color:str="green",shape:str="turtle",speed:int=10):
        self.__x_pos = x_pos
        self.__y_pos = y_pos
        self.__width = width
        self.__height = height
        self.__color = color
        self.__shape = shape
        self.__speed = speed
    def setting(self,turtle):
        turtle.color(self.__color)
        turtle.shape(self.__shape)
        turtle.speed(self.__speed)
    def init_pos(self,turtle):
        turtle.penup()
        turtle.setpos(self.x_pos,self.y_pos)
        turtle.pendown()
    #getter
    @property
    def x_pos(self)->int:
        return self.__x_pos
    @property
    def y_pos(self)->int:
        return self.__y_pos
    @property
    def width(self)->int:
        return self.__width
    @property
    def height(self)->int:
        return self.__height
    #setter
    @x_pos.setter
    def x_pos(self,x_pos)->None:
        self.__x_pos = x_pos
    @y_pos.setter
    def y_pos(self,y_pos)->None:
        self.__y_pos = y_pos
    @width.setter
    def width(self,width)->None:
        self.__width = width
    @height.setter
    def height(self,height)->None:
        self.__height = height

class Triangle(Base):
    def __init__(self,x_pos,y_pos,width,height,point=None,color="green",shape="turtle",speed=10):
        super().__init__(x_pos,y_pos,width,height,color,shape,speed)
        if point == None:
            self.__point = (x_pos+width)//2
        else:
            self.__point = point

    def setting(self,turtle):
        super().setting(turtle)

    def draw(self,turtle):
        self.setting(turtle)
        self.init_pos(turtle)
        turtle.setpos(self.x_pos+self.width,self.y_pos)
        turtle.setpos(self.point,self.height)
        turtle.setpos(self.x_pos,self.y_pos)

    @property
    def point(self)->int:
        return self.__point
    @point.setter
    def point(self,point):
        self.__point = point

class Circle(Base):
    def __init__(self,x_pos,y_pos,width,height,step=None,color="green",shape="turtle",speed=10):
        super().__init__(x_pos,y_pos,width,height,color,shape,speed)
        self.__step = step

    def setting(self,turtle):
        super().setting(turtle)

    def draw(self,turtle):
        self.setting(turtle)
        self.init_pos(turtle)
        turtle.circle(self.width,steps=self.step)
    #getter
    @property
    def step(self)->int:
        return self.__step
    @step.setter
    def step(self,step):
        self.__step = step
        
class Rectangle(Base):
    def __init__(self,x_pos,y_pos,width,height,color="green",shape="turtle",speed=10):
        super().__init__(x_pos,y_pos,width,height,color,shape,speed)

    def setting(self,turtle):
        super().setting(turtle)
        
    def draw(self,turtle):
        self.setting(turtle)
        self.init_pos(turtle)
        turtle.setpos(self.width,self.y_pos)
        turtle.setpos(self.width,self.y_pos+self.height)
        turtle.setpos(self.x_pos,self.y_pos+self.height)
        turtle.setpos(self.x_pos,self.y_pos)
r = Rectangle(0,0,30,40,speed=3)
r.draw(t.Turtle())
r1 = Rectangle(40,30,30,40,speed=3,color="red")
r1.draw(t.Turtle())
r2 = Circle(30,-60,60,10,speed=5,step=6)
r2.draw(t.Turtle())
r2 = Circle(30,-60,50,5,speed=5)
r2.draw(t.Turtle())
r3 = Triangle(-20,-20,30,40,color="red")
r3.draw(t.Turtle())
t.done()