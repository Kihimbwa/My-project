from django import forms
from django.contrib.auth.models import User
from .models import Member, BorrowRecord

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['member_id', 'phone', 'address']


class BorrowForm(forms.ModelForm):
    class Meta:
        model = BorrowRecord
        fields = ['expected_return_date']
        widgets = {
            'expected_return_date': forms.DateInput(attrs={'type': 'date'})
        }

