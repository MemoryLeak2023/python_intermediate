class Dier:
    #def __str__(self):
      #return 'Dit is de door Sandra bedachte klasse: Dier'  


    def geluid(self):
        print("Het dier maakt een geluid")

class Hond(Dier):
    def geluid(self):
        print("Woef!")

class Kat(Dier):
    def geluid(self):
        print("Miauw")

class Puppy(Hond):
    def geluid(self):
        super().geluid()
        print("...maar dan schattiger!")

d = Dier()
h = Hond()
k = Kat()
p = Puppy()

d.geluid()  # → Het dier maakt een geluid.
h.geluid()  # → Woef!
k.geluid()  # → Miauw!
p.geluid()  # → Woef! \n ...maar dan met een schattig piepje 🐶

print(k)