import os
path = os.getcwd() # get the path of the .pyde file

class Tile:
    def __init__(self, rowid, colid, id):
        self.rowid = rowid
        self.colid = colid
        self.id = id
        self.img = loadImage(path + "/images/" + str(id) + ".png")
        
    def display(self):
        #print("Now drawing tile " + str(self.id))
        image(self.img, self.colid * 200, self.rowid * 200, 200, 200)

        strokeWeight(5)
        noFill()
        rect(self.colid * 200, self.rowid * 200, 200, 200)

def setup():
    size(800, 800)
    background(0)
    
tiles = []
id = 0
for rowid in range(4):
    for colid in range(4):
        tiles.append(Tile(rowid, colid, id))
        id += 1

def draw():
    for tile in tiles:
        tile.display()
