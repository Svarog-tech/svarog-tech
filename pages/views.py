from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
import requests
import json

# Create your views here.
def home(request):
    return render(request, 'pages/home.html')

def index(request):
    return render(request, 'pages/index.html')

def send_discord_notification(name, email, message):
    """Send contact form submission to Discord via bot"""
    bot_token = settings.DISCORD_BOT_TOKEN
    channel_id = settings.DISCORD_CHANNEL_ID

    if not bot_token or not channel_id:
        return False

    # Discord API endpoint for sending messages
    url = f"https://discord.com/api/v10/channels/{channel_id}/messages"

    # Create Discord embed
    embed = {
        "title": "New Contact Form Submission",
        "color": 16766720,  # Amber color
        "fields": [
            {
                "name": "Name",
                "value": name,
                "inline": True
            },
            {
                "name": "Email",
                "value": email,
                "inline": True
            },
            {
                "name": "Message",
                "value": message,
                "inline": False
            }
        ],
        "footer": {
            "text": "Svarog Tech Contact Form"
        }
    }

    payload = {
        "embeds": [embed]
    }

    headers = {
        "Authorization": f"Bot {bot_token}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        return response.status_code == 200
    except Exception as e:
        print(f"Discord bot error: {e}")
        return False

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        message = request.POST.get('message', '')

        if name and email and message:
            try:
                # Send to Discord
                discord_sent = send_discord_notification(name, email, message)

                # Also send email as backup (optional)
                # send_mail(
                #     subject=f'New Contact Form Submission from {name}',
                #     message=f"""
                # New contact form submission:
                #
                # Name: {name}
                # Email: {email}
                # Message:
                # {message}
                # """,
                #     from_email=settings.EMAIL_HOST_USER,
                #     recipient_list=['staffsvarog@gmail.com'],
                #     fail_silently=True,
                # )

                if discord_sent:
                    messages.success(request, 'Thank you for your message! We will get back to you soon.')
                else:
                    messages.error(request, 'Sorry, there was an error sending your message. Please try again later.')
            except Exception as e:
                messages.error(request, 'Sorry, there was an error sending your message. Please try again later.')
        else:
            messages.error(request, 'Please fill in all fields.')

    return render(request, 'pages/contact.html')