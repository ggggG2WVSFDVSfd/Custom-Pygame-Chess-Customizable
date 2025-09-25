# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 22:13:06 2022

@author: not bert
"""
import pygame
import pieces as pc
import engine as eng
import chessbot as cb


pygame.init()

canvas = pygame.display.set_mode([800,800])
  
# TITLE OF CANVAS

pygame.display.set_caption("Chess 2.0")

#Arrangements
#default = {"A1":pc.rook("art/wrook.png", b),"B1":pc.knight("art/wknight.png", b), "C1":pc.bishop("art/wbishop.png", b), "D1":pc.queen("art/wqueen.png", b), "E1":pc.king("art/whiteking.png", b), "F1":pc.bishop("art/wbishop.png", b), "G1":pc.knight("art/wknight.png", b), "H1":pc.rook("art/wrook.png", b), "A2":pc.pawn("art/wpawn.png", b),"B2":pc.pawn("art/wpawn.png", b), "C2":pc.pawn("art/wpawn.png", b), "D2":pc.pawn("art/wpawn.png", b), "E2":pc.pawn("art/wpawn.png", b), "F2":pc.pawn("art/wpawn.png", b), "G2":pc.pawn("art/wpawn.png", b), "H2":pc.pawn("art/wpawn.png", b), "A8":pc.rook("art/brook.png", b, col = "b"),"B8":pc.knight("art/bknight.png", b, col = "b"), "C8":pc.bishop("art/bbishop.png", b, col = "b"), "D8":pc.queen("art/bqueen.png", b, col = "b"), "E8":pc.king("art/bking.png", b, col = "b"), "F8":pc.bishop("art/bbishop.png", b, col = "b"), "G8":pc.knight("art/bknight.png", b, col = "b"), "H8":pc.rook("art/brook.png", b, col = "b"), "A7":pc.pawn("art/bpawn.png", b, col = "b"),"B7":pc.pawn("art/bpawn.png", b, col = "b"), "C7":pc.pawn("art/bpawn.png", b, col = "b"), "D7":pc.pawn("art/bpawn.png", b, col = "b"), "E7":pc.pawn("art/bpawn.png", b, col = "b"), "F7":pc.pawn("art/bpawn.png", b, col = "b"), "G7":pc.pawn("art/bpawn.png", b, col = "b"), "H7":pc.pawn("art/bpawn.png", b, col = "b")}
#enpass_test = {"A2":pc.pawn("art/wpawn.png", b), "B4":pc.pawn("art/bpawn.png", b, col = "b", my = True)}
#enpass_test2 = {"D5":pc.pawn("art/wpawn.png", b, my = True), "F5":pc.pawn("art/wpawn.png", b, my = True), "E7":pc.pawn("art/bpawn.png", b, col = "b")}
#castle_test = {"A1":pc.rook("art/wrook.png", b), "E1":pc.king("art/whiteking.png", b), "H1":pc.rook("art/wrook.png", b), "A2":pc.pawn("art/wpawn.png", b),"B2":pc.pawn("art/wpawn.png", b), "C2":pc.pawn("art/wpawn.png", b), "D2":pc.pawn("art/wpawn.png", b), "E2":pc.pawn("art/wpawn.png", b), "F2":pc.pawn("art/wpawn.png", b), "G2":pc.pawn("art/wpawn.png", b), "H2":pc.pawn("art/wpawn.png", b), "A8":pc.rook("art/brook.png", b, col = "b"), "E8":pc.king("art/bking.png", b, col = "b"), "H8":pc.rook("art/brook.png", b, col = "b"), "A7":pc.pawn("art/bpawn.png", b, col = "b"),"B7":pc.pawn("art/bpawn.png", b, col = "b"), "C7":pc.pawn("art/bpawn.png", b, col = "b"), "D7":pc.pawn("art/bpawn.png", b, col = "b"), "E7":pc.pawn("art/bpawn.png", b, col = "b"), "F7":pc.pawn("art/bpawn.png", b, col = "b"), "G7":pc.pawn("art/bpawn.png", b, col = "b"), "H7":pc.pawn("art/bpawn.png", b, col = "b")}
#shatranj = {"A1":pc.rook("art/wrook.png", b),"B1":pc.knight("art/wknight.png", b), "C1":pc.pil("art/wpil.png", b), "D1":pc.ferz("art/wqueen.png", b), "E1":pc.king("art/whiteking.png", b), "F1":pc.pil("art/wpil.png", b), "G1":pc.knight("art/wknight.png", b), "H1":pc.rook("art/wrook.png", b), "A2":pc.sarbaz("art/wpawn.png", b),"B2":pc.sarbaz("art/wpawn.png", b), "C2":pc.sarbaz("art/wpawn.png", b), "D2":pc.sarbaz("art/wpawn.png", b), "E2":pc.sarbaz("art/wpawn.png", b), "F2":pc.sarbaz("art/wpawn.png", b), "G2":pc.sarbaz("art/wpawn.png", b), "H2":pc.sarbaz("art/wpawn.png", b), "A8":pc.rook("art/brook.png", b, col = "b"),"B8":pc.knight("art/bknight.png", b, col = "b"), "C8":pc.pil("art/bpil.png", b, col = "b"), "D8":pc.ferz("art/bqueen.png", b, col = "b"), "E8":pc.king("art/bking.png", b, col = "b"), "F8":pc.pil("art/bpil.png", b, col = "b"), "G8":pc.knight("art/bknight.png", b, col = "b"), "H8":pc.rook("art/brook.png", b, col = "b"), "A7":pc.sarbaz("art/bpawn.png", b, col = "b"),"B7":pc.sarbaz("art/bpawn.png", b, col = "b"), "C7":pc.sarbaz("art/bpawn.png", b, col = "b"), "D7":pc.sarbaz("art/bpawn.png", b, col = "b"), "E7":pc.sarbaz("art/bpawn.png", b, col = "b"), "F7":pc.sarbaz("art/bpawn.png", b, col = "b"), "G7":pc.sarbaz("art/bpawn.png", b, col = "b"), "H7":pc.sarbaz("art/bpawn.png", b, col = "b")}
#checkmate_test = {"A1":pc.rook("art/wrook.png", b), "G1":pc.king("art/whiteking.png", b), "F2":pc.pawn("art/wpawn.png", b), "G2":pc.pawn("art/wpawn.png", b), "H2":pc.pawn("art/wpawn.png", b), "F7":pc.pawn("art/bpawn.png", b, col = "b"), "G7":pc.pawn("art/bpawn.png", b, col = "b"), "H7":pc.pawn("art/bpawn.png", b, col = "b"), "G8":pc.king("art/bking.png", b, col = "b"), "B8": pc.rook("art/brook.png", b, col = "b")}
#knook = {"A1":pc.rook("art/wrook.png", b),"B1":pc.knook("art/wknook.png", b), "C1":pc.bishop("art/wbishop.png", b), "D1":pc.queen("art/wqueen.png", b), "E1":pc.king("art/whiteking.png", b), "F1":pc.bishop("art/wbishop.png", b), "G1":pc.knight("art/wknight.png", b), "H1":pc.rook("art/wrook.png", b), "A2":pc.pawn("art/wpawn.png", b),"B2":pc.pawn("art/wpawn.png", b), "C2":pc.pawn("art/wpawn.png", b), "D2":pc.pawn("art/wpawn.png", b), "E2":pc.pawn("art/wpawn.png", b), "F2":pc.pawn("art/wpawn.png", b), "G2":pc.pawn("art/wpawn.png", b), "H2":pc.pawn("art/wpawn.png", b), "A8":pc.rook("art/brook.png", b, col = "b"),"B8":pc.knook("art/bknook.png", b, col = "b"), "C8":pc.bishop("art/bbishop.png", b, col = "b"), "D8":pc.queen("art/bqueen.png", b, col = "b"), "E8":pc.king("art/bking.png", b, col = "b"), "F8":pc.bishop("art/bbishop.png", b, col = "b"), "G8":pc.knight("art/bknight.png", b, col = "b"), "H8":pc.rook("art/brook.png", b, col = "b"), "A7":pc.pawn("art/bpawn.png", b, col = "b"),"B7":pc.pawn("art/bpawn.png", b, col = "b"), "C7":pc.pawn("art/bpawn.png", b, col = "b"), "D7":pc.pawn("art/bpawn.png", b, col = "b"), "E7":pc.pawn("art/bpawn.png", b, col = "b"), "F7":pc.pawn("art/bpawn.png", b, col = "b"), "G7":pc.pawn("art/bpawn.png", b, col = "b"), "H7":pc.pawn("art/bpawn.png", b, col = "b")}

def spv(canvas):
    #single player vanilla
    b = eng.board()
    #default = {"A1":pc.rook("art/wrook.png", b),"B1":pc.knight("art/wknight.png", b), "C1":pc.bishop("art/wbishop.png", b), "D1":pc.queen("art/wqueen.png", b), "E1":pc.king("art/whiteking.png", b), "F1":pc.bishop("art/wbishop.png", b), "G1":pc.knight("art/wknight.png", b), "H1":pc.rook("art/wrook.png", b), "A2":pc.pawn("art/wpawn.png", b),"B2":pc.pawn("art/wpawn.png", b), "C2":pc.pawn("art/wpawn.png", b), "D2":pc.pawn("art/wpawn.png", b), "E2":pc.pawn("art/wpawn.png", b), "F2":pc.pawn("art/wpawn.png", b), "G2":pc.pawn("art/wpawn.png", b), "H2":pc.pawn("art/wpawn.png", b), "A8":pc.rook("art/brook.png", b, col = "b"),"B8":pc.knight("art/bknight.png", b, col = "b"), "C8":pc.bishop("art/bbishop.png", b, col = "b"), "D8":pc.queen("art/bqueen.png", b, col = "b"), "E8":pc.king("art/bking.png", b, col = "b"), "F8":pc.bishop("art/bbishop.png", b, col = "b"), "G8":pc.knight("art/bknight.png", b, col = "b"), "H8":pc.rook("art/brook.png", b, col = "b"), "A7":pc.pawn("art/bpawn.png", b, col = "b"),"B7":pc.pawn("art/bpawn.png", b, col = "b"), "C7":pc.pawn("art/bpawn.png", b, col = "b"), "D7":pc.pawn("art/bpawn.png", b, col = "b"), "E7":pc.pawn("art/bpawn.png", b, col = "b"), "F7":pc.pawn("art/bpawn.png", b, col = "b"), "G7":pc.pawn("art/bpawn.png", b, col = "b"), "H7":pc.pawn("art/bpawn.png", b, col = "b")}
    #shatranj = {"A1":pc.rook("art/wrook.png", b),"B1":pc.knight("art/wknight.png", b), "C1":pc.pil("art/wpil.png", b), "D1":pc.ferz("art/wqueen.png", b), "E1":pc.king("art/whiteking.png", b), "F1":pc.pil("art/wpil.png", b), "G1":pc.knight("art/wknight.png", b), "H1":pc.rook("art/wrook.png", b), "A2":pc.sarbaz("art/wpawn.png", b),"B2":pc.sarbaz("art/wpawn.png", b), "C2":pc.sarbaz("art/wpawn.png", b), "D2":pc.sarbaz("art/wpawn.png", b), "E2":pc.sarbaz("art/wpawn.png", b), "F2":pc.sarbaz("art/wpawn.png", b), "G2":pc.sarbaz("art/wpawn.png", b), "H2":pc.sarbaz("art/wpawn.png", b), "A8":pc.rook("art/brook.png", b, col = "b"),"B8":pc.knight("art/bknight.png", b, col = "b"), "C8":pc.pil("art/bpil.png", b, col = "b"), "D8":pc.ferz("art/bqueen.png", b, col = "b"), "E8":pc.king("art/bking.png", b, col = "b"), "F8":pc.pil("art/bpil.png", b, col = "b"), "G8":pc.knight("art/bknight.png", b, col = "b"), "H8":pc.rook("art/brook.png", b, col = "b"), "A7":pc.sarbaz("art/bpawn.png", b, col = "b"),"B7":pc.sarbaz("art/bpawn.png", b, col = "b"), "C7":pc.sarbaz("art/bpawn.png", b, col = "b"), "D7":pc.sarbaz("art/bpawn.png", b, col = "b"), "E7":pc.sarbaz("art/bpawn.png", b, col = "b"), "F7":pc.sarbaz("art/bpawn.png", b, col = "b"), "G7":pc.sarbaz("art/bpawn.png", b, col = "b"), "H7":pc.sarbaz("art/bpawn.png", b, col = "b")}
    knook = {"A1":pc.rook("art/wrook.png", b),"B1":pc.knook("art/wknook.png", b), "C1":pc.bishop("art/wbishop.png", b), "D1":pc.queen("art/wqueen.png", b), "E1":pc.king("art/whiteking.png", b), "F1":pc.bishop("art/wbishop.png", b), "G1":pc.knook("art/wknook.png", b), "H1":pc.rook("art/wrook.png", b), "A2":pc.pawn("art/wpawn.png", b),"B2":pc.pawn("art/wpawn.png", b), "C2":pc.pawn("art/wpawn.png", b), "D2":pc.pawn("art/wpawn.png", b), "E2":pc.pawn("art/wpawn.png", b), "F2":pc.pawn("art/wpawn.png", b), "G2":pc.pawn("art/wpawn.png", b), "H2":pc.pawn("art/wpawn.png", b), "A8":pc.rook("art/brook.png", b, col = "b"),"B8":pc.knook("art/bknook.png", b, col = "b"), "C8":pc.bishop("art/bbishop.png", b, col = "b"), "D8":pc.queen("art/bqueen.png", b, col = "b"), "E8":pc.king("art/bking.png", b, col = "b"), "F8":pc.bishop("art/bbishop.png", b, col = "b"), "G8":pc.knight("art/bknight.png", b, col = "b"), "H8":pc.rook("art/brook.png", b, col = "b"), "A7":pc.pawn("art/bpawn.png", b, col = "b"),"B7":pc.pawn("art/bpawn.png", b, col = "b"), "C7":pc.pawn("art/bpawn.png", b, col = "b"), "D7":pc.pawn("art/bpawn.png", b, col = "b"), "E7":pc.pawn("art/bpawn.png", b, col = "b"), "F7":pc.pawn("art/bpawn.png", b, col = "b"), "G7":pc.pawn("art/bpawn.png", b, col = "b"), "H7":pc.pawn("art/bpawn.png", b, col = "b")}
    b.loadboard(knook)
    b.drawboard(canvas)
    ready = True
    checkmate = False
    exit = False
    while not exit:
        pygame.display.flip()
        events = pygame.event.get()
        for event in events:
            if ((not ready) & (not checkmate)):
                pygame.time.wait(3000)
                ready = True
            if event.type == pygame.QUIT:
                exit = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                start_square = pygame.mouse.get_pos()
            elif event.type == pygame.MOUSEBUTTONUP:
                end_square = pygame.mouse.get_pos()
                if (ready):
                    ready = False
                    start = ""
                    end = ""
                    for x in b.squares:
                        if ((b.squares[x][0] < start_square[0] < b.squares[x][1]) & (b.squares[x][2] < start_square[1] < b.squares[x][3])):
                            start = x
                        if ((b.squares[x][0] < end_square[0] < b.squares[x][1]) & (b.squares[x][2] < end_square[1] < b.squares[x][3])):
                            end = x
                    if ((start != "") & (end != "") & (start != end)):
                        if (b.checklegal(start, end) == True):
                            if (b.has_moves(b.turn) == False):
                                print("Stalemate!")
                                ready = False
                            else:
                                if (b.causes_check(start, end) == -1):
                                    if (b.check == True):
                                        print("you need to get out of check!")
                                        #print(b.has_moves(b.turn))
                                    else:
                                        print("You can't put yourself into check!")
                                    ready = True
                                   
                                else:
                                    c = b.causes_check(start, end)
                                    if (b.move(start, end) == 2):
                                        b.square_pieces[start] = b.square_pieces[end]
                                        b.square_pieces[end] = ""
                                        c = b.causes_check(start, end)
                                        #print(c)
                                        b.square_pieces[end] = b.square_pieces[start]
                                        b.square_pieces[start] = ""
                                        #This if statement and code is needed to check for check
                                        #or checkmate after a pawn is upgraded in the final row
                                   
                                    if (c == 1):
                                        if (b.has_moves(b.turn) == False):
                                            b.drawboard(canvas)
                                            pygame.display.flip()
                                            print("Checkmate!")
                                            ready = False
                                            b.check = True
                                            checkmate = True
                                        else:
                                            print("Player " + b.turn + " Now in check")
                                            b.drawboard(canvas)
                                            pygame.display.flip()
                                            b.check = True
                                            ready = True
                                    else:
                                        b.check = False
                                        b.drawboard(canvas)
                                        pygame.display.flip()
                                        ready = True
                                        
                    else:
                        ready = True
        
    pygame.quit()

def spvAI(canvas):
    #single player vanilla
    b = eng.board()
    b.AIgame = True
    bt = cb.playerbot(lev = 2)
    b.AIcolor = bt.color
    #enpass_test2 = {"D5":pc.pawn("art/wpawn.png", b, my = True), "F5":pc.pawn("art/wpawn.png", b, my = True), "E7":pc.pawn("art/bpawn.png", b, col = "b")}
    default = {"A1":pc.rook("art/wrook.png", b),"B1":pc.knight("art/wknight.png", b), "C1":pc.bishop("art/wbishop.png", b), "D1":pc.queen("art/wqueen.png", b), "E1":pc.king("art/whiteking.png", b), "F1":pc.bishop("art/wbishop.png", b), "G1":pc.knight("art/wknight.png", b), "H1":pc.rook("art/wrook.png", b), "A2":pc.pawn("art/wpawn.png", b),"B2":pc.pawn("art/wpawn.png", b), "C2":pc.pawn("art/wpawn.png", b), "D2":pc.pawn("art/wpawn.png", b), "E2":pc.pawn("art/wpawn.png", b), "F2":pc.pawn("art/wpawn.png", b), "G2":pc.pawn("art/wpawn.png", b), "H2":pc.pawn("art/wpawn.png", b), "A8":pc.rook("art/brook.png", b, col = "b"),"B8":pc.knight("art/bknight.png", b, col = "b"), "C8":pc.bishop("art/bbishop.png", b, col = "b"), "D8":pc.queen("art/bqueen.png", b, col = "b"), "E8":pc.king("art/bking.png", b, col = "b"), "F8":pc.bishop("art/bbishop.png", b, col = "b"), "G8":pc.knight("art/bknight.png", b, col = "b"), "H8":pc.rook("art/brook.png", b, col = "b"), "A7":pc.pawn("art/bpawn.png", b, col = "b"),"B7":pc.pawn("art/bpawn.png", b, col = "b"), "C7":pc.pawn("art/bpawn.png", b, col = "b"), "D7":pc.pawn("art/bpawn.png", b, col = "b"), "E7":pc.pawn("art/bpawn.png", b, col = "b"), "F7":pc.pawn("art/bpawn.png", b, col = "b"), "G7":pc.pawn("art/bpawn.png", b, col = "b"), "H7":pc.pawn("art/bpawn.png", b, col = "b")}
    #knook = {"A1":pc.rook("art/wrook.png", b),"B1":pc.knook("art/wknook.png", b), "C1":pc.bishop("art/wbishop.png", b), "D1":pc.queen("art/wqueen.png", b), "E1":pc.king("art/whiteking.png", b), "F1":pc.bishop("art/wbishop.png", b), "G1":pc.knook("art/wknook.png", b), "H1":pc.rook("art/wrook.png", b), "A2":pc.pawn("art/wpawn.png", b),"B2":pc.pawn("art/wpawn.png", b), "C2":pc.pawn("art/wpawn.png", b), "D2":pc.pawn("art/wpawn.png", b), "E2":pc.pawn("art/wpawn.png", b), "F2":pc.pawn("art/wpawn.png", b), "G2":pc.pawn("art/wpawn.png", b), "H2":pc.pawn("art/wpawn.png", b), "A8":pc.rook("art/brook.png", b, col = "b"),"B8":pc.knook("art/bknook.png", b, col = "b"), "C8":pc.bishop("art/bbishop.png", b, col = "b"), "D8":pc.queen("art/bqueen.png", b, col = "b"), "E8":pc.king("art/bking.png", b, col = "b"), "F8":pc.bishop("art/bbishop.png", b, col = "b"), "G8":pc.knight("art/bknight.png", b, col = "b"), "H8":pc.rook("art/brook.png", b, col = "b"), "A7":pc.pawn("art/bpawn.png", b, col = "b"),"B7":pc.pawn("art/bpawn.png", b, col = "b"), "C7":pc.pawn("art/bpawn.png", b, col = "b"), "D7":pc.pawn("art/bpawn.png", b, col = "b"), "E7":pc.pawn("art/bpawn.png", b, col = "b"), "F7":pc.pawn("art/bpawn.png", b, col = "b"), "G7":pc.pawn("art/bpawn.png", b, col = "b"), "H7":pc.pawn("art/bpawn.png", b, col = "b")}
    #upgrade_pawn_test = {"E2":pc.pawn("art/wpawn.png", b), "G2":pc.pawn("art/wpawn.png", b), "F3":pc.pawn("art/wpawn.png", b), "G3":pc.pawn("art/wpawn.png", b), "D4":pc.bishop("art/wbishop.png", b), "F1":pc.rook("art/wrook.png", b),"F2":pc.king("art/whiteking.png", b), "E1":pc.bishop("art/wbishop.png", b), "G1":pc.bishop("art/wbishop.png", b),"E8":pc.king("art/bking.png", b, col = "b"), "H2":pc.pawn("art/bpawn.png", b, col = "b", my = True)}
    #shatranj = {"A1":pc.rook("art/wrook.png", b),"B1":pc.knight("art/wknight.png", b), "C1":pc.pil("art/wpil.png", b), "D1":pc.ferz("art/wqueen.png", b), "E1":pc.king("art/whiteking.png", b), "F1":pc.pil("art/wpil.png", b), "G1":pc.knight("art/wknight.png", b), "H1":pc.rook("art/wrook.png", b), "A2":pc.sarbaz("art/wpawn.png", b),"B2":pc.sarbaz("art/wpawn.png", b), "C2":pc.sarbaz("art/wpawn.png", b), "D2":pc.sarbaz("art/wpawn.png", b), "E2":pc.sarbaz("art/wpawn.png", b), "F2":pc.sarbaz("art/wpawn.png", b), "G2":pc.sarbaz("art/wpawn.png", b), "H2":pc.sarbaz("art/wpawn.png", b), "A8":pc.rook("art/brook.png", b, col = "b"),"B8":pc.knight("art/bknight.png", b, col = "b"), "C8":pc.pil("art/bpil.png", b, col = "b"), "D8":pc.ferz("art/bqueen.png", b, col = "b"), "E8":pc.king("art/bking.png", b, col = "b"), "F8":pc.pil("art/bpil.png", b, col = "b"), "G8":pc.knight("art/bknight.png", b, col = "b"), "H8":pc.rook("art/brook.png", b, col = "b"), "A7":pc.sarbaz("art/bpawn.png", b, col = "b"),"B7":pc.sarbaz("art/bpawn.png", b, col = "b"), "C7":pc.sarbaz("art/bpawn.png", b, col = "b"), "D7":pc.sarbaz("art/bpawn.png", b, col = "b"), "E7":pc.sarbaz("art/bpawn.png", b, col = "b"), "F7":pc.sarbaz("art/bpawn.png", b, col = "b"), "G7":pc.sarbaz("art/bpawn.png", b, col = "b"), "H7":pc.sarbaz("art/bpawn.png", b, col = "b")}
    #checkmate_test = {"A1":pc.rook("art/wrook.png", b), "G1":pc.king("art/whiteking.png", b), "F2":pc.pawn("art/wpawn.png", b), "G2":pc.pawn("art/wpawn.png", b), "H2":pc.pawn("art/wpawn.png", b), "F7":pc.pawn("art/bpawn.png", b, col = "b"), "G7":pc.pawn("art/bpawn.png", b, col = "b"), "H7":pc.pawn("art/bpawn.png", b, col = "b"), "G8":pc.king("art/bking.png", b, col = "b"), "B8": pc.rook("art/brook.png", b, col = "b")}
    b.loadboard(default)
    b.drawboard(canvas)
    ready = True
    checkmate = False
    exit = False
    while not exit:
        pygame.display.flip()
        events = pygame.event.get()
        for event in events:
            if ((not ready) & (not checkmate)):
                pygame.time.wait(3000)
                ready = True
            if event.type == pygame.QUIT:
                exit = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                start_square = pygame.mouse.get_pos()
            elif event.type == pygame.MOUSEBUTTONUP:
                end_square = pygame.mouse.get_pos()
                #print(b.turn)
                if (ready & (b.turn != bt.color)):
                    ready = False
                    start = ""
                    end = ""
                    for x in b.squares:
                        if ((b.squares[x][0] < start_square[0] < b.squares[x][1]) & (b.squares[x][2] < start_square[1] < b.squares[x][3])):
                            start = x
                        if ((b.squares[x][0] < end_square[0] < b.squares[x][1]) & (b.squares[x][2] < end_square[1] < b.squares[x][3])):
                            end = x
                    if ((start != "") & (end != "") & (start != end)):
                        if (b.checklegal(start, end) == True):
                            if (b.has_moves(b.turn) == False):
                                print("Stalemate!")
                                ready = False
                            else:
                                if (b.causes_check(start, end) == -1):
                                    if (b.check == True):
                                        print("you need to get out of check!")
                                        #print(b.has_moves(b.turn))
                                    else:
                                        print("You can't put yourself into check!")
                                    ready = True
                                   
                                else:
                                    c = b.causes_check(start, end)
                                    if (b.move(start, end) == 2):
                                        b.square_pieces[start] = b.square_pieces[end]
                                        b.square_pieces[end] = ""
                                        c = b.causes_check(start, end)
                                        #print(c)
                                        b.square_pieces[end] = b.square_pieces[start]
                                        b.square_pieces[start] = ""
                                        #This if statement and code is needed to check for check
                                        #or checkmate after a pawn is upgraded in the final row
                                    if (c == 1):
                                        if (b.has_moves(b.turn) == False):
                                            b.drawboard(canvas)
                                            pygame.display.flip()
                                            print("Checkmate!")
                                            ready = False
                                            b.check = True
                                            checkmate = True
                                        else:
                                            print("Player " + b.turn + " Now in check")
                                            b.drawboard(canvas)
                                            pygame.display.flip()
                                            b.check = True
                                            m = bt.AImove(b)
                                            #print(m)
                                            #print(b.turn)
                                            b.move(m[0], m[1])
                                            b.drawboard(canvas)
                                            pygame.display.flip()
                                            if bt.starts_check == True:
                                                if (b.has_moves(b.turn) == False):
                                                    print("Checkmate!")
                                                    checkmate = True
                                                    ready = False
                                                else:
                                                    print("Player " + b.turn + " Now in check")
                                                    b.check = True
                                                    ready = True
                                                    cb.playerbot.starts_check == False
                                            else:
                                                b.check = False
                                                ready = True
                                    else:
                                        b.check = False
                                        b.drawboard(canvas)
                                        pygame.display.flip()
                                        m = bt.AImove(b)
                                        #print(m)
                                        #print(b.turn)
                                        b.move(m[0], m[1])
                                        b.drawboard(canvas)
                                        pygame.display.flip()
                                        if bt.starts_check == True:
                                            if (b.has_moves(b.turn) == False):
                                                print("Checkmate!")
                                                checkmate = True
                                                ready = False
                                            else:
                                                print("Player " + b.turn + " Now in check")
                                                b.check = True
                                                ready = True
                                                cb.playerbot.starts_check == False
                                        else:
                                            b.check = False
                                            ready = True
                                        
                    else:
                        ready = True
        
    pygame.quit()
    

exit = False
playing = False
AI =  False
while not (exit | playing):
    button1 = pygame.draw.rect(canvas, [255,0,0], pygame.Rect(200,200,400,100))
    font = pygame.font.SysFont(None, 24)
    button1t = font.render("Start singleplayer game", True, (255, 255, 255))
    canvas.blit(button1t, (200,200,400,100))
        
    button2 = pygame.draw.rect(canvas, [255,0,0], pygame.Rect(200,350,400,100))
    button2t = font.render("Start AI game", True, (255, 255, 255))
    canvas.blit(button2t, (200,350,400,100))
            
    pygame.display.update([button1, button2])
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONUP:
            clickplace = pygame.mouse.get_pos()
            if (200 <= clickplace[0] <= 600) & (200 <= clickplace[1] <= 300):
                playing = True
                canvas.fill([0,0,0])
            elif (200 <= clickplace[0] <= 600) & (350 <= clickplace[1] <= 450):
                playing = True
                AI = True
                canvas.fill([0,0,0])

if (playing):
    if AI:
        spvAI(canvas)
    else:  
        spv(canvas)
pygame.quit()

