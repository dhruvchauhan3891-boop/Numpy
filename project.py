# class programmer:
#     company = "microsoft"
#     def __init__(self, name, salary, pincode):
#         self.name = name
#         self.salary = salary
#         self.pincode = pincode
        
# p = programmer("dhruv",  100000, 382415)
# print(p.name, p.salary, p.pincode, p.company)
# r = programmer("rajesh",  100000, 382415)
# print(r.name, r.salary, r.pincode, r.company)


# class calculator:
#     def __init__(self, n):
#         self.n = n
        
#     def square(self):
#         print(f"the square is {self.n*self.n}")
        
#     def cube(self):
#         print(f"the cube is {self.n*self.n*self.n}")
        
#     def squareroot(self):
#         print(f"the squareroot is {self.n**1/2}")
        
#     @staticmethod
#     def hello():
#         print("hello dhruv!!")
            
# a = calculator(4)
# a.hello()
# a.square()
# a.cube()
# a.squareroot()


# class demo:
#     a = 4
    
# o = demo()
# print(o.a)
# o.a = 0
# print(o.a)



class train:
    def book(self):
        pass      
    def getstatus(self, trainno):
        pass
    def getfare(self, trainno, fro, to):
        pass