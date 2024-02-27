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
            return f"""
            Compyuter nomi -> {self.kompnomi}
            Comyuter Tezkor hotirasi -> {self.ozu}
            Compyuter Ekrani suratlari yangilanish tezligi yani (FPS) -> {self.kadrlar_soni}
            Compyuter ishlab chiqarilgan yili -> {self.ishlab_ch_yili}"
            Copyuter rangi -> {self.rangi}
            Monitor olchami -> {self.monitor}
            Compyuter narxi -> {self.narxi}
            Compyuter mishkasi turi -> {self.mishka_n_}
            Compyuter klaviaturasi RGBsi bormi -> {self.rgb}"""
            

logitech = Computer(int(input("Ozu olchami ->")),input("Monitor o'lchamini kiriting -> "), int(input("Kadrlar sonini kiriting -> ")), input("Compyuter nomini kiriting -> "), int(input("Compyuter ishlab chiqarilgan yili ->")), int(input("Compyuter Narxini kiriting -> ")), input("Mishka markasini kiriting -> "),bool(input("Klaviatura RGB bormi yoqmi, bolsa True. yoq bolsa False ->")),int(input("HDD olchamini kiriting -> ")),input("Compyuter rangini kiriting ->"))
print(logitech.komp_info())