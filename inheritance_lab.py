# Class induk utama
class Karakter:

    def __init__(self, nama):
        self.nama = nama

    def info(self):
        print(f"Karakter: {self.nama}")


# Class turunan dari Karakter
class Warrior(Karakter):

    def __init__(self, nama):
        super().__init__(nama)

    def skill_warrior(self):
        print(f"{self.nama} menggunakan pedang!")


# Class turunan dari Karakter
class Mage(Karakter):

    def __init__(self, nama):
        super().__init__(nama)

    def skill_mage(self):
        print(f"{self.nama} menggunakan sihir!")


# Diamond Problem:
# Battlemage mewarisi Warrior dan Mage
class Battlemage(Warrior, Mage):

    def __init__(self, nama):
        super().__init__(nama)

    def skill_ultimate(self):
        print(f"{self.nama} menggunakan kombinasi pedang dan sihir!")


# Membuat object
hero = Battlemage("Arthur")

# Menjalankan method
hero.info()
hero.skill_warrior()
hero.skill_mage()
hero.skill_ultimate()

# Melihat urutan Method Resolution Order (MRO)
print(Battlemage.__mro__)   



