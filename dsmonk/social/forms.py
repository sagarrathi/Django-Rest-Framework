from django import forms
from django.core import validators
from django.db.models.deletion import CASCADE
from django.forms import fields, widgets
from social import models

def check_for_small(value):
    if len(value[0].lower()) <2:
        raise forms.ValidationError("Increase your text size")

def check_for_same(value):
    pass

# class UserForm(forms.Form):
#     first_name=forms.CharField(validators=[check_for_small])
#     second_name=forms.CharField()
#     email=forms.EmailField()
#     vemail=forms.EmailField(label="Verify your email")
    
#     bot=forms.CharField(required=False,
#                                 widget=forms.HiddenInput,
#                                 validators=[validators.MaxLengthValidator(0)])


#     def clean_bot(self):
#         bot_t = self.cleaned_data["bot"]
#         print(bot_t)
#         if len(bot_t)>0:
#             raise forms.ValidationError("GOTCHA BOT!")
#         return bot_t

#     def clean(self):
#         all_cleaned_data=super().clean()
#         email=all_cleaned_data['email']
#         vemail=all_cleaned_data['vemail']
        
#         if email !=vemail:
#             raise forms.ValidationError("Email not matchin") 


class UserModelForm(forms.ModelForm):
    class Meta:
        model= models.Users
        fields=['first_name', 'email_id']


from django.contrib.auth.models import User
class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model=User
        fields=('username', 'email','password')
    


from social.models import UserProfileInfo
class UserProfileInfoForm(forms.ModelForm):
    portfolio =forms.URLField(required=True)
    picture=forms.ImageField(required=True)

    class Meta():
        model=UserProfileInfo
        exclude=('user',)