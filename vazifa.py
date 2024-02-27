import os
os.system("cls")

class Computer:
    def __init__(self,ozu: int, monitor_olchami: str, kadrlar_soni: int, komp_nomi: int, ishlab_ch_yili: int, narxi: int, mishka_n_: str, rgb: bool, hdd: int, rangi: str):
        self.ozu = ozu
        self.monitor = monitor_olchami
        self.kadrlar_soni = kadrlar_soni
        self.kompnomi = komp_nomi
        self.ishlab_ch_yili = ishlab_ch_yili
        self.narxi = narxi
        self.mishka_n_ = mishka_n_
        self.rgb = rgb
        self.hdd = hdd
        self.rangi = rangi
    def komp_info(self):
        if self.kompnomi == str:
            print(f"Compyuter nomi -> {self.kompnomi}")
        elif self.ozu == int:
            print(f"Comyuter Tezkor hotirasi -> {self.ozu}")
        elif self.kadrlar_soni == int:
            print(f"Compyuter Ekrani suratlari yangilanish tezligi yani (FPS) -> {self.kadrlar_soni}")
        elif self.ishlab_ch_yili == int:
            print(f"Compyuter ishlab chiqarilgan yili -> {self.ishlab_ch_yili}")
        elif self.rangi == str:
            print(f"Copyuter rangi -> {self.rangi}")
        elif self.monitor == str:
            print(f"Monitor olchami -> {self.monitor}")
        elif self.narxi == int:
            print(f"Compyuter narxi -> {self.narxi}")
    def qoshimcha_narsalar(self):
        if self.mishka_n_ == str:
            print(f"Compyuter mishkasi turi -> {self.mishka_n_}")
        elif self.rgb == bool:
            print(f"Compyuter klaviaturasi RGBsi bormi -> {self.rgb}")

logitech = Computer(int(input("Ozu olchami ->")),input("Monitor o'lchamini kiriting -> "), int(input("Kadrlar sonini kiriting -> ")), input("Compyuter nomini kiriting -> "), int(input("Compyuter ishlab chiqarilgan yili ->")), int(input("Compyuter Narxini kiriting -> ")), input("Mishka markasini kiriting -> "),bool(input("Klaviatura RGB bormi yoqmi, bolsa True. yoq bolsa False ->")),int(input("HDD olchamini kiriting -> ")),input("Compyuter rangini kiriting ->"))