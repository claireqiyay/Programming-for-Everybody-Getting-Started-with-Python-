hrs= float(input('Enter Hours: '))
rate  = float(input('Enter Rate: '))
pay = hrs * rate
if hrs > 40:
    ahrs = hrs - 40
    arate = rate * (1.5 - 1.0)
    apay = float(ahrs) * float(arate)
    pay = pay + apay
print(pay)
