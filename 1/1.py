def expensify():
  expenses = [expense.strip() for expense in open('input', 'r').readlines()]
  for expense in expenses:
    for compare_expense in expenses:
      if int(expense) + int(compare_expense) == 2020:
        return int(expense) * int(compare_expense)

if __name__ == "__main__":
  print(expensify())
