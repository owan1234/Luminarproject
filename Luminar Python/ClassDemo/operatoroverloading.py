class Book:
    def __init__(self,pages):
        self.pages=pages
    def __add__(self, other):
        return Book(self.pages+other.pages)
    def __sub__(self,other):
        return (self.pages-other.pages)
    def __str__(self):
        return str(self.pages)

    
ob=Book(100)
ob2=Book(200)
obj=Book(300)
print(ob+ob2+obj)
print(ob)