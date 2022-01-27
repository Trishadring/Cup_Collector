from django.forms import ModelForm
from .models import Using

class UsingForm(ModelForm):
  class Meta:
    model = Using
    fields = ['date', 'content']