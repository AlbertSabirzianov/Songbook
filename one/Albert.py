import smtplib
from email.mime.text import MIMEText


class Post:
    my_email = 'albertuno@mail.ru'
    my_password = 'ezq5srpfxNpqpWnzudtq'

    def __init__(self, name, count, comp):
        self.name = name
        self.count = count
        self.comp = comp

    def get_message(self):
        message = MIMEText('Привет!\n' + str(self.name) + ' загрузил композицую: '
                           + str(self.comp) + '\n'
                           + 'Сейчас на сайте уже ' + str(self.count) + ' композиций!'
                           )
        message['Subject'] = 'Создателю сайта Songbook'
        return message

    def send(self):
        Obj = smtplib.SMTP_SSL('smtp.mail.ru', 465)
        Obj.ehlo()
        Obj.login(self.my_email, self.my_password)
        Obj.sendmail(self.my_email, self.my_email, self.get_message().as_string())
        Obj.quit()


class World:
    data = {
        '0': 'ок',
        '1': 'ка',
        '2': 'ки',
        '3': 'ки',
        '4': 'ки',
        '5': 'ок',
        '6': 'ок',
        '7': 'ок',
        '8': 'ок',
        '9': 'ок',
    }

    def __init__(self, number):
        self.number = number

    def wr(self):
        return self.data[str(self.number)[-1]]
