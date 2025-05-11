from django.db import models

class Reminder(models.Model):
    REMINDER_METHOD_CHOICES = [
        ('sms', 'SMS'),
        ('email', 'Email'),
    ]

    date = models.DateField()
    time = models.TimeField()
    message = models.TextField()
    method = models.CharField(max_length=10, choices=REMINDER_METHOD_CHOICES)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.method.upper()} Reminder at {self.date} {self.time}"
