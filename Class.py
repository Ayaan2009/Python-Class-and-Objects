class Building (object):

    def __init__ (self, color= "beige", shape= 'circle' , floors=15 , height=50 , width=25):
        self.color = color
        self.shape = shape
        self.floors = floors
        self.height = height
        self.width = width
    
glass = Building()
glass1 = Building("red")
glass2 = Building("green", "triangle", 30, 100, 50)
print(glass2.color, glass2.shape, glass2.floors, glass2.height, glass2.width)
#give arguments sequentially