# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 21:18:08 2022

@author: not bert
"""

import pygame as pyg

class chpiece:
    def __init__ (self, file, board, col = "w", m = {1:["x", "y+1"]}, n ="unknown", c = {1:["x-1", "y+1"], 2:["x+1", "y+1"]}, j = [False], r= False, v = 3, m_y = False, u = False):
        self.sprite = pyg.image.load(file).convert_alpha()
        self.img = pyg.transform.scale(self.sprite, (board.side_width, board.side_height))
        self.color = col
        self.moves = m
        # move notation: given a starting location x,y, the piece can end up at any of these combinations. n means any number
        self.name = n
        self.captures = c
        self.jumps = j
        self.reflects = r
        #Reflects means the piece's movement is reflected over the x axis for different teams, such as the pawn
        if ((self.reflects) & (self.color != "w")):
          for x in self.moves:
              self.moves[x][0] = self.moves[x][0].replace("-", "%")
              self.moves[x][1] = self.moves[x][1].replace("-", "%")
              self.moves[x][0] = self.moves[x][0].replace("+", "-")
              self.moves[x][1] = self.moves[x][1].replace("+", "-")
              self.moves[x][0] = self.moves[x][0].replace("%", "+")
              self.moves[x][1] = self.moves[x][1].replace("%", "+")
          for x in self.captures:
              self.captures[x][0] = self.captures[x][0].replace("-", "%")
              self.captures[x][1] = self.captures[x][1].replace("-", "%")
              self.captures[x][0] = self.captures[x][0].replace("+", "-")
              self.captures[x][1] = self.captures[x][1].replace("+", "-")
              self.captures[x][0] = self.captures[x][0].replace("%", "+")
              self.captures[x][1] = self.captures[x][1].replace("%", "+")
              
        self.value = v
        #approximate weight the AI should give the peice
        self.moved_yet = m_y
        self.upgrades = u
            
       
       


class king(chpiece):
    def __init__ (self, fil, boar, col = "w", moves = {1:["x", "y+1"], 2:["x+1", "y+1"], 3:["x-1", "y+1"], 4:["x-1", "y"], 5:["x-1", "y-1"], 6:["x", "y-1"], 7:["x+1", "y-1"], 8:["x+1", "y"]}, my= False):
        chpiece.__init__(self, file = fil, board = boar, col = col,  m = moves, n = "King", c= moves, j = [False, False, False, False, False, False, False, False], r = False, v = 200, m_y = my)

class queen(chpiece):
    def __init__ (self, fil, boar, col = "w", moves = {1:["x", "y+n"], 2:["x+n", "y+n"], 3:["x-n", "y+n"], 4:["x-n", "y"], 5:["x-n", "y-n"], 6:["x", "y-n"], 7:["x+n", "y-n"], 8:["x+n", "y"]}, my= False):
        chpiece.__init__(self, file = fil, board = boar, col = col,  m = moves, n = "Queen", c= moves, j = [False, False, False, False, False, False, False, False], r = False, v = 9, m_y = my)
        
class rook(chpiece):
    def __init__ (self, fil, boar, col = "w", moves = {1:["x", "y+n"], 2:["x-n", "y"], 3:["x", "y-n"], 4:["x+n", "y"]}, my= False):
        chpiece.__init__(self, file = fil, board = boar, col = col,  m = moves, n = "Rook", c= moves, j = [False, False, False, False], r = False, v = 5, m_y = my)
        
class bishop(chpiece):
    def __init__ (self, fil, boar, col = "w", moves = {1:["x+n", "y+n"], 2:["x-n", "y+n"], 3:["x-n", "y-n"], 4:["x+n", "y-n"]}, my= False):
        chpiece.__init__(self, file = fil, board = boar, col = col,  m = moves, n = "Bishop", c= moves, j = [False, False, False, False], r = False, v = 3, m_y = my)
        
class knight(chpiece):
    def __init__ (self, fil, boar, col = "w", moves = {1:["x-2", "y+1"], 2:["x-1", "y+2"], 3:["x+1", "y+2"], 4:["x+2", "y+1"], 5:["x+2", "y-1"], 6:["x+1", "y-2"], 7:["x-1", "y-2"], 8:["x-2", "y-1"]}, my= False):
        chpiece.__init__(self, file = fil, board = boar, col = col,  m = moves, n = "Knight", c= moves, j = [True, True, True, True, True, True, True, True], r = False, v = 3, m_y = my)

class pawn(chpiece):
    def __init__ (self, fil, boar, col = "w", my= False):
        chpiece.__init__(self, file = fil, board = boar, col = col,  m = {1:["x", "y+1"], 2:["x", "y+2"]}, n = "Pawn", c= {1:["x-1", "y+1"], 2:["x+1", "y+1"]}, j = [False, False], r = True, v = 1, m_y = my, u = True)

#fairy pieces
class knook(chpiece):
    def __init__ (self, fil, boar, col = "w", moves = {1:["x", "y+n"], 2:["x-n", "y"], 3:["x", "y-n"], 4:["x+n", "y"], 5:["x-2", "y+1"], 6:["x-1", "y+2"], 7:["x+1", "y+2"], 8:["x+2", "y+1"], 9:["x+2", "y-1"], 10:["x+1", "y-2"], 11:["x-1", "y-2"], 12:["x-2", "y-1"]}, my= False):
        chpiece.__init__(self, file = fil, board = boar, col = col,  m = moves, n = "knook", c= moves, j = [False, False, False, False, True, True, True, True, True, True, True, True], r = False, v = 9, m_y = my)

#Shatranj Pieces
class sarbaz(pawn):
    def __init__ (self, fil, boar, col = "w", my= False):
        chpiece.__init__(self, file = fil, board = boar, col = col,  m = {1:["x", "y+1"]}, n = "Sarbaz", c= {1:["x-1", "y+1"], 2:["x+1", "y+1"]}, j = [False, False], r = True, v = 1, m_y = my, u = True)
        
class ferz(chpiece):
    def __init__ (self, fil, boar, col = "w", moves = {1:["x+1", "y+1"], 2:["x-1", "y+1"], 3:["x-1", "y-1"], 4:["x+1", "y-1"]}, my= False):
        chpiece.__init__(self, file = fil, board = boar, col = col,  m = moves, n = "Ferz", c= moves, j = [False, False, False, False], r = False, v = 2, m_y = my)
        
class pil(chpiece):
    def __init__ (self, fil, boar, col = "w", moves =  {1:["x+2", "y+2"], 2:["x-2", "y+2"], 3:["x+2", "y-2"], 4:["x+2", "y-2"]}, my= False):
        chpiece.__init__(self, file = fil, board = boar, col = col,  m = moves, n = "Pil", c= moves, j = [True, True, True, True], r = False, v = 2, m_y = my)


#Xiangqi Pieces
class general(king):
    def __init__ (self, fil, boar, col = "w", moves = {1:["x", "y+1"], 2:["x-1", "y"], 3:["x", "y-1"], 4:["x+1", "y"]}, my= False):
        chpiece.__init__(self, file = fil, board = boar, col = col,  m = moves, n = "Jiang", c= moves, j = [False, False, False, False, False, False, False, False], r = False, v = 200, m_y = my)

class advisor(chpiece):
    def __init__ (self, fil, boar, col = "w", moves = {1:["x+1", "y+1"], 2:["x-1", "y+1"], 3:["x-1", "y-1"], 4:["x+1", "y-1"]}, my= False):
        chpiece.__init__(self, file = fil, board = boar, col = col,  m = moves, n = "Shi", c= moves, j = [False, False, False, False], r = False, v = 2, m_y = my)

class elephant(chpiece):
    def __init__ (self, fil, boar, col = "w", moves =  {1:["x+2", "y+2"], 2:["x-2", "y+2"], 3:["x+2", "y-2"], 4:["x+2", "y-2"]}, my= False):
        chpiece.__init__(self, file = fil, board = boar, col = col,  m = moves, n = "Xiang", c= moves, j = [False, False, False, False], r = False, v = 2, m_y = my)

class soldier(pawn):
    def __init__ (self, fil, boar, col = "w", my= False):
        chpiece.__init__(self, file = fil, board = boar, col = col,  m = {1:["x", "y+1"], 2:["x-1", "y"], 3:["x+1", "y"]}, n = "Zubing", c= {1:["x", "y+1"], 2:["x-1", "y"], 3:["x+1", "y"]}, j = [False, False, False], r = True, v = 1, m_y = my, u = False)

class cannon(chpiece):
    def __init__ (self, fil, boar, col = "w", moves = {1:["x", "y+n"], 2:["x-n", "y"], 3:["x", "y-n"], 4:["x+n", "y"]}, my= False):

        chpiece.__init__(self, file = fil, board = boar, col = col,  m = moves, n = "Pao", c= moves, j = [False, False, False, False], r = False, v = 4.5, m_y = my)
