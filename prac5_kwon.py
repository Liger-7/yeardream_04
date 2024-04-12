# prac5.py

from typing import Any


class Zoo:
    def __init__(self):
        self.animal_list = []
        pass

    def add_animal(self, animal):
        a, b = animal, self.animal_list
        
        if a not in b:
            self.animal_list.append(a)
        else :
            print(f"\"{a.name} The {a.species}\"은 이미 동물원에 있습니다. 다른 이름을 사용하거나, 다른 종으로 추가해주세요.")
        pass

    def show_animals(self):
        for i in self.animal_list:
            print(f"{i.name} The {i.species}")
        pass

    def show_animals_by_species(self, animal_name):
        for i in self.animal_list:
            if i.species == animal_name:
                print(f"{i.name} The {i.species}")

    def __repr__(self) -> str:
        return f"{self.animal_list}"

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        pass
    def __repr__(self) -> str:
        return f"{self.name, self.species}"

def main():
    # 동물원을 선언하고 10마리의 동물들을 추가합니다.
    zoo = Zoo()
    zoo.add_animal(Animal("Leo", "Lion"))
    zoo.add_animal(Animal("Harry", "Hippo"))
    zoo.add_animal(Animal("Ella", "Elephant"))
    zoo.add_animal(Animal("Gerry", "Giraffe"))
    zoo.add_animal(Animal("Gira", "Giraffe"))
    zoo.add_animal(Animal("Terry", "Lion"))
    zoo.add_animal(Animal("Barry", "Bear"))
    zoo.add_animal(Animal("Larry", "Leopard"))
    zoo.add_animal(Animal("Cary", "Crocodile"))
    zoo.add_animal(Animal("Mary", "Monkey"))

    print(zoo)
    # 동물원에 있는 모든 동물을 출력합니다.
    # zoo.show_animals()
    ## 출력 결과 : 
    '''
    현재 동물원에는 다음 동물들이 있습니다 :
    - Leo the Lion
    - Harry the Hippo
    - Ella the Elephant
    - Gerry the Giraffe
    - Gira the Giraffe
    - Terry the Lion
    - Barry the Bear
    - Larry the Leopard
    - Cary the Crocodile
    - Mary the Monkey
    '''

    # 특정 종에 해당하는 동물들의 이름만 출력합니다.
    # zoo.show_animals_by_species("Lion")
    # 출력 결과 : 
    '''
    - Leo the Lion
    - Terry the Lion
    '''
    # zoo.show_animals_by_species("Elephant")
    # 출력 결과 : 
    '''
    - Ella the Elephant
    '''

    # 이미 존재하는 동물을 추가한 경우, 해당 동물이 이미 있음을 출력합니다.
    zoo.add_animal(Animal("Leo", "Lion"))
    # 출력 결과 : 
    '''
    "Leo the Lion"은 이미 동물원에 있습니다. 다른 이름을 사용하거나, 다른 종으로 추가해주세요.
    '''
    # print(zoo)
if __name__ == "__main__":
    main()