from django.shortcuts import render
from .forms import ExpenseForm,IncomeForm
from .models import Expense,Income
from .filters import ExpenseFilter,IncomeFilter

def index(response):
    return render(response, "expense/base.html", {})

def home(response):
    return render(response, "expense/home.html", {})

def add_expense(response):
    if response.method == "POST":
        form = ExpenseForm(response.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            a = form.cleaned_data["amount"]
            d = form.cleaned_data["description"]
            response.user.expense_set.create(name=n, amount=a, description=d)
    else:
        form = ExpenseForm()
    return render(response, "expense/addexpense.html", {"form":form})

def add_income(response):
    if response.method == "POST":
        form = IncomeForm(response.POST)
        if form.is_valid():
            a = form.cleaned_data["amount"]
            s = form.cleaned_data["source"]
            response.user.income_set.create(amount=a, source=s)
    else:
        form = IncomeForm()
    return render(response, "expense/addincome.html", {"form":form})

def viewexpense(response):
    ls=Expense.objects.all()
    myFilter = ExpenseFilter(response.GET, queryset=ls)
    ls=myFilter.qs
    contents = {'expenses': ls, 'myFilter': myFilter}
    return render(response, "expense/viewexpense.html", contents)

def viewincome(response):
    rs=Income.objects.all()
    myFilter = IncomeFilter(response.GET, queryset=rs)
    rs=myFilter.qs
    contents = {'incomes': rs, 'myFilter': myFilter}
    return render(response, "expense/viewincome.html", contents)
