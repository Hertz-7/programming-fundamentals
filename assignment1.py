### YOUR CODE FOR calculateArea() FUNCTION GOES HERE ###
def calculateArea(length,width):
    area = length*width
    return area

#### End OF MARKER



### YOUR CODE FOR checkTilesFit() FUNCTION GOES HERE ###
def checkTilesFit(plot_width, plot_length , tile_width , tile_length):
    w = plot_width / tile_width
    l = plot_length / tile_length
    a = plot_width * plot_length
    b = tile_length * tile_width
    tiles = a%b
    tiles2 = w*l
    if ( int(w) != w or int(l) != l ) :
        if tiles==0 :
            return True
        else:
            return False
    else:
        return True
    if  plot_width < 0 or tile_width < 0 or tile_length < 0 or plot_length < 0:
        return False
    else:
        return True
        

#### End OF MARKER


### YOUR CODE FOR calculateTiles() FUNCTION GOES HERE ###

def calculateTiles(plot_width, plot_length , tile_width , tile_length):
    if type(plot_width)==str or type(plot_length)==str or type(tile_width)==str or type(tile_length)== str:
        return "Invalid Input"
    elif plot_width== 0 or plot_length== 0 or tile_width== 0 or tile_length == 0 :
        return None
    r = checkTilesFit(plot_width, plot_length , tile_width , tile_length)
    if r == True:
        w= plot_width / tile_width
        l= plot_length / tile_length
        tiles = int(w*l)
        return tiles
    elif r == False:
        return "Not Possible"
    
    

#### End OF MARKER



