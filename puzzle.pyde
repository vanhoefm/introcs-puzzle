add_library("minim")
import os, random
path = os.getcwd() # get the path of the .pyde file
audioPlayer = Minim(this)

class Tile:
    def __init__(self, rowid, colid, id):
        self.rowid = rowid
        self.colid = colid
        self.id = id
        self.img = loadImage(path + "/images/" + str(id) + ".png")
        
    def display(self, win):
        if not win and self.id == 15:
            return
        
        #print("Now drawing tile " + str(self.id))
        image(self.img, self.colid * 200, self.rowid * 200, 200, 200)

        if not win:
            stroke(0, 0, 0)
            strokeWeight(5)
            noFill()
            rect(self.colid * 200, self.rowid * 200, 200, 200)
        
class Puzzle:
    def __init__(self):
        self.win = False
        self.tiles = []
        id = 0
        for rowid in range(4):
            for colid in range(4):
                self.tiles.append(Tile(rowid, colid, id))
                id += 1
        self.clickSound = audioPlayer.loadFile(path + "/sounds/click.mp3")
        self.bgSound = audioPlayer.loadFile(path + "/sounds/background.mp3")
        self.winSound = audioPlayer.loadFile(path + "/sounds/win.mp3")
        #self.bgSound.play()
    
    def display(self):
        background(0)
        for tile in self.tiles:
            tile.display(self.win)
        
        if not self.win:
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
                self.win = self.checkSolved()
                print("Swap with", rowDirection, colDirection)
    
    def checkSolved(self):
        for tile in self.tiles:
            if tile.rowid * 4 + tile.colid != tile.id:
                return False
            
        self.winSound.rewind()
        self.winSound.play()
        return True
    
    def shufflePuzzle(self, difficulty=10):
        emptyTile = self.getTile(3, 3)
        print("Shuffling puzzle..")
        
        for i in range(difficulty):
            direction = random.choice([[1,0], [-1,0], [0,1], [0,-1]])
            rowDirection = direction[0]
            colDirection = direction[1]
            otherTile = self.getTile(emptyTile.rowid + rowDirection, emptyTile.colid + colDirection)
            if otherTile != False:
                print("Shuffle: now swapping tiles")
                self.swapTile(emptyTile, otherTile)
        
def setup():
    size(800, 800)
    background(0)

p = Puzzle()
p.shufflePuzzle()

def draw():
    p.display()

def mouseClicked():
    if p.win:
        p.shufflePuzzle()
        p.win = False
    else:
        p.handleMouseClick()
