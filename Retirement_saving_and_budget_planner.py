# -*- coding: utf-8 -*-
"""
Created on Mon Nov 24 09:53:03 2025

@author: surya
"""


print(" || <<<RETIREMENT SAVINGS & BUDGET TOOL>>> ||   ")


#  1. Basic Information neeeded
name = input("Please enter your name: ")
age = int(input("What is your current age? "))
retire_age = int(input("At what age would you like to retire? "))

years_left = retire_age - age

if years_left <= 0:
    print("Looks like you are already at retirement age!")
    years_left = 0
else:
    print(f"You have around {years_left} year(s) left before you retire.\n")

# 2. Savings Plan
print("Let's check your savings plan\n")

current_savings = float(input("How much savings do you currently have (rupee)? "))
monthly_saving = float(input("How much can you save every month (rupee)? "))
income = float(input("Enter your current monthly income (rupee): "))

# Simple Interest Calculation (assuming 5% annual interest)
interest_rate = 0.05

# 1. Estimate interest on initial savings (simple interest)
future_value = current_savings * (1 + interest_rate * years_left)

# 2. Estimate interest on contributions (assumes contributions earn interest for half the duration on average)
total_contributions = monthly_saving * 12 * years_left
future_value += total_contributions * (1 + interest_rate * (years_left / 2))

print("<<<<<<<<<<-------------------------------------->>>>>>>>>>>>>")
print(f"Your estimated savings at retirement: ₹{future_value:,.2f}")
print("<<<<<<<<<<-------------------------------------->>>>>>>>>>>>>")

# 3. Monthly Budget 
print("Now let's figure out your monthly budget\n")

print("Enter your monthly expenses below:")
rent = float(input("   House Rent or Maintenance: ₹"))
food = float(input("   Food & Groceries: ₹"))
medicine = float(input("   Medicines/Health: ₹"))
travel = float(input("   Transport/Travel: ₹"))
other = float(input("   Other expenses: ₹"))

total_expenses = rent + food + medicine + travel + other
balance = income - total_expenses - monthly_saving

 # Checks if income covers expenses AND the savings goal

# calculation
print(" MONTHLY EXPANCE")
print(f"Total Income:              ₹{income:,.2f}")
print(f"Total Expenses:            ₹{total_expenses:,.2f}")
print(f"Monthly Savings Goal:      ₹{monthly_saving:,.2f}")
print("________________________________________________________________")

# Budget Health Check
expense_ratio = (total_expenses * 100) / income
savings_ratio = (monthly_saving * 100) / income

print(f"Your expenses are:       {expense_ratio:,.1f}% of your monthly income")
print(f"You are saving:          {savings_ratio:,.1f}% of your monthly income")
print("________________________________________________________________")

if balance > 0:
    print(f"You have ₹{balance:,.2f} left after expenses and  your savings goal.    <<<Excellent!>>")
elif balance == 0:
    print("||You're perfectly on budget||No loss, no extra saving Need  more saving to meat your goal.")
else:
    # balance is negative, we show the positive shortfall
    print(f"||You are short by|| ₹{-balance:,.2f} to meet your budget and savings goal Try to reducing some expenses.")


print("<<< Thank you!! <<best wishes for you bright futrure>>                            - by suryansh pratap singh   ")
