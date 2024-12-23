from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Form
from .serializers import FormSerializer
# Create your views here.
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponse
class FormCreate(generics.ListCreateAPIView):
    queryset = Form.objects.all()
    serializer_class = FormSerializer

    def perform_create(self, serializer):
        # Save the form data
        form_instance = serializer.save()

        # Send an email
        send_mail(
            subject=f"New Form Submission",
            message=f"""
            You have received a new form submission:

            Name: {form_instance.fname} {form_instance.lname}
            Company: {form_instance.company or 'N/A'}
            Email: {form_instance.email}
            Phone: {form_instance.phone}
            Subject : {form_instance.sub}
            Message: {form_instance.message}
            """,
            from_email="shreyasameerbhoir16@gmail.com",  # Replace with your email
            recipient_list=["shreyaahb@gmail.com"],  # Replace with your email
        )

class FormRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Form.objects.all()
    serializer_class = FormSerializer
    lookup_field = "pk"

