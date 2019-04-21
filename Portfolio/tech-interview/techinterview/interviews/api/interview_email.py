import jwt

from django.conf import settings
from django.template.loader import get_template
from django.core.mail import send_mail
import datetime


def anc(id):
    try:
        payload = {}
        payload['id'] = id
        payload['exp'] = datetime.datetime.now() + datetime.timedelta(days=3)
        token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
    except Exception as error:
        raise error

    return token


def send_email_cand(token, serializer):
    cand_name = serializer['candidate']['auth']['first_name'].capitalize()
    cand_email = [serializer['candidate']['auth']['email'],]
    inter_id = serializer['id']
    date = serializer['interview_date']
    year = date[0:4]
    month = date[5:7]
    day = date[8:10]
    hour = date[11:13]
    minute = date[14:16]
    inter_date = "{0}:{1}, {2}-{3}-{4}".format(hour, minute, day, month, year)
    subject_email = 'Technical Poll'
    from_email = settings.DEFAULT_FROM_EMAIL
    context = {
        'username': cand_name,
        'interview_id': inter_id,
        'email': cand_email,
        'date': inter_date,
        'url': "http://127.0.0.1:8000/api/interviews/link_interview/{}".format(token.decode('utf-8'))
    }
    email_html_message = "{}, from {}, time {}".format(cand_name, cand_email, inter_date)
    email_html_message = get_template('mail_candidate.html').render(context)
    send_mail(subject_email,
              email_html_message,
              from_email, cand_email,
              fail_silently=False,
              html_message=email_html_message)


def deanc(token):
    decoded = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
    return decoded['id']


def create_token(id):
    try:
        payload = {}
        payload['id'] = id
        payload['exp'] = datetime.datetime.now() + datetime.timedelta(days=3)
        token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
    except Exception as error:
        raise error

    return token


def send_email_expert(token, serializer):
    expert_name = serializer['expert']['auth']['first_name'].capitalize()
    expert_email = [serializer['expert']['auth']['email'],]
    inter_id = serializer['id']
    date = serializer['interview_date']
    year = date[0:4]
    month = date[5:7]
    day = date[8:10]
    hour = date[11:13]
    minute = date[14:16]
    inter_date = "{0}:{1}, {2}-{3}-{4}".format(hour, minute, day, month, year)
    subject_email = 'Technical Poll'
    from_email = settings.DEFAULT_FROM_EMAIL
    context = {
        'name': expert_name,
        'interview_id': inter_id,
        'email': expert_email,
        'date': inter_date,
        'url': "http://127.0.0.1:8000/api/interviews/link_interview_exp/{}".format(token.decode('utf-8'))
    }

    email_html_message = "{}, from {}, time {}".format(expert_name, expert_email, inter_date)
    email_html_message = get_template('mail_expert.html').render(context)
    send_mail(subject_email,
              email_html_message,
              from_email,
              expert_email,
              fail_silently=False,
              html_message=email_html_message)
