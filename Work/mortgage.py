# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
num_months = 0
extra_pmt = 1000
i = 0

while principal > 0:
  principal = principal * (1+ rate/12) - payment
  total_paid = total_paid + payment
  if i < 12:
    principal = principal - extra_pmt
    total_paid = total_paid + extra_pmt
    i = i + 1
  num_months = num_months +1

print('Total paid',total_paid, num_months,'months')
