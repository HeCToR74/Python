"""helper file with other functions"""

from authorization.models import Roles, UserData
from django.conf import settings
from django.template.loader import get_template
from django.core.mail import send_mail


def set_first_last_role(user, request):
    """
    save any fields to AUTH_USER
    nd create UserData an entry with model AUTH_USER
    """

    user.first_name = request.data['first_name']
    user.last_name = request.data['last_name']
    user.is_active = False
    user.save()

    role = Roles.objects.get(name='recruiter')
    UserData.objects.create(f_auth=user, f_role=role)

    return user


def email_confirm_token_send(user, token):
    """send email to new user"""

    context = {
        'current_user': user,
        'username': user.username,
        'email': user.email,
        'verify_url': "{SITE_URL}/api/user/verify_email/{}".format(token.decode('utf-8'), SITE_URL=settings.SITE_URL)
    }

    subject = 'Contact Form Received'
    from_email = settings.DEFAULT_FROM_EMAIL
    to_email = [user.email]

    email_html_message = get_template('mail_confirm.html').render(context)
    return send_mail(subject, email_html_message, from_email, to_email)
