from django import forms
from .models import Expense,Income


class ExpenseForm(forms.ModelForm):
    name = forms.CharField(label='Expense Name', max_length=100)
    amount = forms.DecimalField(label='Amount', max_digits=10, decimal_places=2)
    description = forms.CharField(max_length=255, required=False)

    class Meta:
        model = Expense
        fields = ['name', 'amount', 'description']

class IncomeForm(forms.ModelForm):
    amount = forms.DecimalField(label='Amount', max_digits=10, decimal_places=2)
    source = forms.CharField(label='Source',max_length=255)

    class Meta:
        model = Income
        fields = ['amount', 'source']        
    

    
          