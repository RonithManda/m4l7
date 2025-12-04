class vehicle:
    def __init__(self,name,vmax,mileage):
        self.name=name
        self.vmax=vmax
        self.mileage=mileage
obj=vehicle("Audi",180,600)
print("vehicle one")
print("name:",obj.name)
print("top speed:",obj.vmax)
print("range:",obj.mileage)

obj2=vehicle("Mustang",300,300)
print("vehicle 2")
print("name:",obj2.name)
print("top speed:",obj2.vmax)
print("range:",obj2.mileage)