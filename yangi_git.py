import os
os.system("cls")

class car:
    def __init__(self, Name: str, color: str, ishlab_chiqilgan_Yili: int):
        self.name = Name
        self.colocr = color
        self.ishlab = ishlab_chiqilgan_Yili
        pass
    def Car_Name(self):
        return f"Car_Name -> {self.name}"
    def Car_Color(self):
        return f"Car_Color -> {self.colocr}"
    def Car_ishlabchiqilgan_Yili(self):
        return f"Car_Ishlab_Chiqilgan_Yili -> {self.ishlab}"
lamborgini = car(Name="Lambargini Aventador", color="Black",ishlab_chiqilgan_Yili=1991)
ferrari = car(Name="Ferrari alambalo",color="Red",ishlab_chiqilgan_Yili=1582)
print(ferrari.Car_Name())
print(ferrari.Car_Color())
print(lamborgini.Car_ishlabchiqilgan_Yili())
print(lamborgini.Car_Name())
print(lamborgini.Car_Color())
print(lamborgini.Car_ishlabchiqilgan_Yili())