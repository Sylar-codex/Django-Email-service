from rest_framework import serializers
from .models import EmailMessenger
from .utils import Util

class EmailMessengerSerializers(serializers.ModelSerializer) :
    class Meta :
        model = EmailMessenger
        fields = '__all__'

    def create(self, data):
        subject = data.get("subject")
        body = data.get("body")
        to_email = data.get("to_email")
        email_data = {'email_body':body, "to_email":to_email,"email_subject":subject}
        Util.send_email(email_data)

        email = EmailMessenger.objects.create(subject=subject, body=body, to_email=to_email)
        return email