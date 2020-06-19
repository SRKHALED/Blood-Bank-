from django import forms
from .models import Donor

class DateInput(forms.DateInput):
    input_type = 'date'

class RegForm(forms.ModelForm):
	class Meta:
		model = Donor
		fields = "__all__"
		widgets = {
            'date_of_birth': DateInput(),
        	'password': forms.PasswordInput(),
        }

class SearchForm(forms.Form):
	division = forms.CharField(required = True)
	city = forms.CharField(required = True)
	BT = (('','Blood Group'),('A+','A+'),('B+','B+'),('O+','O+'),('AB+','AB+'),
	 ('A-','A-'),('B-','B-'),('O-','O-'),('AB-','AB-'))
	GD = (('','Choos Gender'),('Male','Male'),('Female','Female'),('Others','Others'))
	gender = forms.ChoiceField(choices = GD)
	blood = forms.ChoiceField(choices = BT)

class LoginForm(forms.Form):
	email = forms.EmailField()
	password = forms.ChoiceField(widget = forms.PasswordInput)