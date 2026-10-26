class Animal:
    def __init__(self, name, age, sex, kind, temperament, neutered):
        self.name = name
        self.age = age
        self.sex = sex
        self.kind = kind
        self.temperament = temperament
        self.neutered = neutered
        self.adopted_by = None


#a=animal

class AdoptionAgency:
    def __init__(self): 
        self.adoptable = [
            Animal("Spicy", "5", "F", "cat", "cuddly", "y"),
            Animal("Pepper", "5", "F", "cat", "quiet", "y"),
            Animal("Gulu", "7", "M", "cat", "cuddly", "y"),
            Animal("Buddy", "3", "M", "dog", "energetic", "y"),
        ]
        self.adopted = []




    def run(self):
        while True:
            print("\nWelcome to the PAWS Animal Adoption Agency!")
            print("Available animals:")
            for a in self.adoptable:
                print(f"- {a.name} the {a.kind}")



            if not self.adoptable or input("\nAdopt an animal? (yes/no): ").lower() != "yes":
                break


                
            animal = next((a for a in self.adoptable 
            if a.name.lower() == input("Which animal? ").lower()), None) #?


            if not animal:
                print("Animal not found.")
                continue
            print(f"Name: {animal.name}, Age: {animal.age}, Sex: {animal.sex}, Type: {animal.kind}, "
                  f"Temperament: {animal.temperament}, Neutered: {animal.neutered}")


                  
            if input(f"Adopt {animal.name}? (yes/no): ").lower() == "yes":
                animal.adopted_by = input("Your name: ")
                self.adopted.append(animal)
                self.adoptable.remove(animal)
                print(f"Congratulations! {animal.name} was adopted by {animal.adopted_by}.")

AdoptionAgency().run()