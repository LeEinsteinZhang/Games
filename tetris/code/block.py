class Block:
    RED = "../pic/red.png"
    ORANGE = "../pic/orange.png"
    YELLOW = "../pic/yellow.png"
    GREEN = "../pic/green.png"
    CYAN = "../pic/cyan.png"
    BLUE = "../pic/blue.png"
    PURPLE = "../pic/purple.png"

    def __init__(self):
        self.I = [[(0,0), (0,1), (0,2), (0,3)], [(0,0), (1,0), (2,0), (3,0)]]
        self.J = [[(0,0), (1,0), (1,1), (1,2)], []]
