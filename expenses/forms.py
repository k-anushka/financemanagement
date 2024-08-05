from django import forms
from.models import Xpenses
from.models import MyUser


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Xpenses
        fields = ['name','description','date','amount','category']
        widgets = {
            'date': forms.DateTimeInput(attrs={'type':'date'}),
            'category': forms.Select(choices=Xpenses. CATEGORY_CHOICES),
            'description' : forms.Textarea(attrs={'rows' : 2}),
        }
def clean_amount(self):
        amount = self.cleaned_data.get('amount')
        if amount <= 0:
            raise forms.ValidationError('Amount must be a positive number.')
        return amount


class UserForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ['user_name','password']

   