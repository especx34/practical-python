# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
num_months = 0
extra_pmt = 1000
extra_payment_start_month = 61
extra_payment_end_month = 108

while principal > 0:
  num_months = num_months +1
  principal = principal * (1+ rate/12) - payment
  total_paid = total_paid + payment
  if num_months >= extra_payment_start_month and num_months <= extra_payment_end_month:
    principal = principal - extra_pmt
    total_paid = total_paid + extra_pmt
  
  print(num_months,total_paid,principal)
  

print('Total paid',total_paid) 
print('Months',num_months)
