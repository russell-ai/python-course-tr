#%% class-instance (sınıf-nesne) oluşturma:
# class Daire:
#     pi = 3.14
#
#     def __init__(self,r):
#         self.cap = r
#
#     def area(self):
#         return self.pi * self.cap ** 2
#
#     def around(self):
#         return 2 * self.pi * self.cap
#
# d1 = Daire(3)
# d2 = Daire(4)
# print(Daire.pi)
# print(d1.area())
# print(d2.around())

#
# class Car:
#
#     def __init__(self, marka, model):
#         print("Car constructer...")
#         self.marka = marka
#         self.model = model
#
#     def run(self):
#         print("motor çalıştı...")
#
#     def stop(self):
#         print("motor durdu...")
#
# c1 = Car("toyota","auris")
# print(c1.marka, c1.model)
# c1.run()
# c1.stop()

#%% inheritence ve overriding
#
# class Motorbike(Car):
#
#     def __init__(self, marka, model, cc):
#         print("Motorbike nesnesi.")
#         super().__init__(marka,model)
#         self.cc = cc
#
#     def run(self):
#         print("Kontak çevir..")
#         super().run()
#
# m1 = Motorbike("honda","scooter",150)
# print(m1.marka, m1.model, m1.cc)
# m1.run()

#%% Encapsulation - Gizlilik

# class Person:
#
#     def __init__(self,id,name,age):
#         self.id = id
#         self._name = name
#         self.__age = age
#         self.__password = "python"
#
#     def getAge(self):
#         return self.__age
#
#     def setAge(self,newAge):
#         if self.__password == input("şifre:"):
#             self.__age = newAge

# %% str ve repr metodları
#
# class Person:
#
#     def __init__(self,id,name,age):
#         self.id = id
#         self._name = name
#         self.__age = age
#         self.__password = "python"
#
#     def getAge(self):
#         return self.__age
#
#     def setAge(self,newAge):
#         if self.__password == input("şifre:"):
#             self.__age = newAge
#
#     def __str__(self):
#         return f"id:{self.id} name:{self._name} age:{self.__age}"
#
#     def __repr__(self):
#         return f"{self.id} {self._name} {self.__age}"
#
#
# p1 = Person(1,"Hakan",18)
# print(p1)
# # print(str(p1))
# # print(repr(p1))
# p1.setAge(23)
# print(p1.getAge())
