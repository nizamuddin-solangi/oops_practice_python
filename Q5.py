class EmailNotification:
    def send(self, message):
        print("Email sent:", message)


class SMSNotification:
    def send(self, message):
        print("SMS sent:", message)


class PushNotification:
    def send(self, message):
        print("Push notification sent:", message)


class WhatsAppNotification:
    def send(self, message):
        print("WhatsApp message sent:", message)


def notify_all(notifications, message):
    for notification in notifications:
        notification.send(message)


all_notifications = [
    EmailNotification(), SMSNotification(), PushNotification(), WhatsAppNotification()
]
notify_all(all_notifications, "Your order has been delivered.")

# Polymorphism happens because every object uses the same send() call differently.
