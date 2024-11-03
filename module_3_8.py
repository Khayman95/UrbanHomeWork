def send_email(message, recipient,*, sender):
    c = recipient.find('@')
    b = recipient.find('.com' or '.ru' or '.net')
    if c < 0 or b < 0:
        print('Невозможно отправить письмо с адреса ', sender, 'на адрес ', recipient)
    elif sender == recipient:
        print('Нельзя отправить письмо самому себе!')
    elif sender == 'university.help@gmail.com':
        print('Письмо успешно отправлено с адреса ', sender, 'на адрес', recipient)
    else:
        print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса ', sender, 'на адрес', recipient)
send_email('привет всем','khayman@yandex.com',sender='university.help@gmail.com')