from django import forms
from django.core import validators
from django.contrib.auth.models import User
from hotellu_app.models import UserProfileInfo#,User

# def check_for_a(value):
#     if value[0].lower != 'a':
#         raise forms.ValidationError("NAME NEEDS TO START WITH A")

class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter email again')
    text = forms.CharField(widget = forms.Textarea)
    # botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']

        if email != vmail:
            raise forms.ValidationError("EMAIL DONT MATCH")

'''
    botcatcher = forms.CharField(required = False, widget = forms.HiddenInput)

The below custom method is used to catch the bot, however Django Validators can be used to perform the same
The below will not be used generally and only the custom validators will be used
    def clean_botcatcher(self):
        botcatcher = self.cleaned_data['botcatcher']
        if len(botcatcher) >0:
            raise forms.ValidationError("BOT FOUND")
        return botcatcher'''
#
# class NewUserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = '__all__'

class AuthUserForm(forms.ModelForm):
    password = forms.CharField(widget= forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email','password')


class AuthUserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pics')
