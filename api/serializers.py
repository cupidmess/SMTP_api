from rest_framework import serializers
from .models import Form
class FormSerializer (serializers.ModelSerializer):
  class Meta : 
    model = Form
    fields = ["id", "fname", "lname", "company", "email", "phone", "sub", "message", "published_date"]