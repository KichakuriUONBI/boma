from django.shortcuts import render, redirect
from .forms import IncomeForm, ExpenseForm, CattleForm, CattleEventForm
from .models import Income, Expense, Cattle, CattleEvent

def home(request):
    return render(request, 'boma/home.html')

def add_income(request):
    if request.method == 'POST':
        form = IncomeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = IncomeForm()
    return render(request, 'boma/add_income.html', {'form': form})

def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ExpenseForm()
    return render(request, 'boma/add_expense.html', {'form': form})

def add_cattle(request):
    if request.method == 'POST':
        form = CattleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CattleForm()
    return render(request, 'boma/add_cattle.html', {'form': form})

def add_cattle_event(request):
    if request.method == 'POST':
        form = CattleEventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CattleEventForm()
    return render(request, 'boma/add_cattle_event.html', {'form': form})