# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pygame
import pieces as pc
import statistics as stat
import copy
import chessbot as cb
  

 
# CREATING CANVAS




class board:
    def __init__ (self, dim = [8,8], perc = 60, screen = [800, 800]):
        self.screen_size = screen
        self.size = dim
        self.percent = perc/100
        self.side_width = self.percent*self.screen_size[0]/(self.size[0])
        self.side_height = self.percent*self.screen_size[1]/(self.size[1])
        self.squares = {}
        self.squarecolors = {}
        #self.squares will be dictionary of square (in chess notation format) and edges of that square
        #self.squarecolors will be dictionary of squares (in chess notation) and that square's color
        self.square_pieces = {}
        self.turnqueau = ["b"]
        self.turn = "w"
        #self.square_pieces is a dictionary of pieces on each square at any given time. Each piece is a Piece object
        for x in range(self.size[0]):
            for y in range(self.size[1]):
                name = chr(ord('@')+x + 1) + str(self.size[1]-y)
                self.squares[name] = [x*self.side_width + (1-self.percent)*self.screen_size[0]/6, (x+1)*self.side_width + (1-self.percent)*self.screen_size[0]/6, y*self.side_height + (1-self.percent)*self.screen_size[1]/2, (y+1)*self.side_height + (1-self.percent)*self.screen_size[1]/2]
                self.square_pieces[name] = ""
                if (x+y + 1) % 2 == 0:
                    self.squarecolors[name] = (100,40,0)
                else:
                    self.squarecolors[name] = (255, 255, 255)
        self.enpassant = [False, [], "", "", ""]
        self.castle_moves = {}
        self.teams_castle = {"w":True, "b":True}
        #dictionary of permissions of whom has had castling disabled, True means may still
        #castle if conditions allow
        self.check = False
        self.AIgame = False
        self.AIcolor = ""
        self.piecetypes = {}
        #array of all different piece types on board at start of game
        
    def loadboard(self, Arrangement={}):
        #will load self.square_pieces with the arrangement of chess pieces at the beginning of the game
        #arrangement is dictionary of squares and their pieces, only containing squares with pieces
        for x in self.square_pieces:
            if x in Arrangement:
                self.square_pieces[x] = Arrangement[x]
               

    def drawboard(self, canvas):
        for x in range(0, self.size[0],1):  
            font = pygame.font.SysFont(None, 24)
            letter = font.render(chr(65+x), True, (255, 255, 255))
            canvas.blit(letter, ((stat.mean([self.squares[list(self.squares)[0]][0], self.squares[list(self.squares)[0]][1]]) - 5) + x*self.side_width, self.squares[list(self.squares)[0]][2] -20))
            canvas.blit(letter, ((stat.mean([self.squares[list(self.squares)[0]][0], self.squares[list(self.squares)[0]][1]]) - 5) + x*self.side_width, self.squares[list(self.squares)[(self.size[0]*self.size[1] -1)]][3] + 10))
        for x in range(0, self.size[1],1):  
            font = pygame.font.SysFont(None, 24)
            number = font.render(str(self.size[1]-x), True, (255, 255, 255))
            canvas.blit(number, (self.squares[list(self.squares)[0]][0] -20, (stat.mean([self.squares[list(self.squares)[0]][2], self.squares[list(self.squares)[0]][3]]) - 5) + x*self.side_height))
            canvas.blit(number, (self.squares[list(self.squares)[(self.size[0]*self.size[1] -1)]][1]+10, (stat.mean([self.squares[list(self.squares)[0]][2], self.squares[list(self.squares)[0]][3]]) - 5) + x*self.side_height))
        for x in self.squares:
            pygame.draw.rect(canvas, self.squarecolors[x], pygame.Rect(self.squares[x][0], self.squares[x][2], self.side_width, self.side_height))
            #print("drew " + x + " successfully")
            if self.square_pieces[x] != "":
                canvas.blit(self.square_pieces[x].img, (self.squares[x][0],self.squares[x][2]))
                #renders piece on that square if the square contains a piece
                
    def getcoords(self, key):
        #returns top left corner of a chess square given its standard letter
        return(self.squares[key][0],self.squares[key][2])
    
    def move(self, start, end):
        #returns 0 if no move, 1 if normal move, 2 if piece is upgraded
        if (self.square_pieces[start] == ""): 
            return 0
        elif (self.square_pieces[start].color != self.turn):
            return 0
        else:
            if (self.square_pieces[end] != ""):
                if (self.square_pieces[start].color == self.square_pieces[end].color):
                    return 0
            if ((end == self.enpassant[4]) & (start in self.enpassant[1])):
                self.square_pieces[self.enpassant[2]] = ""
                self.enpassant = [False,[], "", "", ""]  
                #executes en passant if it possible, and resets ability
                
            self.square_pieces[end] = self.square_pieces[start]
            self.square_pieces[end].moved_yet = True
            temp = self.turn
            self.turn = self.turnqueau.pop()
            self.turnqueau.insert(0, temp)
            self.square_pieces[start] = ""
            
            if (isinstance(self.square_pieces[end], pc.pawn) & (abs(int(end[1]) - int(start[1])) == 2)):
                #This block checks for en passant opportunities next turn, and logs them
                possible = [(chr(ord(end[0])-1) + end[1]), (chr(ord(end[0])+1) + end[1])]
                for x in possible:
                    if (x in self.square_pieces):
                        if (self.square_pieces[x] != ""):
                            if (isinstance(self.square_pieces[x], pc.pawn) & (self.square_pieces[x].color != self.square_pieces[end].color)):
                                self.enpassant[0] = True
                                self.enpassant[1].append(x)
                                self.enpassant[2] = end
                                self.enpassant[3] = start
            else:
                self.enpassant = [False,[], "", "", ""]   
            
            if ((isinstance(self.square_pieces[end], pc.king))):
                if self.teams_castle[self.square_pieces[end].color] == True:
                    if end in self.castle_moves:
                        self.square_pieces[self.castle_moves[end][0]] = self.square_pieces[self.castle_moves[end][1]]
                        self.square_pieces[self.castle_moves[end][0]].moved_yet = True
                        self.square_pieces[self.castle_moves[end][1]] = ""
                    self.teams_castle[self.square_pieces[end].color] = False
                else:
                    return 1
            if ((self.square_pieces[end].upgrades == True) & (("1" in end) | ("8" in end))):
                if self.AIgame ==  True:
                    if self.square_pieces[end].color == self.AIcolor:
                        bord = self
                        cb.choosepiece(bord, start, end, real = True)
                    else:
                        self.choose_upgrade(end)
                else:
                    self.choose_upgrade(end)
                return 2
            else:
                return 1
                
    def choose_upgrade(self, sq):
        answer = False
        while (not answer):
            newpiece = input("Enter piece to upgrade pawn to \n")
            if newpiece == "queen":
                answer = True
                if (self.square_pieces[sq].color == "b"):
                    self.square_pieces[sq] = pc.queen("art/bqueen.png", self, col = "b")
                elif (self.square_pieces[sq].color == "w"):
                    self.square_pieces[sq] = pc.queen("art/wqueen.png", self)
            elif newpiece == "knight":
                answer = True
                if (self.square_pieces[sq].color == "b"):
                    self.square_pieces[sq] = pc.knight("art/bknight.png", self, col = "b")
                elif (self.square_pieces[sq].color == "w"):
                    self.square_pieces[sq] = pc.knight("art/wknight.png", self)
            elif newpiece == "rook":
                answer = True
                if (self.square_pieces[sq].color == "b"):
                    self.square_pieces[sq] = pc.rook("art/brook.png", self, col = "b")
                elif (self.square_pieces[sq].color == "w"):
                    self.square_pieces[sq] = pc.rook("art/wrook.png", self)
            elif newpiece == "bishop":
                answer = True
                if (self.square_pieces[sq].color == "b"):
                    self.square_pieces[sq] = pc.bishop("art/bbishop.png", self, col = "b")
                elif (self.square_pieces[sq].color == "w"):
                    self.square_pieces[sq] = pc.bishop("art/wbishop.png", self)
        
    def checklegal(self, start, end):
        if (self.square_pieces[start] == ""):
            return False
        elif(end not in self.square_pieces):
            return False
        elif(end in self.find_movesp(self.square_pieces[start], start)):
            return True
        else:
            #print("cant do that!")
            #print(self.square_pieces[start].moved_yet)
            return False
        
    def find_movesp(self, piece, location):
        #finds all the possible squares a single piece on the board can move to
        #returns list of squares a piece can move to
        x,y = [ord(location[0])-65, int(location[1])]
        destinations =[]
        if piece.moves == piece.captures:
         for z in piece.moves:
             if (("n" in piece.moves[z][0]) | ("n" in piece.moves[z][1])):
                 for k in range(1,8,1):
                     n = k
                     a = eval(piece.moves[z][0])
                     b = eval(piece.moves[z][1])
                     dest = chr(a+65)+str(b)
                     if (dest in self.squares):
                         if (self.square_pieces[dest] != ""):
                             if (self.square_pieces[dest].color != piece.color):
                                 destinations.append(dest)
                             if (piece.jumps[z-1] == False):
                                 break
                         else:
                             destinations.append(dest)
             else:
                 a = eval(piece.moves[z][0])
                 b = eval(piece.moves[z][1])
                 dest = chr(a+65)+str(b)
                 if (dest in self.squares):
                     if (self.square_pieces[dest] != ""):
                         if (self.square_pieces[dest].color == piece.color):
                             continue
                     if piece.jumps[z-1] == False:
                         pl = self.find_between(location, dest)
                         if pl != []:
                             flag = False
                             for k in pl:
                                 if self.square_pieces[k] != "":
                                     flag = True
                                     break
                             if flag == False:
                                 destinations.append(dest)
                         else:
                             destinations.append(dest)
                     else:
                         destinations.append(dest)
        else:
            if (isinstance(piece, pc.pawn) & piece.moved_yet == True):
                if (len(self.square_pieces[location].moves) > 1):
                    self.square_pieces[location].moves.popitem()
            for z in piece.moves:
                if (("n" in piece.moves[z][0]) | ("n" in piece.moves[z][1])):
                    for k in range(1,8,1):
                        n = k
                        a = eval(piece.moves[z][0])
                        b = eval(piece.moves[z][1])
                        dest = chr(a+65)+str(b)
                        if (dest in self.squares):
                           if (self.square_pieces[dest] == ""):
                               destinations.append(dest)
                           else:
                               if (piece.jumps[z-1] == False):
                                   break


                else:
                    a = eval(piece.moves[z][0])
                    b = eval(piece.moves[z][1])
                    dest = chr(a+65)+str(b)
                    if (dest in self.squares): 
                        if (self.square_pieces[dest] == ""):
                            if piece.jumps[z-1] == False:
                                pl = self.find_between(location, dest)
                                if pl != []:
                                    flag = False
                                    for k in pl:
                                        if self.square_pieces[k] != "":
                                            flag = True
                                            break
                                    if flag == False:
                                        destinations.append(dest)
                                else:
                                    destinations.append(dest)
                            else:
                                destinations.append(dest)
                                
                        
            for z in piece.captures:
                if (("n" in piece.captures[z][0]) | ("n" in piece.captures[z][1])):
                    for k in range(1,8,1):
                        n = k
                        a = eval(piece.captures[z][0])
                        b = eval(piece.captures[z][1])
                        dest = chr(a+65)+str(b)
                        if (dest in self.squares):
                           if (self.square_pieces[dest] != ""):
                               if (self.square_pieces[dest].color != piece.color):
                                   destinations.append(dest)
                               if (piece.jumps[z-1] == False):
                                   break

                else:
                    a = eval(piece.captures[z][0])
                    b = eval(piece.captures[z][1])
                    dest = chr(a+65)+str(b)
                    if (dest in self.squares):
                       if (self.square_pieces[dest] != ""):
                           if (self.square_pieces[dest].color != piece.color):
                               if piece.jumps[z-1] == False:
                                   pl = self.find_between(location, dest)
                                   if pl != []:
                                       flag = False
                                       for k in pl:
                                           if self.square_pieces[k] != "":
                                               flag = True
                                               break
                                       if flag == False:
                                           destinations.append(dest)
                                   else:
                                       destinations.append(dest)
                               else:
                                   destinations.append(dest)

        if ((self.enpassant[0] == True) & (isinstance(self.square_pieces[location], pc.pawn)) & (location in self.enpassant[1])):
            p = (self.enpassant[2][0] + chr(stat.mean([ord(self.enpassant[2][1]), ord(self.enpassant[3][1])])))
            self.enpassant[4] = p
            destinations.append(p)     
            #Adds a square a pawn can do an en passant to if its allowed this turn
            
        if (self.teams_castle[self.square_pieces[location].color] == True) & (isinstance(piece, pc.king)):
            #checks if a king can castle
            destinations = destinations + self.verify_castle(location)
       
        return destinations
    
    def find_moves2(self, piece, location):
        #streamlined version of find_movesp used to calculate castling through check
        x,y = [ord(location[0])-65, int(location[1])]
        destinations =[]
        for z in piece.captures:
            if (("n" in piece.captures[z][0]) | ("n" in piece.captures[z][1])):
                for k in range(1,8,1):
                    n = k
                    a = eval(piece.captures[z][0])
                    b = eval(piece.captures[z][1])
                    dest = chr(a+65)+str(b)
                    if (dest in self.squares):
                         destinations.append(dest)
                         if (self.square_pieces[dest] != ""):
                            if (piece.jumps[z-1] == False):
                                break
            else:
                a = eval(piece.captures[z][0])
                b = eval(piece.captures[z][1])
                dest = chr(a+65)+str(b)
                if (dest in self.squares):
                    if piece.jumps[z-1] == False:
                        pl = self.find_between(location, dest)
                        if pl != []:
                            flag = False
                            for k in pl:
                                if self.square_pieces[k] != "":
                                    flag = True
                                    break
                            if flag == False:
                                destinations.append(dest)
                        else:
                            destinations.append(dest)
                    else:
                        destinations.append(dest)
            
        return destinations
    
    def verify_castle(self, start):
        #checks if a king on a square, start, can castle, and returns end destinations
        if (isinstance(self.square_pieces[start], pc.king) &  self.square_pieces[start].moved_yet == False):
            locations = []
            p1 = [] #farther castle
            for x in range(-4,0,1):
                p1.append(chr(ord(start[0])+x) + start[1])   
                #generates array of squares that will have to be checked for castling
            p2 = [] #closer castle
            for x in range(1,4,1):
                p2.append(chr(ord(start[0])+x) + start[1]) 
            p1.reverse()
            
            #This little for loop makes it so you can't castle through check
            for x in self.square_pieces:
                if self.square_pieces[x] != "":
                    if self.square_pieces[x].color != self.square_pieces[start].color:
                        for z in self.find_moves2(self.square_pieces[x], x):
                            if z in p1:
                                p1 = ["nope"]
                            if z in p2:
                                p2 = ["nope"]
                            if (("nope" in p1) & ("nope" in p2)):
                                return []
            
            
            for x in p1:
                if x in self.squares:
                    if self.square_pieces[x] != "":
                        if ((x == p1[3]) & (isinstance(self.square_pieces[x], pc.rook)) & (self.square_pieces[x].moved_yet == False)):
                            #This code won't execute unless everything else is good to castle
                            self.castle_moves[p1[1]] = [p1[0], p1[3]]
                            locations.append(p1[1])
                        else:
                            break
                else:
                    break
                
            for x in p2:
                if x in self.squares:
                    if self.square_pieces[x] != "":
                        if ((x == p2[2]) & (isinstance(self.square_pieces[x], pc.rook)) & (self.square_pieces[x].moved_yet == False)):
                          #This code won't execute unless everything else is good to castle
                          self.castle_moves[p2[1]] = [p2[0], p2[2]]
                          locations.append(p2[1])
                        else:
                            break
                else:
                    break
            return locations
       
        else:
            return []
    
    def causes_check(self, start, end):
        #checks if moving a piece to a certain square puts other player in check or puts themself in check
        #move will be prohibited if it puts the player themself in check'
        #returns 0 if move is illegal, 1 if it causes check on other player, -1 if it causes check
        # on self, 2 if normal move
        flag = 0
        if (self.square_pieces[start] == ""): 
            return flag
        else:
            if (self.square_pieces[end] != ""):
                if (self.square_pieces[start].color == self.square_pieces[end].color):
                    return flag
            temp = self.square_pieces[end]
            self.square_pieces[end] = self.square_pieces[start]
            self.square_pieces[start] = ""
            for x in self.find_movesp(self.square_pieces[end], end):
                #print(self.square_pieces[end], x)
                if isinstance(self.square_pieces[x], pc.king):
                    if (self.square_pieces[x].color != self.square_pieces[end].color):
                        flag = 1
                        break
            for z in self.square_pieces:
                if (self.square_pieces[z] != ""):
                    if (self.square_pieces[z].color != self.square_pieces[end].color):
                        for x in self.find_movesp(self.square_pieces[z], z):
                            if isinstance(self.square_pieces[x], pc.king):
                                if (self.square_pieces[x].color == self.square_pieces[end].color):
                                    flag = -1
                                    self.square_pieces[start] = self.square_pieces[end]
                                    self.square_pieces[end] = temp
                                    return flag
            self.square_pieces[start] = self.square_pieces[end]
            self.square_pieces[end] = temp
            if flag == 1:
                return flag
            else:
                flag = 2
                return flag
            
    def has_moves(self, col, p = False):
        result = False
        for x in self.square_pieces:
            if (self.square_pieces[x] != ""):
                if (self.square_pieces[x].color == col):
                    for y in self.find_movesp(self.square_pieces[x], x):
                        if (self.causes_check(x,y) != -1):
                            result = True
                            if (p):
                                print(self.turn + self.square_pieces[x].name + x + " to " + y)
                            return result
        return result
    
    def find_between(self, s1, s2):
        #returns list of all squares between s1 and s2
        if s1 == s2:
            return []
        if ((s1 not in self.squares )|(s2 not in self.squares)):
            return []
        x1, y1 = [ord(s1[0])-65, int(s1[1])]
        x2, y2 = [ord(s2[0])-65, int(s2[1])]
        sq = []
        if x1 == x2:
            if (abs(y2-y1) == 1):
                return []
            first = min(y1, y2)
            last = max(y1,y2)
            for k in range(1, last-first, 1):
                sq.append(chr(x1 + 65)+str(first+k))
        elif y1 == y2:
            if (abs(x2-x1) == 1):
                return []
            first = min(x1, x2)
            last = max(x1,x2)
            for k in range(1, last-first, 1):
                sq.append(chr(first + 65 + k)+str(y1))
        elif (abs(x1-x2) == abs(y1-y2)):
            if (abs(x2-x1) == 1):
                return []
            firstx = min(x1, x2)
            if firstx == x1:
                t = int(abs(y2-y1)/(y2-y1))
                for k in range(t, t*abs(x1-x2), t):
                    sq.append(chr(firstx + 65 + abs(k))+str(y1+k))
            else:
                t = int(abs(y1-y2)/(y1-y2))
                for k in range(t, t*abs(x1-x2), t):
                    sq.append(chr(firstx + 65 + abs(k))+str(y2+k))
        else:
            #This will execute if both are on the board, but not on the same row, column, or diagonal
            return [] 
        return sq

    def pseudomove(self, start, end):
        #returns 0 if no move, 1 if normal move, 2 if piece is upgraded
        #exactly the same as move but doesnt change pieces
        if (self.square_pieces[start] == ""): 
            return 0
        elif (self.square_pieces[start].color != self.turn):
            return 0
        else:
            if (self.square_pieces[end] != ""):
                if (self.square_pieces[start].color == self.square_pieces[end].color):
                    return 0
            if ((end == self.enpassant[4]) & (start in self.enpassant[1])):
                self.square_pieces[self.enpassant[2]] = ""
                self.enpassant = [False,[], "", "", ""]  
                #executes en passant if it possible, and resets ability
                
            self.square_pieces[end] = self.square_pieces[start]
            temp = self.turn
            self.turn = self.turnqueau.pop()
            self.turnqueau.insert(0, temp)
            self.square_pieces[start] = ""
            
            if (isinstance(self.square_pieces[end], pc.pawn) & (abs(int(end[1]) - int(start[1])) == 2)):
                #This block checks for en passant opportunities next turn, and logs them
                possible = [(chr(ord(end[0])-1) + end[1]), (chr(ord(end[0])+1) + end[1])]
                for x in possible:
                    if (x in self.square_pieces):
                        if (self.square_pieces[x] != ""):
                            if (isinstance(self.square_pieces[x], pc.pawn) & (self.square_pieces[x].color != self.square_pieces[end].color)):
                                self.enpassant[0] = True
                                self.enpassant[1].append(x)
                                self.enpassant[2] = end
                                self.enpassant[3] = start
            else:
                self.enpassant = [False,[], "", "", ""]   
            
            if ((isinstance(self.square_pieces[end], pc.king))):
                if self.teams_castle[self.square_pieces[end].color] == True:
                    if end in self.castle_moves:
                        self.square_pieces[self.castle_moves[end][0]] = self.square_pieces[self.castle_moves[end][1]]
                        #self.square_pieces[self.castle_moves[end][0]].moved_yet = True
                        self.square_pieces[self.castle_moves[end][1]] = ""
                    self.teams_castle[self.square_pieces[end].color] = False
                else:
                    return 1
            if ((self.square_pieces[end].upgrades == True) & (("1" in end) | ("8" in end))):
                bord = self
                cb.choosepiece(bord, start, end)
                return 2
            else:
                return 1                  
                    
def copyboard(b):
    if not isinstance(b, board):
        return 0
    else:
        b2 = board()
        b2.loadboard(b.square_pieces)
        b2.turn = copy.deepcopy(b.turn)
        b2.turnqueau = copy.deepcopy(b.turnqueau)
        b2.enpassant = copy.deepcopy(b.enpassant)
        b2.castle_moves = copy.deepcopy(b.castle_moves)
        return b2


