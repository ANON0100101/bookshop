from django.core.mail import send_mail

def send_activation_code(email,code):
    send_mail(
        'activation_code',
        f'Привет, для активации аккаунта перейди по данной ссылке: \n\n http://localhost:8000/api/account/activate/{code}',
        'a.kudaikulov04@gmail.com',
        [email]
    )