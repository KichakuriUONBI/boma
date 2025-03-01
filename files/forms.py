from django import forms
from .models import Income, Expense, Cattle, CattleEvent

class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = '__all__'

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = '__all__'

class CattleForm(forms.ModelForm):
    class Meta:
        model = Cattle
        fields = '__all__'

class CattleEventForm(forms.ModelForm):
    class Meta:
        model = CattleEvent
        fields = '__all__'