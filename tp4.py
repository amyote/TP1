import arcade



SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480


class Balle:
    def __init__(self, x, y, changeX, changeY, rayon, couleur):
        self.x = x
        self.y = y
        self.changeX = changeX
        self.changeY = changeY
        self.rayon = rayon
        self.couleur = couleur
    
    def on_draw(self):
        arcade.start_render()
        arcade.draw_circle_filled(self.x, self.y, self.rayon, self.couleur)
    
    def on_update(self):
        pass

class Rectangle:
    def __init__(self, x, y, changeX, changeY, largeur, hauteur, couleur, angle):
        self.x = x
        self.y = y
        self.changeX = changeX
        self.changeY = changeY
        self.largeur = largeur
        self.hauteur = hauteur
        self.couleur = couleur
        self.angle = angle
    
    def on_draw(self):
        arcade.start_render()
        arcade.draw_rectangle_filled(self.x, self.y, self.largeur, self.hauteur, self.couleur, self.angle)
    
    def on_update(self):
        pass

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.balles = []
        self.rectangles = []
    
    def on_draw(self):
        for balle in self.balles:
            self.balle.on_draw()
        for rectangle in self.rectangles:
            self.rectangle.on_draw()
    '''
    def on_update(self):
        for balle in self.balles:
            self.balle.on_update()
        for rectangle in self.rectangles:
            self.rectangle.on_update()
    '''
    def on_mouse_press(self, x, y, button, modifiers):
        print(button)
    

def main():

    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, "Tuto")
    arcade.run()

main()
