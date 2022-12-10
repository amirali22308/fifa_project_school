from search import *
from profile import *
from compare import *
from mosts import *

import os
def main() -> None:
    path = os.path.realpath(__file__)
    path = os.path.dirname(path) + chr(92) + "data" + chr(92)
    print("enter exit to exit the program")
    print("enter graphics to enter graphical user interface")
    print("enter help for more information")
    while True:
        Input = input().split(" ")
        if Input[0] == "exit":
            break
        elif Input[0] == "graphics":
            print("not here yet!")
        elif Input[0] == "help":
            if len(Input) == 1:
                print("enter help [insert command name] for more")
                print("all active comands:")
                print("*\tsearch player")
                print("*\tsearch team")
                print("*\tsearch manager")
                print("*\tsearch referee")
                print("*\tsearch player")
                print("*\tprofile player")
                print("*\tprofile team")
                print("*\tprofile manager")
                print("*\tprofile referee")
                print("*\tprofile competition")
                print("*\ttop goal scorer")
                print("*\tbest attack")
                print("*\tbest defense")
            elif Input[1] == "search":
                if Input[2] == "player":
                    print("inputs:\n*\tplayer firstname or lastname")
                    print("outputs:\n*\tplayer(s) firstname and lastname and id")
                if Input[2] == "team":
                    print("inputs:\n*\tteam name or code")
                    print("outputs:\n*\tteam(s) name and code and id")
                if Input[2] == "manager":
                    print("inputs:\n*\tmanager firstname or lastname")
                    print("outputs:\n*\tmanager(s) firstname and lastname and id")
                if Input[2] == "referee":
                    print("inputs:\n*\treferee firstname or lastname")
                    print("outputs:\n*\treferee(s) firstname and lastname and id")
            elif Input[1] == "profile":
                print("inputs:\n*\t",Input[2]," id")
                print("outputs:\n*\t",Input[2],"'s data")
            elif Input[1:4] == ['top','goal','scorer']:
                print("inputs:\n*\tyear(eg. 1993 or all)")
                print("outputs:\n*\tdata about top scorer")
            elif Input[1:3] == ['best','attack']:
                print("inputs:\n*\tyear(eg. 1993 or all)")
                print("outputs:\n*\tdata about best attacking team")
            elif Input[1:3] == ['best','deffense']:
                print("inputs:\n*\tyear(eg. 1993 or all)")
                print("outputs:\n*\tdata about best defending team")
        elif Input[0] == "search":
            output = "there is no such input!"
            if Input[1] == "player": output = search(input(),path+"players.csv",2,0,2,1)
            if Input[1] == "team": output = search(input(),path+"teams.csv",1,0,2,2)
            if Input[1] == "manager": output = search(input(),path+"managers.csv",1,0,2,2)
            if Input[1] == "referee": output = search(input(),path+"referees.csv",1,0,2,2)
            if output is str:
                print(output)
            else: 
                for item in output[0:30]: print(output)
                if len(output) > 30: print("more than 30 results")
        elif Input[0] == "profile":
            if Input[1] == "player": player_profile(path,input())
            if Input[1] == "team": team_profile(path,input())
            if Input[1] == "manager": manager_profile(path,input())
            if Input[1] == "referee": referee_profile(path,input())
            if Input[1] == "competition": compare(path,input(),input())
        elif Input == ['top','goal','scorer']:
            year = input()
            if year == 'all': year = None
            else: year = int(year)
            best_goaler(path,year)
        elif Input == ['best','attack']:
            year = input()
            if year == 'all': year = None
            else: year = int(year)
            goals_check(path,False,year)
        elif Input == ['best','defense']:
            year = input()
            if year == 'all': year = None
            else: year = int(year)
            goals_check(path,True,year)
        else:
            print("there is no such command")
if __name__ == "__main__":
    main()