from celery import shared_task
from billing_app.models import Purchase
from django.core.mail import send_mail
from billing_system_project import settings


@shared_task
def send_invoice_confirmation_mail(purchase_id,customer_email):
    purchase = Purchase.objects.get(id=purchase_id)
    mail_sub = f"Invoice for your purchase on {purchase.created_at.strftime('%d-%m-%Y %H:%M:%S')}"
    mail_content = f"Thank you for your purchase. Your net price is {purchase.net_price} and paid amount is {purchase.paid_amount}. Your balance amount is {purchase.balance_amount}"

    send_mail(
        subject=mail_sub,
        message=mail_content,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[customer_email],
        fail_silently=False,
    )
    print("Sending invoice email...")