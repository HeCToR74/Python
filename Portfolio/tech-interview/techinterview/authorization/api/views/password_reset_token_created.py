from django.dispatch import receiver
from django_rest_passwordreset.signals import reset_password_token_created
from django.conf import settings
from django.template.loader import get_template
from django.core.mail import send_mail
from techinterview.logger import log


@receiver(reset_password_token_created)
def password_reset_token_created(sender, reset_password_token, *args, **kwargs):
    """password_reset_token_created function"""

    context = {
        'current_user': reset_password_token.user,
        'username': reset_password_token.user.username,
        'email': reset_password_token.user.email,
        'reset_password_url':
            "{SITE_URL}/password_reset/confirm/{}".format(reset_password_token.key, SITE_URL=settings.SITE_URL)
    }

    subject = 'Contact Form Received'
    from_email = settings.DEFAULT_FROM_EMAIL
    to_email = [reset_password_token.user.email]
    log.info('User {} requested password reset'.format(reset_password_token.user.username))
    email_html_message = get_template('mail_send.html').render(context)
    is_email_sent = send_mail(subject, email_html_message, from_email, to_email)
    if is_email_sent:
        log.info('Email was sent to {}'.format(reset_password_token.user.email))
    else:
        log.info('Email was\'t sent')

    return is_email_sent
