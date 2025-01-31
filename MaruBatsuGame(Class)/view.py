from marubatsu import MaruBatsu

# view.py
class View :

    def __init__(self,game) :
        self.view = game
        self.field = self.view.field
        self.size = self.view.size
        
    def print_field(self) :
        print("    ", end = "")
        for num in range(self.size):
            print(f" {self.view.ALPHABET[num]} ",  end= "")
        print()
        print("   +"+"---"*self.size + "+")

        for y in range(self.size):
            print(f" {y} ", end ="|")
            for x in range(self.size):
                print(self.field[x][y].value, end = "")        
            print("|")
    
        print("   +"+"---"*self.size + "+")

