""" ATM Withdrawal Logic
Create an ATM program with a balance of ₹15,000.
Rules:
• Correct PIN: 4321.
• Withdrawal must be positive.
• The balance must never fall below ₹2,000.
• Withdrawals above ₹10,000 require manager approval.
• An incorrect PIN must prevent all further transactions.
Tricky condition: The balance is ₹12,000 and the customer tries to withdraw ₹11,000 without manager approval.
Task: Use nested if statements to handle every condition and display the correct remaining balance"""

balance = 15000
correct_pin = 4321
entered_pin = int(input("Enter your 4 digit pin: "))
withdrawal_amount=int(input("Enter amount to withdraw: "))
if entered_pin == correct_pin:
  print("Pin is correct")
  if withdrawal_amount>0:
    if balance - withdrawal_amount>=2000:
      if withdrawal_amount > 10000:
        manager_approval=(input("yes or no: "))
        if manager_approval=="yes":
          print("Amount withdrawal successfully")
        else:
          print("Manager permission required ")
  else:
    print("Amount can't be negative impact ")
else:
  print("Invalid Pin")
remaining_balance=balance-withdrawal_amount
print("Remaining amount", remaining_balance)
