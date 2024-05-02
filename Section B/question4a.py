def calculateBonus(salary, yearofService):
    bonus = 0
    if yearofService > 4:
        bonus = 0.08 * salary
    elif yearofService == 3:
        bonus = 0.05 * salary
    netBonus = bonus
    netSalary = salary + netBonus
    return netBonus, netSalary

while True:
    try:
        salary = float(input("Enter employee's salary: "))
        
        yearofService = int(input("Enter employee's years of service: "))
        netBonus, netSalary = calculateBonus(salary, yearofService)
        
        
        print(f"Net bonus amount: {netBonus}")
        print(f"Net salary amount: {netSalary}")
        
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    choice = input("Do you want to continue? (y/n): ")
    if choice.lower() != 'y':
        break
