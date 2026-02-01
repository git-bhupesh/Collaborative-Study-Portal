from django.contrib.auth.forms import UserCreationForm
from django import forms
from . models import *
from .models import Profile

class UserRegForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists")
        return email


    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'username',
            'password1',
            'password2'
        ]

class DateInput(forms.DateInput):
    input_type = 'date'

class NoteDescForm(forms.ModelForm):
    # this function is used to make notes while studying - update, delete, mark as done are it's functionalities
    class Meta:
        model = Notes
        fields = ['title', 'desc']

class HwForm(forms.ModelForm):
    # this function is used to keep track of HW while studying - update, delete, mark as done are it's functionalities
    class Meta:
        model = Homework
        widgets = {'due':DateInput()}
        fields = ['subject', 'title', 'desc', 'due', 'is_finished']

class DashboardForm(forms.Form):
    text = forms.CharField(max_length = 100, label = "Enter To Search ")

class TodoForm(forms.ModelForm):
    # TODO list - things to be done!
    class Meta:
        model = Todo
        fields = ['title', 'desc', 'is_finished']

class ConversationForm(forms.Form):
    # works like a calculator
    CHOICES = [('length', 'Length'), ('mass', 'Mass')]
    measurement = forms.ChoiceField(choices = CHOICES, widget = forms.RadioSelect)

class MassConversion(forms.Form) :
    CHOICES= [('pound', 'Pound'), ('kg', 'Kg' )]
    input = forms.CharField (required=False, label=False, widget=forms.TextInput(
    attrs = {'type': 'number', 'placeholder' : "Enter the Number"}))
    measure1 = forms.CharField (
        label= '', widget = forms.Select(choices = CHOICES)
    )
    measure2 = forms.CharField(
        label='', widget = forms.Select (choices = CHOICES)
    )

class LengthConversion(forms.Form) :
    CHOICES= [('yard', 'Yard'), ('foot', 'Foot' )]
    input = forms.CharField (required=False, label=False, widget=forms.TextInput(
    attrs = {'type': 'number', 'placeholder' : "Enter the Number"}))
    measure1 = forms.CharField (
        label= '',widget = forms.Select(choices = CHOICES)
    )
    measure2 = forms.CharField(
        label='',widget = forms.Select (choices = CHOICES)
    )
    print("\nIt's working!", measure1 , measure2)



class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']  # No more error here!
        
    # Optional: Styling the image field to match your SaaS look
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].widget.attrs.update({'class': 'form-control-file'})