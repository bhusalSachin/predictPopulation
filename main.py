initPop = int(input("Enter initial population"))
rateOfGrowth = int(input("Enter rate of growth"))
hrToAchieve = int(input("Enter number of hours to achieve the rate of hours"))
totalHour = int(input("Enter total hours during which population grows"))

def predictPop(i, r, h, t):
    totalPop = 0
    splitHr = int(t/h)
    for j in range(splitHr):
        totalPop = i * r
        i = totalPop
    print(totalPop)

predictPop(initPop, rateOfGrowth, hrToAchieve, totalHour)
