money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

months_of_happiness = 0
money = money_capital + salary - spend #Оставшиеся деньги после 1-го месяца

while(money >= 0):
    money = money + salary - spend * (1 + increase * months_of_happiness)
    months_of_happiness = months_of_happiness + 1

months_of_happiness = months_of_happiness - 1 #1 месяц лишний, потому что первым считали 0-й месяц

print("Количество месяцев, которое можно протянуть без долгов:", months_of_happiness)