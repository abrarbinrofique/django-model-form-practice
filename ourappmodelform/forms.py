from django import forms
import datetime
from ourappmodelform.models import MyModel



class Example(forms.ModelForm):
	class Meta:
		model=MyModel
		fields='__all__'

