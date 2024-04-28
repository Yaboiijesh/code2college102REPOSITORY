show databases
import mysql.connector

def menu():
  print("--------------------------------------------")
  print("1. View Account Balances ")
  print("2. Deposit ")
  print("3. Withdraw ")
  print("4. Delete account")
  print("5. Make accoount")
  print("6. Change account details")
  print("--------------------------------------------")

connection = mysql.connector.connect(
        user = 'root', 
        database = 'sample', 
        password = 'poop1234'
)