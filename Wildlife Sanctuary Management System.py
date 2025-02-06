# ---------------------------------------------
# Wildlife Sanctuary Management System
# ---------------------------------------------
# This system manages:
# 1. Various types of animals (Mammals, Birds, Reptiles).
# 2. Animal interactions and behaviors.
# 3. Endangered status tracking for species.
# 4. Flying capabilities for certain bird species.
# ---------------------------------------------

# ---------------------------------------------
# Base Animal Class
# ---------------------------------------------

class Animal:
    """
    Represents a general animal with species classification.
    """

    population = 0  # Tracks total animal population

    def __init__(self, name, species):
        self.name = name
        self.species = species
        Animal.population += 1

    def get_info(self):
        """
        Retrieves basic information about the animal.
        """
        return f"Animal Name: {self.name} | Species: {self.species}"
    
    @classmethod
    def pop_amount(cls):
        """
        Retrieves the total population of animals in the sanctuary.
        """
        return f"Total animal population: {cls.population}"
    
    @staticmethod
    def is_wild(species):
        """
        Determines if an animal is wild based on species.
        """
        wild_animals = ["dolphin", "eagle", "snake"]
        return species in wild_animals
    
    def sleeping(self):
        """
        Simulates the animal sleeping.
        """
        return f"{self.name} is sleeping!"
    
    def eating(self):
        """
        Simulates the animal eating.
        """
        return f"{self.name} is eating!"
    
    def describe(self):
        """
        Describes the animal's appearance (to be overridden by subclasses).
        """
        return f"{self.name}'s color is {self.color} and it is {self.size}."

# ---------------------------------------------
# Endangered Status Mixin
# ---------------------------------------------

class IsEndangered:
    """
    Mixin class to track endangered species status.
    """

    def __init__(self, endanger_status):
        self.endanger_status = endanger_status

    def status(self):
        """
        Returns the conservation status of the animal.
        """
        return f"{self.name} is classified as {self.endanger_status}."

# ---------------------------------------------
# Mammal Class
# ---------------------------------------------

class Mammal(Animal):
    """
    Represents a mammal with swimming abilities.
    """

    def __init__(self, name, color, size, species):
        super().__init__(name, species)
        self.color = color
        self.size = size

    def swimming(self):
        """
        Simulates the mammal swimming.
        """
        return f"{self.name} is swimming!"

# ---------------------------------------------
# Bird Class
# ---------------------------------------------

class Bird(Animal):
    """
    Represents a bird with attributes like wingspan and length.
    """

    def __init__(self, name, color, size, species, wing_span, length):
        super().__init__(name, species)
        self.color = color
        self.size = size
        self.wing_span = wing_span
        self.length = length

    def running(self):
        """
        Simulates the bird running.
        """
        return f"{self.name} is running!"

    def describe(self):
        """
        Provides a detailed description of the bird.
        """
        return f"{self.name}'s color is {self.color}, size: {self.size}, wingspan: {self.wing_span} meters, length: {self.length} feet."

# ---------------------------------------------
# Reptile Class
# ---------------------------------------------

class Reptile(Animal):
    """
    Represents a reptile with slithering abilities.
    """

    def __init__(self, name, color, size, species):
        super().__init__(name, species)
        self.color = color
        self.size = size

    def slithering(self):
        """
        Simulates the reptile slithering.
        """
        return f"{self.name} is slithering!"

# ---------------------------------------------
# Flying Bird Class
# ---------------------------------------------

class FlyingBird(Bird):
    """
    Represents a bird that can fly and perform aerial maneuvers.
    """

    def __init__(self, name, color, size, species, wing_span, length):
        super().__init__(name, color, size, species, wing_span, length)

    def is_soaring(self):
        """
        Simulates the bird soaring in the sky.
        """
        return f"{self.name} is soaring!"

    def is_diving(self):
        """
        Simulates the bird diving.
        """
        return f"{self.name} is diving!"

    def flying(self):
        """
        Simulates the bird flying.
        """
        return f"{self.name} is flying!"

# ---------------------------------------------
# Endangered Bird Class
# ---------------------------------------------

class EndangeredBird(IsEndangered, FlyingBird):
    """
    Represents a flying bird that is endangered.
    """

    def __init__(self, name, color, size, species, endanger_status, wing_span, length):
        FlyingBird.__init__(self, name, color, size, species, wing_span, length)
        IsEndangered.__init__(self, endanger_status)

# ---------------------------------------------
# Interaction Class
# ---------------------------------------------

class Interacting:
    """
    Allows interaction with different animals.
    """

    def interact(self, animal):
        """
        Interacts with an animal by describing it.
        """
        return animal.describe()

# ---------------------------------------------
# Example Usage
# ---------------------------------------------

# Creating different animals
dolphin = Mammal(name="Dolph", color="Blue", size="Big", species="Dolphin")
eagle = EndangeredBird(name="Rick", color="Brown and White", size="Huge", species="Eagle", endanger_status="Endangered", wing_span=4.5, length=18)
snake = Reptile(name="Sabath", color="Black and White", size="Tiny", species="Garden Snake")

# Creating an interaction environment
environment = Interacting()

print("\n--- Animal Interactions ---")
print(environment.interact(dolphin))
print(environment.interact(eagle))
print(environment.interact(snake))

print("\n--- Animal Population & Wild Status ---")
print(Animal.pop_amount())
print(Animal.is_wild("dolphin"))
print(Animal.is_wild("eagle"))
print(Animal.is_wild("snake"))
print(Animal.is_wild("horse"))  # Not in the list

print("\n--- Endangered Bird Actions ---")
print(eagle.is_soaring())
print(eagle.is_diving())
print(eagle.flying())
print(eagle.describe())
print(eagle.eating())
print(eagle.sleeping())

print("\n--- Mammal Actions ---")
print(dolphin.swimming())
print(dolphin.describe())
print(dolphin.eating())
print(dolphin.sleeping())

print("\n--- Reptile Actions ---")
print(snake.slithering())
print(snake.describe())
print(snake.eating())
print(snake.sleeping())
