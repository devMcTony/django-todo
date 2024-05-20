from django import forms
from django.forms import ModelForm

from .models import *


class TodoForm(forms.ModelForm):
	title= forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Add new to-do...',"class":"border p-2 border-gray-200 rounded focus:outline-none"}))

	class Meta:
		model = TodoItem
		fields = '__all__'
