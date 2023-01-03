# Sukurkite klasę "Movie", kuri gebės sukurti objektus 3 savybėm ir 1 metodu. 
# Naudojant šią klasę sukurkite bent du skirtingus objektus.

# Savybės:
# title: string
# director: string
# budget: number

# Metodas: 
# wasExpensive() - jeigu filmo "budget" yra daugiau nei 100 000 000 mln USD, tada grąžins True, kitu atveju False. 


# sukuriama klase su savybem
class Movie:
    def __init__(self, title, director, budget):
        self.title = title
        self.director = director
        self.budget = budget

# sukuriamas metodas
    def wasExpensive(self):
        film_budget = int(self.budget) # kintamasis, kuris prilyginamas self.budget (biudzeto sumai)
        if film_budget > 100000000:
            print(f"Filmo {self.title} budžetas daugiau nei 100 mln. USD") # True
        else:
            print(f"Filmo {self.title} budžetas mažiau nei 100 mln. USD") # False

# du objektai - du filmai (pavadinimas, rezisierius, biudzetas)
movie1 = Movie("Avatar", "James Cameron", 237000000)
movie2 = Movie("Ice age", "Chris Wedge", 59000000)
movie3 = Movie("I Wanna Dance with Somebody", "Kasi Lemmons", 45000000)

# issaukiami metodai
movie1.wasExpensive()
movie2.wasExpensive()
movie3.wasExpensive()
