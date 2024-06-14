import arcade 

class TTT(arcade.Window):
    def __init__ (self): # diese funktion heißt konstruktur und wird automatisch dann aufgerufen, wenn ein objekt der klasse TTT erstellt wird 
        super().__init__(600, 600, "Tic Tac Toe") # das fenster soll 600x600 pixel groß sein und den titel "tic tac toe" besitzen 

        arcade.set_background_color(arcade.color.DARK_TURQUOISE )        

        self.reset()
        
    def reset(self):
        self.arena = { (0, 0): "", (1, 0): "", (2, 0): "", (0, 1): "", (1, 1): "", (2, 1): "", (0, 2): "", (1, 2): "", (2, 2): ""}

        self.spieler = "X"


    def _gewinnprüfung(self):
        if self.arena[(0, 0)] == self.arena[(1, 0)] == self.arena[(2, 0)] != "":
            return True
        if self.arena[(0, 1)] == self.arena[(1, 1)] == self.arena[(2, 1)] != "":
            return True
        if self.arena[(0, 2)] == self.arena[(1, 2)] == self.arena[(2, 2)] != "":
            return True
        if self.arena[(0, 0)] == self.arena[(0, 1)] == self.arena[(0, 2)] != "":
            return True
        if self.arena[(1, 0)] == self.arena[(1, 1)] == self.arena[(1, 2)] != "":
            return True
        if self.arena[(2, 0)] == self.arena[(2, 1)] == self.arena[(2, 2)] != "":
            return True
        if self.arena[(0, 0)] == self.arena[(1, 1)] == self.arena[(2, 2)] != "":
            return True
        if self.arena[(0, 2)] == self.arena[(1, 1)] == self.arena[(2, 2)] != "":
            return True
        return False

   #gibt eine Liste mit positionen aller freien Felder zurück 
    def _freie_felder(self):
        
    
    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.Q:
            arcade.exit()
        if symbol == arcade.key.R:
            self.reset() 
    
    # Wird automatisch immer dann ausgeführt, wenn der Spieler mit der Maus klickt 
    # In x, y steht Position des Mausklicks

    def on_mouse_press(self, x, y, button, modifiers):
    
        x_arena = x // 200 # Durch 200 teilen und abrunden/alle Nachkommastellen abschneiden
        y_arena = y // 200
        # 0 <= x < 200 -> 0
        # 200 <= x < 400 -> 1
        # 400 <= x < 600 -> 2
        if self.arena[(x_arena ,y_arena)] =="" and not self._gewinnprüfung():
            self.arena[(x_arena ,y_arena)] = self.spieler 

            self.spieler = "O" if self.spieler == "X" else "X"


    def on_update(self, delta_time):
        ...

    def on_draw(self):
        self.clear()

        #Eine Weiße Linie der Dicke 12 von (x=20, y=200, x=580, y=200)
        arcade.draw_line(20, 200, 580, 200, arcade.color.DARK_GREEN, 12)
        arcade.draw_line(20, 400, 580, 400, arcade.color.DARK_GREEN, 12)
        arcade.draw_line(200, 580, 200, 20, arcade.color.DARK_GREEN, 12)
        arcade.draw_line(400, 580, 400, 20, arcade.color.DARK_GREEN, 12)

        for koordinaten in self.arena:
            x_arena = koordinaten[0]
            x_fenster = x_arena * 200 + 100 
            y_arena = koordinaten[1]
            y_fenster = y_arena * 200 + 100
            feld_inhalt = self.arena[koordinaten]
            arcade.draw_text(feld_inhalt, x_fenster, y_fenster,color=arcade.color.OFFICE_GREEN, font_size=120, font_name="Garamond", anchor_x="center", anchor_y="center")

        if self._gewinnprüfung():
            arcade.draw_rectangle_filled(self.width / 2, self.height / 2, self.width, self.height, arcade.make_transparent_color(arcade.color.PAYNE_GREY, 150))
            arcade.draw_text("Du hast gewonnen, Spieler " + ("X" if self.spieler == "O" else "O") + "!", self.width / 2, self.height / 2, color=arcade.color.SKY_BLUE, font_size=90, font_name="Garamond", width=self.width, align="center", anchor_x="center", anchor_y="center", multiline=True) 
TTT() 
arcade.run()
