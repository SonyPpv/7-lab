days = ("Понеделник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье")
w = int(input("Сколько выходных на неделе вы хотите? "))
weekends = days[-w:]
work = days[:-w]
print("Ваши выходные дни:", ", ".join(weekends))
print("Ваши рабочие дни:", ", ".join(work))

