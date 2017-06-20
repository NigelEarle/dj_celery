from celery import shared_task, current_task
from celery.utils.log import get_task_logger
from django.core.mail import send_mail

logger = get_task_logger(__name__)

@shared_task(name="feedback_email_task")
def feedback_email_task(name, email, message):
  return send_email(name, email, message)

def send_email(name, email, message):
  send_mail(name, message, None, [email], fail_silently=False)
