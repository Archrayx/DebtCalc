#Debt Calculator
##############################
#Imports turtle module for UI#
##############################
import turtle
wn = turtle.Screen()
wn.title("Debt Calculator")
wn.setup(width=1280,height=720)
wn.bgcolor("cyan")
#################################
#Sets question prompt parameters#
#################################
final = turtle.Turtle()
final.penup()
final.goto(-600,200)
final.pendown()
wn.update()
currentB = float(wn.textinput("balance?: ","balance?"))
wn.update()
months = int(wn.textinput("how many months to pay off in?: ","how many months to pay off in?"))
apr = float(wn.textinput("apr(in decimal)?: ","apr(in decimal)?")) / months
####################################
#Main Function that Calculates Debt#
####################################
mmp = 10 #minimum payment will be incremented by 10 when new balance does not decrease current
         #balance AND when requested months does not match calculated amount of months to finish

def calc(currentB):
    global mmp
    month = 0
    while currentB > 0:
        newB = round(currentB * (1+apr) - mmp,2)
        if newB > currentB:
            print(apr, newB, currentB, mmp)
            mmp += 10
        else:
            month += 1
            print(month,newB,currentB,mmp) #ALL CALCULATIONS CAN BE SEEN DONE ON TERMINAL WITH THIS FORMAT
            currentB = round(newB,2)
    return([month,newB,currentB,mmp])
##############################################################
#while loop that checks calculated month and requested months#
##############################################################
balanceCalc = calc(currentB)

while balanceCalc[0] > months:
    mmp += 10
    balanceCalc = calc(currentB)

######################################
#Screen to display Final Calculations#
######################################
while True:
    wn.update()
    if balanceCalc[0] == 12 and balanceCalc[2] == 0:
        final.write("for " + str(months) + " months, you will need to pay " + str(balanceCalc[3]) + " dollars.",font = ("Times New Roman", 20, "normal"))
    else:
        final.write("for " + str(balanceCalc[0]) + " months, you will need to pay " + str(balanceCalc[3]) + " dollars. and on the " + str(balanceCalc[0] + 1) + "th month you will need to pay " + str(round((balanceCalc[2]+mmp)/(1+apr),2)),font = ("Times New Roman", 20, "normal"))
