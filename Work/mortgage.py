# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000.0

current_month = 1

while principal > 0:
    if current_month >= extra_payment_start_month and current_month <= extra_payment_end_month:
        principal = principal * (1 + rate / 12) - payment - extra_payment
        total_paid = total_paid + payment + extra_payment
    else :
        principal = principal * (1 + rate / 12) - payment
        total_paid = total_paid + payment
    
    if principal < 0:
        total_paid = total_paid + principal
        principal = 0.0

    print(f'{current_month} {total_paid:0.2f} {principal:0.2f}')

    current_month = current_month + 1
    

print(f'Total paid {total_paid:0.2f}')