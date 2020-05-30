# mortgage.py
#
# Exercise 1.7
#Base mortage info
principal = 500000.0
rate = 0.05
payment = 2684.11

#Extra payment variables
extra_payment = 1000
extra_payment_start_month = 60
extra_payment_end_month = 108

#Counter variables
total_paid = 0.0
months = 0

while principal > 0:
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    months += 1
    if months <= extra_payment_end_month and months >= extra_payment_start_month:
        principal = principal - extra_payment
        total_paid += extra_payment
    #Print table
    if principal < 0:
        total_paid += principal
        principal += abs(principal)

    print(months, round(total_paid, 2), round(principal, 2))

print('Total paid', round(total_paid, 2))
print('Total months', months)