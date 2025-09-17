from django import forms
from .models import Expense, CATEGORY_CHOICES

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = '__all__'
        widgets = {
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'จำนวนเงิน'}),
            'category': forms.Select(choices=CATEGORY_CHOICES, attrs={'class': 'form-control'}),
            'note': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'รายละเอียดเพิ่มเติม'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
