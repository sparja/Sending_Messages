import os
import smtplib

site_name = "https://dvmn.org/referrals/1tB51q9gDU5BPxKRcALJ4XSBOshQKqMbUGyGhT0G/"
friends = "Димитрий"
name = "Вадим"
subject = "Приглашение!"
content_type = 'text/plain; charset="UTF-8"'
to = "Vadim.konshin456@yandex.ru"
from_whom = "sero-munk@yandex.ru"
password = os.environ['PASSWORD_YANDEX']
login = os.environ['LOGIN_YANDEX']

letter = """\
From: {from_whom}
To: {to}
Subject: {subject}
Content-Type: {content_type}

Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → %website%  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл...""".replace("%website%", "https://dvmn.org/referrals/1tB51q9gDU5BPxKRcALJ4XSBOshQKqMbUGyGhT0G/").replace("%friend_name%", friends).replace("%my_name%", name).format(to = to, from_whom = from_whom, subject = subject, content_type = content_type)

letter = letter.encode("UTF-8")
server = smtplib.SMTP_SSL('smtp.yandex.ru:465')
server.login(login, password)
server.sendmail(login, to, letter)
server.quit()
