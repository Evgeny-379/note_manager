
username = input("Введите имя: ")
title = []
i = 0
while i < 3:
    i = i + 1
    title.append(input("Введите заголовок заметки: "))
title = input("Введите заголовок заметки: ")
content = input("Введите описание заметки: ")
status = input("Введите статус заметки: ")
created_date = input('Введите дату создания заметки в формате "день-месяц-год": ')
issue_date = input('Введите дата истечения заметки (дедлайн) в формате "день-месяц-год": ')

print("Имя пользователя:", username)
print("Заголовоки заметок:", title[0], title[1], title[2], sep=', ')
print("Описание заметки:", content)
print("Статус заметки:", status)
print("Дата создания заметки:", created_date)
print("Дата истечения заметки:", issue_date)