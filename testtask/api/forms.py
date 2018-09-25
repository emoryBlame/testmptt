from django.forms import ModelForm
from django.db import models
from .models import *
from django.forms.models import modelform_factory

'''
class ElemForm(ModelForm):
	class Meta:
		model = Element
		fields = ["name", 'description', 'icon', 'parent']
'''

ElemForm = modelform_factory(Element, fields = ('name', 'description', 'icon', 'parent'))