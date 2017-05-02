import os, room

def press_enter():
    input("\npress enter..")

def clear():
    clearconsole = lambda: os.system('cls')
    clearconsole()

def print_controlls():
    clear()
    print("""Movement:
    
    North:                  w
    East:                   d
    South:                  s 
    West:                   a
    Up:                     up
    Down:                   down

Room description:       info
    
Fight:                  fight
    
Search room for items:  search

Controlls:              controlls
Exit game:              exit
    """)

def print_home():
    #http://patorjk.com/software/taag/#p=display&h=1&v=0&c=bash&f=Three%20Point&t=Welcome%20to
    print("""
     # # # # # # # # # # # # # # # # #
    # \    / _ | _ _  _ _  _   _|_ _  #
    #  \/\/ (/_|(_(_)| | |(/_   | (_) #
    #                                 #
    #  -|-|_  _   |\/| _  _  _. _  _  #
    #   | | |(/_  |  |(_|| |_\|(_)| | #
     # # # # # # # # # # # # # # # # #
    """)

    
        
