def computepay(hour, rate, bonus, hourLimit, bonusLimit, timesmorerate):
    pay = hour * rate
    if hour >= bonusLimit:
      pay = pay + bonus
    if hour >= hourLimit:
        ahrs = hour - hourLimit
        arate = rate * timesmorerate
        apay = arate * ahrs #You do not need the float function.
        pay = pay + apay
    return pay 

hour = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))
bonus = float(input("Enter Bonus: "))
hourLimit = float(input("Enter hour limit to have extra rate: "))
bonusLimit = float(input("Enter hour limit to have a bonus: "))
timesmorerate = float(input("Enter times more rate is: "))
pay = computepay(hour, rate, bonus, hourLimit, bonusLimit, timesmorerate)
print('Pay: ', pay)
