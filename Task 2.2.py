salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

salary_total = salary * months #Итоговая зарплата за 10 месяцев

geom_progress_sum = 0

for i in range(0,months):
    geom_progress = pow((1 + increase), i)
    geom_progress_sum = geom_progress_sum + geom_progress

spend_total = spend * geom_progress_sum

money_capital = spend_total - salary_total

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", int(money_capital))