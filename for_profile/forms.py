from django import forms
from accounts.models import User

class EditProfileFormReg(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'name', 'age', 'gender', 'city']




class EditProfileFormBank(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email','city', 'address']

            


        


