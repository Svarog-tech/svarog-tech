from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def home(request):
    return render(request, 'pages/home.html')

def index(request):
    return render(request, 'pages/index.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        message = request.POST.get('message', '')

        if name and email and message:
            try:
                # Email subject and body
                subject = f'New Contact Form Submission from {name}'
                email_body = f"""
New contact form submission:

Name: {name}
Email: {email}
Message:
{message}
"""

                # Send email
                send_mail(
                    subject=subject,
                    message=email_body,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=['staffsvarog@gmail.com'],
                    fail_silently=False,
                )

                messages.success(request, 'Thank you for your message! We will get back to you soon.')
            except Exception as e:
                messages.error(request, 'Sorry, there was an error sending your message. Please try again later.')
        else:
            messages.error(request, 'Please fill in all fields.')

    return render(request, 'pages/contact.html')