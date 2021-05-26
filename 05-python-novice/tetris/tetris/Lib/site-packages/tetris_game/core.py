#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Implémentation du jeu Tetris

    Usage:

    >>> from tetris_game import TetrisGame
    >>> TetrisGame()
"""

from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

import random
import time
import csv
import os.path

from tetris_game.constantes import *

import os

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame

__all__ = ['Square', 'Line', 'Shape', 'Menu', 'TetrisFrame', 'TetrisGame']

class Square:
    """Class in charge of displaying a Square on the tetris main frame.
    A square is defined by is position (col, line) and his color.
    The size of the square is 38 * 38 px
    2 px has been removed in order to "display" a grid.
    In fact, the grid is made by the space between the squares.
    The "dessin" attribute contain the canvas correspondig to the square.

    A square with position x = 0 or x = 11 or y = 20 correspond to the border
    of the playground. In this case, his displayed by an image of brick.
    """
    photo_name = BRICK_IMG

    def __init__(self, col, line, canvas, parent):
        """Create the square object :
            - Make the square visible at the corresponding position (line, col)
            - Check if the square correspond to the border of the playground and
            display an image instead of a color.
            - The is_occuped attribute (bool) is setted to true if it's not
            possible for another square to replace this one.
            Two cases are possible : this square is a part of the border, or
            this square correspond to a part of a shape that has been locked
        """
        self.canvas = canvas
        self.parent = parent
        self.x = col
        self.y = line
        if self.x == 0 or self.x == 11 or self.y == 20:
            self.color = "red"
            self.is_occuped = True
            self.img = PhotoImage(file=Square.photo_name)
            self.dessin = self.canvas.create_image(40*col+1,
                                                   40*line+1,
                                                   anchor='nw',
                                                   image=self.img)
        else:
            self.color = "gray"
            self.is_occuped = False
            self.dessin = self.canvas.create_rectangle(40*col + 1,
                                                       40*line + 1,
                                                       40+(40*col)-1,
                                                       40+(40*line)-1,
                                                       fill=self.color)
            self.img = None

    def __repr__(self):
        """Used for debug only, display the status of the square"""
        return "{}".format('*' if self.is_occuped else '0')

    def toogleColor(self, occupied=True, color="gray"):
        """Method used to change the color of a Square.
        This method is used when a line is destroyed
        This method also update the is_occupied attribute.
        By default, color is setted to gray (correspond to an empty square)
        And the is_occuped attribute setted to true
        """
        self.canvas.itemconfig(self.dessin, fill = color)
        self.is_occuped = occupied
        return True

    def clean(self):
        """ Method used to delete a square (when a line is destroyed)
        The methode remove the canvas corresponding to the square, and the img"""
        self.canvas.delete(self.parent, self.dessin)
        del self.img

    def moveSquare(self, dY):
        """ This method move the canvas on the Y axis and update the square
        y position attribute. Method used when a moving shape goes down"""
        self.y += dY
        self.canvas.move(self.dessin, 0, 40 * dY)

class Line:
    """ The line class represent an entire line in the main Tetris PlayGround
    A line is composed by 12 square, including the borders. This class provide
    the graphical implementation of a line, and methods associated to a Line
    object in the tetris game (Like removing a line).
    """
    def __init__(self, y, canvas, parent, is_protected = False):
        """
            Create the line object.
            - Create a list of 12 Square object with the good coordinates.
            - By creating the square objetcs, they're also displayed (see Square)
            - The is_protected attribute is only used for the very last line,
            corresponding to the bottom border of the playground.

        """
        self.canvas = canvas
        self.parent = parent
        self.y = y
        self.square_list = []
        self.is_protected = is_protected
        for x in range(0,12,1):
            self.square_list.append(Square(x, self.y, self.canvas, self.parent))

    def __repr__(self):
        """ Only used for debug, display an array corresponding to the line.
        Ex. [1,0,0,1,1,0,1,0,0,0,0,1] 1 Correspond to square wich have
        is_occuped setted to true, 0 others"""

        return str([(1 if x.is_occuped else 0) for x in self.square_list]) + str(self.y)

    def binLine(self):
        """ Method used to check if a shape is able to move down or no.
        Bin line return the binary interpretation of the line.
        Exemple : a line like this [1,1,1,1,1,1,1,1,1,1,1,1] will return 4095
        A line like this [1,0,0,0,0,1,1,0,0,0,0,1,1] will return 2145
        """
        bin = 0
        for index, x in enumerate(self.square_list[::-1]):
            bin += (2**index if x.is_occuped else 0)
        return bin

    def isLoose(self):
        """ This method is used to check if the game can continue or no.
        In tetris, the game over when any square of the last line is occupied.
        This method check if any of the square (excludin the first and the last
        ones) has is is_occupied attribute setted to True"""
        start, *line, end = [x.is_occuped for x in self.square_list]
        return any(line)

    def lineFull(self):
        """ This method is used to check if a line is full or no.
        A full line correspond to a line where all the square have the
        is_occupied attribute setted to true"""
        return all([x.is_occuped for x in self.square_list])

    def moveLine(self, dY):
        """ Method used to move down a line.
        Update the y attribute with the dY parameters, and move all the squares
        of the line by calling the moveSquare method of the Square class"""
        self.y += dY
        for square in self.square_list:
            square.moveSquare(dY)

    def clean(self):
        """ The clean method is used to remove of a line from the playground.
        It removes of the square of the square_list => Unshow the square and
        del the square instance. Be carreful, the clean method does not delette
        the line instance"""
        for square in self.square_list :
            square.clean()
            del(square)

class Shape:
    """
        Class used to represent a shape used in the tetris_game.
        This class allow the tetris_game class to control a moving shaping
        (go down, rotate, lock)
    """
    def __init__(self, shape_type, rotation, shape_color, col, line):
        """ Create a shape object
        Shape_type is the type of shape as str ("T", "I", "O", "S", "Z", "L", "J")
        Rotation is an 0<=Int<4 corresponding to the willing rotation
        Shape_color is an str corresponding to the color ("red", "blue", ...)
        line and col is the position of the shape. The position is setted by
        the [0][0] index of the corresponding shape (see constantes.SHAPES)
        Finaly, the shape correspond to the good shape (as an 2D-array)"""

        self.shape_type = shape_type
        self.shape_rotation = rotation
        self.shape = SHAPES[shape_type][rotation]
        self.color = shape_color
        self.col = col
        self.line = line

    def canMoveShape(self, dX, dY, playground, rotate = False):
        """ canMoveShape method returns True if the shape can move of dX, dY in
        the specified playground. By default, the shape is the shape itself. By
        setting rotate to true, check if the rotation is possible by using the
        next rotation index of the shape instead of the current one"""
        #Getting the good shape
        if not rotate :
            shape = self.shape
        else :
            shape = SHAPES[self.shape_type][(self.shape_rotation +1)%4]

        #First, building an array of four arrays, corresponding to the four Line
        #that the shape will occup AFTER the move.
        #Here, we don't care about dY.

        #Building an empty array of 4 line and 12 cols
        table = []
        for y_temp in range(0,4):
            line = []
            for x_temp in range(0,12):
                line.append(0)
            table.append(line)

        #Filling the table array with the value of the shape, at the desired
        #Position.
        for y_temp in range(len(shape)):
            for x_temp in range(len(shape[y_temp])):
                if x_temp + self.col + dX < len(table[y_temp]):
                    #Here we fill table with the good value
                    table[y_temp][x_temp + self.col + dX] = shape[y_temp][x_temp]
            #Here, an entire line has been filled. Before filled the next one,
            #Convert the line to his binary version
            bin_table = 0
            for index, x in enumerate(table[y_temp][::-1]):
                bin_table+= x*2**index
            table[y_temp]= bin_table

        #Here table contains 4 lines with the new position of the shape as int
        # An exemple of what does table look like :
        # [[2048],
        # [2408],
        # [2048],
        # [2048]]

        #Now, we hava to create a table with the same shape of table, but
        #corresponding to the current status of the playground at the desired
        #positions. Here, we exctract all the line, so we don't care about dX
        #we use dY + the current position to extract to good lines
        table_compare = []
        #Filling the table with empty lines (except the border) in case
        #The expected position of the shape is on top of the playground
        for index in range(self.line + dY, 0):
            table_compare.append(0b100000000001)

        #Adding directly the binary representation of the desired playground lines
        for line in playground[max(self.line + dY,0) : self.line + dY + 4]:
            table_compare.append(line.binLine())

        #Completing the table to ensure that we have 4 lines
        #In case the shape is on the really bottom
        for index in range(4-len(table_compare), 5):
            table_compare.append(0b100000000001)

        #Here we have to tables :
        #1) table -> It's a table of four rows with the desired position of the shape
        #2) table_compare -> It's a table of four rows with the current content of the playground
        for y in range(0, 4):
            #We use the bit/bit & to check if there is a collision :
            # "100001" & "000100" => False
            # "100101" & "000100" => True -> Collision, so return False because we can't move
            if (table[y] & table_compare[y]) :
                return False
        return True

    def rotateShape(self):
        """Method used to update the shape array and it's rotation index"""
        self.shape = SHAPES[self.shape_type][(self.shape_rotation +1)%4]
        self.shape_rotation += 1

    def drawShape(self, playground, dessin = True):
        """Method used to draw the shape on the specified playground.
        By default, this method draw the shape. By specifying dessin = False,
        the methode undraw the shape"""
        for line_number, line in enumerate(self.shape) :
            for col_number, col in enumerate(line) :
                if self.shape[line_number][col_number] and line_number + self.line >=0 and col_number + self.col>= 0 :
                    if dessin :
                        playground[line_number + self.line].square_list[col_number + self.col].toogleColor(occupied=False, color=self.color)
                    else :
                        playground[line_number + self.line].square_list[col_number + self.col].toogleColor(occupied=False)

    def lockShape(self, playground):
        """Method used to lock a shape, meanwile the corresponding square
        id_occuped attributes are setted to True"""
        for line_number, line in enumerate(self.shape) :
            for col_number, col in enumerate(line) :
                if self.shape[line_number][col_number] and line_number + self.line >=0 and col_number + self.col>= 0 :
                    playground[line_number + self.line].square_list[col_number + self.col].toogleColor(occupied=True, color=self.color)

class Menu:
    """The menu Class create a Tk Canvas with all the game informations :
    Score, Future Shape, Number of line destroyed, Music Control"""

    def __init__(self, parent):
        """The init method only need the parent window to put the canvas in.abs
            The init method will call the load_score method to get the highest_score
            ever. It will also start the music, at 50% power by default
        """
        self.parent = parent
        self.canvas = Canvas(self.parent, bg="black", height=600, width=300, bd=0, highlightthickness=0)
        self.canvas.place(x=480, y=0)

        #Creating th futur shape array
        self.canvas.create_text(150,40,fill="red",font="Cambria 50 bold underline", text="Next")
        self.future_shape_array = []
        for y in range(0,6):
            line = []
            for x in range(0,6):
                self.canvas.create_rectangle(30+40*x + 1, 80+40*y + 1, 70+(40*x)-1, 120+(40*y)-1, fill="gray")
                if 0<x<5:
                    line.append(self.canvas.create_rectangle(30+40*x + 1, 80+40*y + 1, 70+(40*x)-1, 120+(40*y)-1, fill="gray"))
            if 0<y<5 :
                self.future_shape_array.append(line)

        #Addind the highest score
        self.load_score()
        self.canvas.create_text(150, 350, fill="red", font="Cambria 15 bold underline", text="Highest score")
        self.highest_score_label = self.canvas.create_text(150, 380 , fill="white", font="Cambria 20 italic", text=format(self.high_score,",").replace(",", " "))
        #Adding the current score
        self.current_score = 0
        self.canvas.create_text(150, 410, fill="red", font="Cambria 15 bold underline", text="Current score")
        self.current_score_label = self.canvas.create_text(150, 440 , fill="white", font="Cambria 20 italic", text=format(self.current_score,",").replace(",", " "))

        #Adding the number of line
        self.number_line = 0
        self.canvas.create_text(80, 480, fill="red", font="Cambria 15 bold underline", text="Lignes : ")
        self.lignes_label = self.canvas.create_text(150, 480, fill="white", font="Cambria 15 bold italic", text=str(self.number_line))


        #Adding the current level
        self.level_label = self.canvas.create_text(150, 540, fill="white", font="Cambria 25 bold italic", text="Level 1")

        #initing pygame and song playing
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.pre_init(44100, -16, 2, 1024)
        self.main_sound = pygame.mixer.Sound(MAIN_SONG)
        self.wall_sound = pygame.mixer.Sound(WALL_SONG)
        self.line_sound = pygame.mixer.Sound(LINE_SONG)
        self.loose_sound = pygame.mixer.Sound(LOOSE_SONG)
        self.level_up_sound = pygame.mixer.Sound(LEVEL_UP_SONG)
        self.list_song=[self.main_sound, self.wall_sound, self.line_sound, self.loose_sound, self.level_up_sound]
        self.change_volume('50')
        self.main_sound.play(-1)

        #Adding the volume control
        self.volume_canvas = Canvas(self.parent, bg="red", height=240, width=300, bd=0, highlightthickness=0)
        self.volume_canvas.place(x=480, y=600)
        self.volume_var =IntVar()
        self.volume_control = Scale(self.volume_canvas, orient='horizontal',
        from_=0, to=100,resolution=1, tickinterval=10, length=250,
        label='Volume (%)', variable=self.volume_var, command=self.change_volume)
        self.volume_control.set(50)
        self.volume_control.place(x=22,y=40)

    def increase_line_level(self, nb_line, current_level):
        """This method increase the number of line destroyed in the canvas.
        It also increase the level each time that the number of line is a multiple
        of 10. In this case, the level label is also updated.
        This method return the value of the current level, and the corresponding
        speedrate"""
        self.number_line += nb_line
        self.canvas.itemconfigure(self.lignes_label, text=str(self.number_line))
        level = self.number_line//10 + 1
        self.canvas.itemconfigure(self.level_label, text="Level " + str(level))
        level_speed = LEVELS[min(level, 20)]
        if level != current_level :
            self.level_up_sound.play()
        return level_speed, level

    def change_volume(self, volume_var):
        """ This method update the volume level to volume_var for all sounds"""
        for sound in self.list_song :
            sound.set_volume(int(volume_var)/100)

    def stop_music(self):
        """ This methods stop all the songs"""
        for sound in self.list_song :
            sound.stop()

    def update_future_shape(self, shape, color):
        """ Update the future shape representation with the given shape and the
        good color. shape has to be an array, and not an instance of shape"""
        for index_line, line in enumerate(self.future_shape_array):
            for index_col, col in enumerate(line) :
                if shape[index_line][index_col] :
                    self.canvas.itemconfig(self.future_shape_array[index_line][index_col], fill = color)
                else :
                    self.canvas.itemconfig(self.future_shape_array[index_line][index_col], fill = "gray")

    def load_score(self):
        """ This method load the highest score. It will try to open the file
        score.csv. If this file does not exist, it will be created.
        Score.csv is a one line csv file with all the past score seperated by
        a comma. It will create the score_list attribute, and the highest_score
        attribute"""
        if not os.path.isfile(SCORE_FILE) :
            f = open(SCORE_FILE, "w")
            f.close()

        self.score_list = []
        with open(SCORE_FILE) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader :
                self.score_list=row
        self.score_list = [int(x) for x in self.score_list]
        self.high_score = int(max(self.score_list or [0]))

    def update_score(self, delta):
        """This method update both the score_label and the highest_score_label.
        If the current score is upper than the highest, the highest score is
        updated and the highest_score_label also."""
        self.current_score += delta
        self.canvas.itemconfigure(self.current_score_label, text=format(self.current_score,",").replace(",", " "))
        if self.current_score > self.high_score:
            self.high_score = self.current_score
            self.canvas.itemconfigure(self.highest_score_label, text=format(self.high_score,",").replace(",", " "))

    def save_score(self):
        """This method append the current score to the score list and save it
        to the score.csv file"""
        self.score_list.append(self.current_score)
        with open(SCORE_FILE, 'w', newline='') as myfile:
            wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
            wr.writerow(self.score_list)
        return True

class TetrisFrame(Tk):
    """This class create a whole playable 780x840 tetris game window"""
    def __init__(self):
        """The init method setup the game.
        It configures the main window, create the playground canvas, init the
        game menu, bind the keyboard and start the main loop.
        """
        super().__init__()
        self.geometry("780x840")
        self.title("Tetris")
        self.iconbitmap(ICON_FILE)
        self.protocol("WM_DELETE_WINDOW",self.onClose)

        #PlayGround Canvas
        self.canvas = Canvas(self, bg="black", height=840, width=480, bd=0, highlightthickness=0)
        self.canvas.place(x=0, y=0)

        #Creating playground as a grid
        self.playground = []
        for y in range(0, 21, 1):
            self.playground.append(Line(y, self.canvas, self, is_protected = (True if y == 20 else False)))

        #Shapes containers:
        self.moving_shape = None
        self.future_shape = None

        #Adding the first Shape and the first future one
        self.moving_shape = self.getRandomShape()
        self.future_shape = self.getRandomShape()

        #Binding Keys
        self.bind("<Any-KeyPress>", self.__onKeypress)

        #initing the menu panel
        self.menu = Menu(self)
        self.menu.update_future_shape(self.future_shape.shape, self.future_shape.color)
        self.current_speed, self.current_level = self.menu.increase_line_level(0, 0)
        self.__animate()

    def __onKeypress(self, event):
        """Method called when a key is pressed. By default the entire keyboard
        is bindend, but we only trigger the left, right, down and space keys"""
        if event.keysym == "Down":
            #A press on the down key decrease the moving shape
            self.autoDecreaseShape()
        #Left and right allows the shape to move on X
        #Space allows the shape to rotate
        #In any of this three cases, we do the followings :
        # 1) Check if the shape can move to the desired position
        #   If yes : undraw the shape, move it, draw again
        #   If not : play a "block" sound
        elif event.keysym == "Left":
            if self.moving_shape.canMoveShape(-1, 0, self.playground):
                self.moving_shape.drawShape(self.playground, dessin = False)
                self.moving_shape.col -=1
                self.moving_shape.drawShape(self.playground, dessin = True)
            else :
                self.menu.wall_sound.play()
        elif event.keysym == "Right":
            if self.moving_shape.canMoveShape(1, 0, self.playground):
                self.moving_shape.drawShape(self.playground, dessin = False)
                self.moving_shape.col +=1
                self.moving_shape.drawShape(self.playground, dessin = True)
            else :
                self.menu.wall_sound.play()
        elif event.keysym == "space":
            if self.moving_shape.canMoveShape(0, 0, self.playground, rotate = True):
                self.moving_shape.drawShape(self.playground, dessin = False)
                self.moving_shape.rotateShape()
                self.moving_shape.drawShape(self.playground, dessin = True)
            else :
                self.menu.wall_sound.play()

    def __animate(self):
        """ This method is the main one. It is used to loop again and again while
        the game is not finish.
        Each time, we first clean the playground (removing lines that are full)
        Then check if the game is loose or no.
        If the game cam continue, comme back to this loop after the current_speed
        time
        """
        self.cleanPlayground()
        if self.playground[0].isLoose() :
            self.gameLoose()
        else :
            self.autoDecreaseShape()
            self.after(self.current_speed, self.__animate)

    def gameLoose(self):
        """Method called when the game is loose.
        It save the score, stop the main sound and play a looser song.
        The it ask the player to play again.
        If yes, reinit the game, if no, stop the program"""
        self.menu.save_score()
        self.menu.main_sound.stop()
        self.menu.loose_sound.play()
        if messagebox.askquestion ('You loose...','Want to play again ?',icon = 'question') == 'yes':
            for widget in self.winfo_children():
                widget.destroy()
            del self.menu
            self.destroy()
            self.__init__()
        else:
            messagebox.showinfo('Goodbye !','Thanks for playing Tetris ! Hope to see you soon !')
            self.destroy()

    def autoDecreaseShape(self):
        """Method that decrease Y position of the moving shape by one. If the
        shape cannot move anymore, it's been locked, the future shape is setted
        as the new moving shape, and a new future shape is created"""

        #Check if shape can go Down
        if self.moving_shape.canMoveShape(0, 1, self.playground):
            #If shape can go down, undraw it, move it, and redraw it
            self.moving_shape.drawShape(self.playground, dessin = False)
            self.moving_shape.line +=1
            self.moving_shape.drawShape(self.playground, dessin = True)
        else :
            #If not, lock the shape using the lockShape method
            self.moving_shape.lockShape(self.playground)
            self.moving_shape, self.future_shape = self.future_shape, self.getRandomShape()
            self.menu.update_future_shape(self.future_shape.shape, self.future_shape.color)

    def getRandomShape(self):
        """Return a randomize shape instance :
            - Random Shape
            - Random rotation
            - Random Color"""
        shape_type, shape_positions = random.choice(list(SHAPES.items()))
        shape_position = random.randint(0, len(shape_positions)-1)
        shape_color =  random.choice(COLORS)
        return Shape(shape_type, shape_position, shape_color, col=3, line=-4)

    def cleanPlayground(self):
        """This method removes lines that are full from the playground.
        If lines are removed, it call the Menu instance to modify the level, the
        speed the score and the number of lines destroyed"""

        #Creating an array wich aim to contain the lines to remove
        lines_to_remove = []
        for index, line in enumerate(self.playground):
            if line.lineFull() and not line.is_protected :
                lines_to_remove.append(line)

        #If they are line to remove, update the score, play the "woouf" song
        #And update the level and the refresh speed
        if lines_to_remove:
            nb_lines = len(lines_to_remove)
            self.menu.line_sound.play()
            if nb_lines == 4:
                delta = 1200 * self.current_level
            elif nb_lines == 3:
                delta = 300 * self.current_level
            elif nb_lines == 2:
                delta = 100 * self.current_level
            else:
                delta = 40 * self.current_level
            self.menu.update_score(delta)
            self.current_speed, self.current_level = self.menu.increase_line_level(nb_lines, self.current_level)

        #Remove all the line that are full and replace them by an empty line
        #on top of the playground
        #It's important to clean the line before deleting it in order to remove
        #the associated canvas
        for line_to_del in lines_to_remove :
            self.playground.remove(line_to_del)
            self.playground = [Line(0, self.canvas, self)] + self.playground
            line_to_del.clean()
            del(line_to_del)

        #Now we need to reindex all the line and move down the line that was upper
        #line that have been removed
        for num_line in range(0,20):
            if self.playground[num_line].y != num_line :
                #Move the line with num_line - y
                self.playground[num_line].moveLine(num_line -self.playground[num_line].y )

    def onClose(self):
        #On close method is called when the user click the red cross.
        #It save the score, and stop the music player.
        self.menu.save_score()
        self.menu.stop_music()
        try:
            self.destroy()
        except RuntimeWarning as e:
            print(e)

def TetrisGame():
    TetrisFrame().mainloop()

if __name__ == "__main__":
    TetrisGame()
