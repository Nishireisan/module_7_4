team1_num = 5
print('В команде Мастера Кода участников: %s !' % team1_num)
team2_num = 6
print('Итого сегодня в командах участников: %s и %s !' % (team1_num, team2_num))
score2 = 42
print("Команда Волшебники Данных решила задач: {}!".format(score2))
team2_time = 18015.2
print('Волшебники данных решили задачи за {}!'.format(team2_time))
score1 = 40
print(f'Команды решили {score1} и {score2} задач.')
tasks_total = score1 + score2
time_avg = 350.4
team1_time = score1 * time_avg
if score2 <= score1 and team1_time > team2_time:
    challenge_result = 'Победа команды Мастера Кода!'
elif score1 <= score2 and team1_time < team2_time:
    challenge_result = 'Победа команды Волшебники Данных!'
else:
    challenge_result = 'Ничья'
print(f'Результат битвы: {challenge_result}')
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')
