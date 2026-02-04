class Plant:
    """
    Plant class is a blueprint for representing plants.
    """
    def __init__(self, name: str, height: int, age: int)->None:
        self.name = name
        self.height = height
        self.age = age
    

    def grow(self, cm)->None:
        self.height += cm


    def age(self, days)->None:
        self.age += days
    
    def get_info(self)->None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


plant1 = Plant("Rose", 25, 30)
plant2 = Plant("Sunflower", 80, 45)
plant3 = Plant("Cactus", 15, 120)
