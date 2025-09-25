# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 19:38:57 2022

@author: not bert
"""
import pieces as pc
import engine as eng
import copy
#this is code for AI player


class playerbot:
    starts_check = False
    def __init__ (self, col = "b", lev = 5):
        self.color = col
        self.level = lev
        if (lev > 10) | (lev < 1):
            self.level = 10

    
    def AImove(self, board):
        choice = []
        possible = self.findall(board)
        if possible == []:
            return 0
        else:
            if self.level == 2:
                best = self.lookahead(board, possible)
                choice = [best[0], best[1]]
                
            elif self.level == 3:
                best = self.lookahead3(board, possible)
                choice = [best[0], best[1]]
            elif self.level >= 4:
                best = self.lookahead5(board, possible)
                choice = [best[0], best[1]]
            else:
                possible = sorted(possible, key=lambda x: x[2])
                possible.reverse()
                choice = [possible[0][0], possible[0][1]]  
        return choice
   
    def findall (self, board, c = "b"):
        #finds all legal moves for a given team on a given board
        results = []
        for x in board.square_pieces:
            if (board.square_pieces[x] != ""):
                if (board.square_pieces[x].color == c):
                    for y in board.find_movesp(board.square_pieces[x], x):
                        if board.check == True:
                            t = board.causes_check(x,y)
                            if (t == -1): 
                                continue
                        if (board.square_pieces[y] != ""):
                            v = board.square_pieces[y].value
                        elif (isinstance(board.square_pieces[x], pc.king)):
                            if (y in ["C1", "C8", "G1", "G8"]):
                                v = 2
                                #incentivizes castling
                            elif (int(y[1]) <= 7 | int(y[1]) >= 2):
                                v = -1
                            elif (int(y[1]) == 8 | int(y[1]) == 1):
                                v = .1
                            else:
                                v = 0
                            #king shouldnt be incentivized to go to middle of board!
                        elif (isinstance(board.square_pieces[x], pc.pawn)):
                            if(int(y[1]) == 7 | int(y[1]) == 2):
                                v = 2
                            if(int(y[1]) == 8 | int(y[1]) == 1):
                                v = 9
                                print("yeee")
                            else:
                                if y in ["E4", "E5", "D4", "D5"]:
                                    v = .15
                                elif y in ["F4", "F5", "F6", "F3", "C4", "C5", "C6", "C3", "D3", "E3", "D6", "E6"]:
                                    v = .1
                                elif y in ["G3" "G4", "G5", "G6", "B3" "B4", "B5", "B6"]:
                                    v = .05
                                    #the squares that aren't on the ends or the edges
                                else:
                                    v = 0
                                    
                        else:
                            if y in ["E4", "E5", "D4", "D5"]:
                                v = .15
                            elif y in ["F4", "F5", "F6", "F3", "C4", "C5", "C6", "C3", "D3", "E3", "D6", "E6"]:
                                v = .1
                            elif y in ["G2", "G3" "G4", "G5", "G6", "G7", "B2", "B3" "B4", "B5", "B6", "B7", "F7","E7", "D7", "C7", "F2","E2", "D2", "C2"]:
                                v = .05
                            else:
                                v = 0
                        results.append([x,y, v])
        #print(results)
        return results
    
    def lookahead(self, board, moves):
        #allows AI to anticipate future moves
        #moves is a list of possible moves for the player whose turn it is, the output of the findall function
        #returns best possible move as a response to another move
        #print(str(moves) + "\n")
        if moves == []:
            return []
        results = copy.deepcopy(moves)
        if board.turn == board.square_pieces[moves[0][0]].color:
            places = self.teampositions(board, c = board.turnqueau[0])
            for x in range(0,len(moves),1): 
                b2 = eng.copyboard(board)
                b2.pseudomove(moves[x][0], moves[x][1])
                opponentmoves = self.findall2(b2, places, c = b2.turn)
                if opponentmoves == []:
                    if board.causes_check(moves[x][0], moves[x][1]):
                        results[x][2] = 100
                        return results
                    else:
                        continue
                else:
                    results[x][2] = results[x][2] -  max([q[2] for q in opponentmoves])
            #print(results)
            results = sorted(results, key=lambda x: x[2])
            results.reverse()
            for z in range(0, len(results), 1):
                #chooses the best move that does not leave AI in check
                t = board.causes_check(results[z][0], results[z][1])
                if t == -1:
                    continue
                elif t == 1:
                    playerbot.starts_check = True
                    return(results[z])
                else:
                    return(results[z])
        else:
            return []
        
    
        
    def findall2 (self, board, squares, c = "b", highest = 9):
        #finds all legal moves for a given team on a given board
        #this is the optimized version for use in look_ahead, ret
        results = []
        for x in squares:
            if (board.square_pieces[x] != ""):
                if (board.square_pieces[x].color == c):
                    for y in board.find_movesp(board.square_pieces[x], x):
                        if board.check == True:
                            t = board.causes_check(x,y)
                            if (t == -1): 
                                continue
                        if (board.square_pieces[y] != ""):
                            v = board.square_pieces[y].value
                            # if v == highest:
                            #     results.append([x,y,v])
                            #     return results
                        elif (isinstance(board.square_pieces[x], pc.king)):
                            if (y in ["C1", "C8", "G1", "G8"]):
                                v = 2
                                #incentivizes castling
                            elif (int(y[1]) <= 7 | int(y[1]) >= 2):
                                v = -1
                            elif (int(y[1]) == 8 | int(y[1]) == 1):
                                v = .1
                            else:
                                v = 0
                            #king shouldnt be incentivized to go to middle of board!
                        elif (isinstance(board.square_pieces[x], pc.pawn)):
                            if(int(y[1]) == 7 | int(y[1]) == 2):
                                v = 2
                                print("yrrrr")
                            if(int(y[1]) == 8 | int(y[1]) == 1):
                                v = 9
                                print("yeeee")
                            else:
                                if y in ["E4", "E5", "D4", "D5"]:
                                    v = .15
                                elif y in ["F4", "F5", "F6", "F3", "C4", "C5", "C6", "C3", "D3", "E3", "D6", "E6"]:
                                    v = .1
                                elif y in ["G3" "G4", "G5", "G6", "B3" "B4", "B5", "B6"]:
                                    v = .05
                                    #the squares that aren't on the ends or the edges
                                else:
                                    v = 0
                                    
                        else:
                            if y in ["E4", "E5", "D4", "D5"]:
                                v = .15
                            elif y in ["F4", "F5", "F6", "F3", "C4", "C5", "C6", "C3", "D3", "E3", "D6", "E6"]:
                                v = .1
                            elif y in ["G2", "G3" "G4", "G5", "G6", "G7", "B2", "B3" "B4", "B5", "B6", "B7", "F7","E7", "D7", "C7", "F2","E2", "D2", "C2"]:
                                v = .05
                            else:
                                v = 0
                        results.append([x,y, v])
        #print(results)
        return results
    
    def teampositions(self, board, c = "w"):
        positions = []
        highest = 0
        for x in board.square_pieces:
            if (board.square_pieces[x] != ""):
                if (board.square_pieces[x].color == c):
                    positions.append(x)
        return positions
    
    def Top5(self, moveset):
        if len(moveset) <= 8:
            return moveset
        else:
            results = sorted(moveset, key=lambda x: x[2])
            results.reverse()
            results = results[:8]
            return results
        
    def lookahead3(self, board, moves):
        #allows AI to anticipate future moves
        #moves is a list of possible moves for the player whose turn it is, the output of the findall function
        #returns best possible move as a response to another move
        #print(str(moves) + "\n")
        if moves == []:
            return []
        results = copy.deepcopy(moves)
        if board.turn == board.square_pieces[moves[0][0]].color:
            places = self.teampositions(board, c = board.turnqueau[0])
            myplaces = self.teampositions(board, c = board.turn)
            for x in range(0,len(moves),1): 
                b2 = eng.copyboard(board)
                b2.pseudomove(moves[x][0], moves[x][1])
                opponentmoves = self.findall2(b2, places, c = b2.turn)
                if opponentmoves == []:
                    if board.causes_check(moves[x][0], moves[x][1]):
                        results[x][2] = 100
                        return results
                    else:
                        continue
                else:
                    myplacesc = copy.deepcopy(myplaces)
                    myplacesc.append(moves[x][1])
                    for z in range(0,len(opponentmoves),1):
                        b3 = eng.copyboard(b2)
                        b3.pseudomove(opponentmoves[z][0], opponentmoves[z][1])
                        mymoves2 = self.findall2(b3, myplacesc, c = b3.turn)
                        if mymoves2 == []:
                            continue
                        opponentmoves[z][2] = opponentmoves[z][2] - max([q[2] for q in mymoves2])
                    results[x][2] = results[x][2] -  max([q[2] for q in opponentmoves])
            #print(results)
            results = sorted(results, key=lambda x: x[2])
            results.reverse()
            #print(results[:4])
            for z in range(0, len(results), 1):
                #chooses the best move that does not leave AI in check
                t = board.causes_check(results[z][0], results[z][1])
                if t == -1:
                    continue
                elif t == 1:
                    playerbot.starts_check = True
                    return(results[z])
                else:
                    return(results[z])
        else:
            return []
        
    def lookahead4(self, board, moves):
      #allows AI to anticipate future moves
      #moves is a list of possible moves for the player whose turn it is, the output of the findall function
      #returns best possible move as a response to another move
      #print(str(moves) + "\n")
      if moves == []:
          return []
      results = copy.deepcopy(moves)
      if board.turn == board.square_pieces[moves[0][0]].color:
          places = self.teampositions(board, c = board.turnqueau[0])
          myplaces = self.teampositions(board, c = board.turn)
          for x in range(0,len(moves),1): 
              b2 = eng.copyboard(board)
              b2.pseudomove(moves[x][0], moves[x][1])
              opponentmoves = self.findall2(b2, places, c = b2.turn)
              if opponentmoves == []:
                  if board.causes_check(moves[x][0], moves[x][1]):
                      results[x][2] = 100
                      return results[x]
                  else:
                      continue
              else:
                  myplacesc = copy.deepcopy(myplaces)
                  myplacesc.append(moves[x][1])
                  for z in range(0,len(opponentmoves),1):
                      if (results[x][2] - opponentmoves[z][2]) < -3:
                          continue
                      b3 = eng.copyboard(b2)
                      b3.pseudomove(opponentmoves[z][0], opponentmoves[z][1])
                      mymoves2 = self.findall2(b3, myplacesc, c = b3.turn)
                      if mymoves2 == []:
                          continue
                      else:
                          places2 = copy.deepcopy(places)
                          places2.append(opponentmoves[z][1])
                          mymoves2 = self.Top5(mymoves2)
                          for w in range(0, len(mymoves2), 1):
                              if (results[x][2] - opponentmoves[z][2] + mymoves2[w][2])  < 0:
                                  continue
                              b4 = eng.copyboard(b3)
                              b4.pseudomove(mymoves2[w][0], mymoves2[w][1])
                              opponentmoves2 = self.findall2(b4, places2, c = b4.turn)
                              if opponentmoves2 == []:
                                  if b4.causes_check(mymoves2[x][0], mymoves2[x][1]):
                                      results[x][2] = 100
                                      return results[x]
                                  else:
                                      continue
                              else:
                                  mymoves2[w][2] =  mymoves2[w][2] - max([q[2] for q in opponentmoves2])
                          opponentmoves[z][2] = opponentmoves[z][2] - max([q[2] for q in mymoves2])
                  results[x][2] = results[x][2] -  max([q[2] for q in opponentmoves])
                  if (results[x][2] >= 3):
                      t = board.causes_check(results[x][0], results[x][1])
                      if t == -1:
                          continue
                      elif t == 1:
                          self.starts_check = True
                          return(results[x])
                      else:
                          return(results[x])
          #print(results)
          results = sorted(results, key=lambda x: x[2])
          results.reverse()
          #print(results[:4])
          for z in range(0, len(results), 1):
              #chooses the best move that does not leave AI in check
              t = board.causes_check(results[z][0], results[z][1])
              if t == -1:
                  continue
              elif t == 1:
                  playerbot.starts_check = True
                  return(results[z])
              else:
                  return(results[z])
      else:
          return []

    def lookahead5(self, board, moves):
      #allows AI to anticipate future moves
      #moves is a list of possible moves for the player whose turn it is, the output of the findall function
      #returns best possible move as a response to another move
      #print(str(moves) + "\n")
      if moves == []:
          return []
      results = copy.deepcopy(moves)
      if board.turn == board.square_pieces[moves[0][0]].color:
          places = self.teampositions(board, c = board.turnqueau[0])
          myplaces = self.teampositions(board, c = board.turn)
          for x in range(0,len(moves),1): 
              b2 = eng.copyboard(board)
              b2.pseudomove(moves[x][0], moves[x][1])
              opponentmoves = self.findall2(b2, places, c = b2.turn)
              if opponentmoves == []:
                  if board.causes_check(moves[x][0], moves[x][1]):
                      results[x][2] = 100
                      return results[x]
                  else:
                      continue
              else:
                  results[x].append(opponentmoves)
                  results[x][2] = results[x][2] -  max([x[2] for x in opponentmoves])
          #print(results)
          results = self.Top5(results)
          for x in range(0,len(results),1):
              if results[x][3] == []:
                  continue
              b2 = eng.copyboard(board)
              b2.pseudomove(results[x][0], results[x][1])
              myplacesc = copy.deepcopy(myplaces)
              myplacesc.append(results[x][1])
              for z in range(0,len(results[x][3]),1):
                  b3 = eng.copyboard(b2)
                  b3.pseudomove(results[x][3][z][0], results[x][3][z][1])
                  mymoves2 = self.findall2(b3, myplacesc, c = b3.turn)
                  if mymoves2 == []:
                      continue
                  else:
                      places2 = copy.deepcopy(places)
                      places2.append(results[x][3][z][1])
                      mymoves2 = self.Top5(mymoves2)
                      for w in range(0, len(mymoves2), 1):
                          b4 = eng.copyboard(b3)
                          b4.pseudomove(mymoves2[w][0], mymoves2[w][1])
                          opponentmoves2 = self.findall2(b4, places2, c = b4.turn)
                          if opponentmoves2 == []:
                              if b4.causes_check(mymoves2[x][0], mymoves2[x][1]):
                                  results[x][2] = 100
                                  return results[x][:3]
                              else:
                                  continue
                          else:
                              mymoves2[w][2] =  mymoves2[w][2] - max([q[2] for q in opponentmoves2])
                      results[x][3][z][2] = results[x][3][z][2] - max([q[2] for q in mymoves2])
              results[x][2] = results[x][2] -  max([q[2] for q in opponentmoves])
              if (results[x][2] >= 5):
                  t = board.causes_check(results[x][0], results[x][1])
                  if t == -1:
                      continue
                  elif t == 1:
                      self.starts_check = True
                      return(results[x][:3])
                  else:
                      return(results[x][:3])
          for z in range(0, len(results), 1):
              #chooses the best move that does not leave AI in check
              t = board.causes_check(results[z][0][:3], results[z][1][:3])
              if t == -1:
                  continue
              elif t == 1:
                  playerbot.starts_check = True
                  return(results[z][:3])
              else:
                  return(results[z][:3])
      else:
          return []
        
def choosepiece(board, start, end, real = False):
    #so AI can choose what to upgrade pawn to at end of board
    #return 0 if unsuccessful, 1 if successfully chose piece
    #This is only called at the end of move or pseudomove, when the turn counter has already changed
    #works by checking if a knight causes checkmate, and if so, chooses knight. Then checks if queen causes stalemate. 
    #IF she doesn't, the player upgrades to a queen
    #Real runs if this is for a real move, as opposed to a simulated move. If so,
    #It changes the game global variable for winning
    c = board.turnqueau[-1]
    other = board.turn
    b2 = eng.copyboard(board)
    b2.square_pieces[start] = pc.knight("art/bknight.png", b2, col = c)
    b2.square_pieces[end] = ""
    t = b2.causes_check(start, end)
    if t == 1:
        b2.turn = c
        b2.pseudomove(start, end)
        if b2.has_moves(other) == False:
            board.square_pieces[end] = pc.knight(("art/" + c + "knight.png"), b2, col = c)
            if real == True:
                playerbot.starts_check = True
            return 1
    t2 = t
    del b2   
    b2 = eng.copyboard(board)
    b2.square_pieces[start] = pc.queen("art/bknight.png", b2, col = c)
    b2.square_pieces[end] = ""
    t = b2.causes_check(start, end)
    if t == 2:
        b2.turn = c
        b2.pseudomove(start, end)
        if b2.has_moves(other) == True:
            board.square_pieces[end] = pc.queen(("art/" + c + "queen.png"), b2, col = c)
            return 1
        else:
            #This block is executed if ugrading to a queen would cause stalemate
            del b2
            b2 = eng.copyboard(board)
            b2.square_pieces[start] = pc.rook("art/bknight.png", b2, col = c)
            b2.square_pieces[end] = ""
            t = b2.causes_check(start, end)
            if t == 2:
                b2.turn = c
                b2.pseudomove(start, end)
                if b2.has_moves(other) == True:
                    board.square_pieces[end] = pc.rook(("art/" + c + "rook.png"), b2, col = c)
                    return 1
                else:
                    #This block is executed if upgrading to a queen or rook would cause stalemate
                    del b2
                    b2 = eng.copyboard(board)
                    b2.square_pieces[start] = pc.bishop(("art/" + c + "bishop.png"), b2, col = c)
                    b2.square_pieces[end] = ""
                    t = b2.causes_check(start, end)
                    if t == 2:
                        b2.turn = c
                        b2.pseudomove(start, end)
                        if b2.has_moves(other) == True:
                            board.square_pieces[end] = pc.bishop(("art/" + c + "bishop.png"), b2, col = c)
                            return 1
                        else:
                            #This block is executed if upgrading to a queen, rook or bishop causes stalemate
                            #upgrades automatically to knight
                            board.square_pieces[end] = pc.knight(("art/" + c + "knight.png"), b2, col = c)
                            del b2
                            if t2 == 1:
                                playerbot.starts_check = True
                            return 1
                    elif t == 1:
                        board.square_pieces[end] = pc.bishop(("art/" + c + "bishop.png"), b2, col = c)
                        if real == True:
                            playerbot.starts_check = True
                        return 1
                    else:
                        board.square_pieces[end] = pc.bishop(("art/" + c + "bishop.png"), b2, col = c)
                        return 1
            elif t == 1:
                board.square_pieces[end] = pc.rook(("art/" + c + "queen.png"), b2, col = c)
                if real == True:
                    playerbot.starts_check = True
                return 1
            else:       
                board.square_pieces[end] = pc.rook(("art/" + c + "queen.png"), b2, col = c)
                return 1
    elif t == 1:
        board.square_pieces[end] = pc.queen(("art/" + c + "queen.png"), b2, col = c)
        if real == True:
            playerbot.starts_check = True
        return 1
    else:       
        board.square_pieces[end] = pc.queen(("art/" + c + "queen.png"), b2, col = c)
        return 1



