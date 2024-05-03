import arcade 

class TTT(arcade.Window):
    def __init__ (self): # diese funktion heißt konstruktur und wird automatisch dann aufgerufen, wenn ein objekt der klasse TTT erstellt wird 
        super().__init__(600, 600, "Tic Tac Toe") # das fenster soll 600x600 pixel groß sein und den titel "tic tac toe" besitzen 

        self.arena = { (0, 0): "", (1, 0): "", (2, 0): "", (0, 1): "", (1, 1): "", (2, 1): "", (0, 2): "", (1, 2): "", (2, 2): ""}

        self.spieler = "X"

    # Wird automatisch immer dann ausgeführt, wenn der Spieler mit der Maus klickt 
    # In x, y steht Position des Mausklicks

    def on_mouse_press(self, x, y, button, modifiers):
    
        x_arena = x // 200 # Durch 200 teilen und abrunden/alle Nachkommastellen abschneiden
        y_arena = y // 200
        # 0 <= x < 200 -> 0
        # 200 <= x < 400 -> 1
        # 400 <= x < 600 -> 2
        self.arena[(x_arena ,y_arena )] = self.spieler

        self.spieler = "O" if self.spieler == "X" else "x"
    def on_update(self, delta_time):
        ...

    def on_draw(self):
        self.clear()

        #Eine Weiße Linie der Dicke 12 von (x=20, y=200, x=580, y=200)
        arcade.draw_line(20, 200, 580, 200, arcade.color.WHITE, 12)
        arcade.draw_line(20, 400, 580, 400, arcade.color.WHITE, 12)
        arcade.draw_line(200, 580, 200, 20, arcade.color.WHITE, 12)
        arcade.draw_line(400, 580, 400, 20, arcade.color.WHITE, 12)

        for koordinaten in self.arena:
            x_arena = koordinaten[0]
            x_fenster = x_arena * 200 + 100 
            y_arena = koordinaten[1]
            y_fenster = y_arena * 200 + 100
            feld_inhalt = self.arena[koordinaten]
            arcade.draw_text(feld_inhalt, x_fenster, y_fenster, font_size=70, font_name="Garamond", anchor_x="center", anchor_y="center")


TTT() 
arcade.run()
