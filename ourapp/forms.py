from django import forms
import datetime



class ExampleForm(forms.Form):
	
	name = forms.CharField()
	comment = forms.CharField(widget=forms.Textarea)
	comment = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
	email = forms.EmailField()
	agree = forms.BooleanField()
	date = forms.DateField()
	date = forms.DateField()
	value = forms.DecimalField()
	email_address = forms.EmailField( 
    label="Please enter your email address",
      )
	first_name = forms.CharField(initial='Your name')
	agree = forms.BooleanField(initial=True)
	day = forms.DateField(initial=datetime.date.today)
	FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
           ]
	favorite_color = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES)
	FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
     ]
	favorite_color = forms.ChoiceField(widget=forms.RadioSelect, choices=FAVORITE_COLORS_CHOICES)
	FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
       ]
	favorite_colors = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=FAVORITE_COLORS_CHOICES)
	geeks_field = forms.GenericIPAddressField( )	
	geeks_field = forms.UUIDField( )
	geeks_field = forms.NullBooleanField( )  




