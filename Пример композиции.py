class Planet:

    def __init__(self, name):
        self.name = name

class Star:

    def __init__(self, name, star_type):
        self.name = name
        self.type = star_type

class System:
    
    def __init__(self, star_name, star_type):
        self.star = Star(star_name, star_type) # экземпляр класса System имеет свойство представляющее собой объект класса Star
        self.planets = []
    def add_planet(self, *name):
        for i in name:
            self.planets.append(Planet(i))
    def __str__(self):
        s = self.star.name + ': ' + self.star.type # self.star.name это свойство name объекта Star, который в свою очередь является свойством объекта System
        for i in self.planets:
            s += '\n' + i.name
        return s

solar_system = System('Sun', 'yellow')
solar_system.add_planet('Mercury', 'Venus', 'Earth')
solar_system.add_planet('Mars', 'Jupiter')
print(solar_system)