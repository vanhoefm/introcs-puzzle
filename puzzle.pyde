add_library("minim")
import os
path = os.getcwd() # get the path of the .pyde file
audioPlayer = Minim(this)

class Tile:
    def __init__(self, rowid, colid, id):
        self.rowid = rowid
        self.colid = colid
        self.id = id
        self.img = loadImage(path + "/images/" + str(id) + ".png")
        
    def display(self):
        if self.id == 15:
            return
        
        #print("Now drawing tile " + str(self.id))
        image(self.img, self.colid * 200, self.rowid * 200, 200, 200)

        stroke(0, 0, 0)
        strokeWeight(5)
        noFill()
        rect(self.colid * 200, self.rowid * 200, 200, 200)

class Puzzle:
    def __init__(self):
        self.tiles = []
        id = 0
        for rowid in range(4):
            for colid in range(4):
                self.tiles.append(Tile(rowid, colid, id))
                id += 1
        self.clickSound = audioPlayer.loadFile(path + "/sounds/click.mp3")
        self.bgSound = audioPlayer.loadFile(path + "/sounds/background.mp3")
        #self.bgSound.play()
    
    def display(self):
        background(0)
        for tile in self.tiles:
            tile.display()
        
        colid = mouseX // 200
        rowid = mouseY // 200
        stroke(0, 255, 0)
        rect(colid * 200, rowid * 200, 200, 200)
        
    def getTile(self, rowid, colid):
        for tile in self.tiles:
            if tile.rowid == rowid and tile.colid == colid:
                return tile
        return False
    
    def swapTile(self, tile1, tile2):
        tmp = tile1.rowid
        tile1.rowid = tile2.rowid
        tile2.rowid = tmp
        
        tmp = tile1.colid
        tile1.colid = tile2.colid
        tile2.colid = tmp
        
    def handleMouseClick(self):
        colid = mouseX // 200
        rowid = mouseY // 200
        tile = self.getTile(rowid, colid)
        print(rowid, colid, tile)
        
        for directions in [[1,0], [-1,0], [0,1], [0,-1]]:
            #print(directions)
            rowDirection = directions[0]
            colDirection = directions[1]
            neighborTile = self.getTile(rowid + rowDirection, colid + colDirection)
            if neighborTile != False and neighborTile.id == 15:
                self.swapTile(tile, neighborTile)
                self.clickSound.rewind()
                self.clickSound.play()
                print("Swap with", rowDirection, colDirection)
    
        
def setup():
    size(800, 800)
    background(0)

p = Puzzle()

def draw():
    p.display()

def mouseClicked():
    p.handleMouseClick()
