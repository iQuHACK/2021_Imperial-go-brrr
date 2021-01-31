#!/usr/bin/env python
# coding: utf-8

# # Poker Game

# ## Packages

# In[3]:


get_ipython().system('pip install qiskit')
get_ipython().system('pip install qiskit_ionq_provider-0.0.1.dev0+45bd6b1-py3-none-any.whl')


# In[1]:


import tkinter as tk                # python 3
from tkinter import font as tkfont  # python 3
import gates as gt
import circuit as ct
import random

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


# ## Main functions

# Main functions for the frontend are in this section.

# In[2]:


class player:
    def __init__(self,hand,points):
        self.hand = hand
        self.points = points

def options(card):
    gate = None
    
    if card == "Hadamard":
        print("choose target: [0,1,2]")
        target = int(input())
        gate = gt.HadamardGate(target)
    elif card == "XGate":
        print("choose target: [0,1,2]")
        target = int(input())
        gate = gt.XGate(target)

    elif card == "CNOT":
        print("choose control: [0,1,2]")
        control = int(input())
        print("choose target: [0,1,2]")
        target = int(input())
        gate = gt.CNOTGate(control,target)

    elif card == "Toffoli":
        print("choose control 1: [0,1,2]")
        control1 = int(input())
        print("choose control 2: [0,1,2]")
        control2 = int(input())
        print("choose target: [0,1,2]")
        target = int(input())
        gate = gt.ToffoliGate([control1,control2],target)

    elif card == "SWAP":
        print("choose control 1: [0,1,2]")
        control1 = int(input())
        print("choose control 2: [0,1,2]")
        control2 = int(input())
        gate = gt.SWAPGate([control1,control2])

    elif card == "Measure":
        if round_num == 1:
            print("illegal")
        else:
            end_game_seq()
        
    return gate
    
def play_card(c,player,gate,card):
    c.apply_gate(gate)
    player.hand[card] -= 1

def display_card(player):
    print(player.hand)

def end_game_seq():
    C.apply_gate(measure)
#     config = C.get_gates() ???
    end_sw = 1

def init_shuffle():
    arr = ["Hadamard","Hadamard","XGate","Measure","XGate","CNOT","SWAP","SWAP","SWAP","SWAP","SWAP","SWAP"]
    random.shuffle(arr)

    h = [{},{},{}]
    for i in range(3):
        curr_p = h[i]
        for j in range(4):
            temp = arr[(4 * i) + j]
            if temp not in curr_p:
                curr_p[arr[(4 * i) + j]] = 1
            else:
                curr_p[arr[(4 * i) + j]] += 1
    
    return h

def ind_round(player_arr,curr_player,control,target):
    
    p1,p2,p3 = player_arr
    if (len(p1.hand) == 0 and len(p2.hand) == 0 and len(p3.hand) == 0):
        end_game_seq()
  
    player = player_arr[curr_player]
    
    while len(player.hand) == 0:
        curr_player += 1
        curr_player = curr_player % 3
        player = player_arr[curr_player]

    print("display_circuit")
    display_card(player)
    
#     if player clicks on card:
    card = random.sample(list(player.hand), 1)[0] #change this
    gate_appl = options(card,control,target)
    play_card(player,gate_appl,card)

    display_card(player)
    print("display_circuit")
    curr_player += 1
    curr_player = player % 3
    
    return curr_player

def init_func():
    house = 0
    end_sw = 0
    
    curr_player = 0
    hands = init_shuffle()
    p1 = player(hands[0],0)
    p2 = player(hands[1],0)
    p3 = player(hands[2],0)

    player_arr = [p1,p2,p3]

    c = ct.Circuit()
    return c,house,end_sw,curr_player,player_arr
#initializing


# In[2]:





# In[13]:


get_ipython().system('pip install pylatexenc')


# ## This should be wrapper in main func

# In[ ]:


def main():
    print("-----Begin Game-----")
    c,house,end_sw,curr_player,player_arr = init_func()
    print(f"Player{curr_player}")
    print("Press Enter to continue")
    input()
    
    print("These are your cards")
    cards = player_arr[curr_player].hand
    print(cards)
    c.draw()
    
    #Rounds
    while end_sw == 0:
        p1,p2,p3 = player_arr
        if (len(p1.hand) == 0 and len(p2.hand) == 0 and len(p3.hand) == 0):
            end_game_seq()

        player = player_arr[curr_player]

        print(f"Player{curr_player}")
        print("Press Enter to continue")
        input()

        print("These are your cards")
        cards = player_arr[curr_player].hand
        print(cards)
        fig = c.draw()
        print(c.draw())

        print(f"choose from one option: {player.hand.keys()}")
        choice = input()

        gate_appl = options(choice)
        play_card(c,player,gate_appl,choice)

        print("display_circuit")
        curr_player += 1
        curr_player = curr_player % 3

main()


# In[ ]:





# In[ ]:




