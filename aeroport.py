import time

class Airport:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.planes = []
        self.flights = []
        self.employees = []
    def abot_airport(self):
        print(f"""
Airport nomi: {self.name}
Airport joylashuvi: {self.location}
Samalyotlar soni: {len(self.planes)}
Ishchilar soni: {len(self.employees)}""")

class salamyot:
    orindiqhisob = 0
    def __init__(self,turi,bakxajmi,uchish,qonish,orindiqlarsoni:int,yoqilgi=100,uchuvchi=False) -> None:
        self.turi = turi
        self.bak_xajmi = bakxajmi
        self.uchish_shaxri = uchish
        self.qonish_shaxri = qonish
        self.orindiqlar = orindiqlarsoni
        self.yoqilgi = yoqilgi
        self.uchuvchi = uchuvchi
        salamyot.orindiqhisob += 1
    def about_plane(self):
        print(f"""
Samalyot turi: {self.turi}
Uchish shaxri: {self.uchish_shaxri}
Qonish shaxri: {self.qonish_shaxri}
Samalyot xajmi: {self.orindiqlar} kishi
""")

class uchuvchi:
    def __init__(self, ismi, yoshi) -> None:
        self.ismi = ismi
        self.yoshi = yoshi

    def launch_airplane(self, samalyot:salamyot, masofa:int, boshqaruv):
        if boshqaruv.check_airplane(samalyot, masofa):
            samalyot.uchuvchi = True
            print(f"{samalyot.turi} Yo'lga chiqdi !")
            time.sleep(5)
            print(f"{samalyot.turi} Aytilgan manzilga yetib keldi !")
        else:
            print(f"{samalyot.turi} uchishga tayyor emas!")

class boshqaruv:
    def __init__(self, ism, airport:Airport) -> None:
        self.ism = ism
        self.airport = airport

    def add_plane(self, plane):
        self.airport.planes.append(plane)

    def remove_plane(self, plane):
        self.airport.planes.remove(plane)

    def add_employe(self, pilot):
        self.airport.employees.append(pilot)
    
    def remove_employe(self, pilot):
        self.airport.employees.remove(pilot)

    def check_airplane(self, tekshiruv:salamyot, masofa:int):
        if tekshiruv.uchuvchi == False:
            if tekshiruv.yoqilgi >= masofa:
                return True
            else:
                print("Yoqilg'i yetarli emas !")
                return False
        else:
            print("Uchuvchi boshqa yo'nalishga biriktirilgan")
            return False

    def fill_up(self, tekshiruv:salamyot):
        tekshiruv.yoqilgi = tekshiruv.bak_xajmi
        print("Yoqilg'i to'ldirildi!")


class yolovchi:
    def __init__(self, ismi, yoshi, yashashmanzil, uchish, pul:int) -> None:
        self.ismi = ismi
        self.yoshi = yoshi
        self.yashash_manzili = yashashmanzil
        self.uchish_shaxri = uchish
        self.puli = pul

    def book_flight(self, boshqaruv):
        mavjud_samolyotlar = [plane for plane in boshqaruv.airport.planes if plane.uchish_shaxri == self.yashash_manzili and plane.qonish_shaxri == self.uchish_shaxri and plane.orindiqlar > 0]
        
        if not mavjud_samolyotlar:
            print("Kechirasiz siz tanlagan davlatga uchuvchi samalyotlar mavjud emas")
            return
        
        print("Mavjud samalyotlar:")
        for i, plane in enumerate(mavjud_samolyotlar):
            print(f"{i+1}. {plane.turi}")
        
        samalyot_raqami = int(input("Qaysi raqam ostidagi samalyotda uchmoqchisiz: ")) - 1
        if samalyot_raqami < 0 or samalyot_raqami >= len(mavjud_samolyotlar):
            print("Mavjud bo'lmagan raqam !")
            return
        
        tanlangan_samalyot = mavjud_samolyotlar[samalyot_raqami]
        tanlangan_samalyot.orindiqlar -= 1
        print(f"Siz muofiqiyatli ro'yxatdan o'tdingiz ! \n")
        tanlangan_samalyot.about_plane()


