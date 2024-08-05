from django.shortcuts import render,redirect
from.forms import ExpenseForm
from .models import Xpenses
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import get_object_or_404
from .models import MyUser
from.forms import UserForm
# Create your views here.

def create_expense(request):
   if request.method == 'POST':      
        form = ExpenseForm(request.POST)
        if form.is_valid():
            user_name = request.session.get('user_name')
            if user_name is None:
                raise Exception("User is not logged in")
            expense = form.save(commit=False)
            expense.created_by=user_name
            expense.save()
        return redirect('../view_expenses/') # redirect to a success page
   else:
       form = ExpenseForm()
   
   return render(request,'expenses.html',{'form':form})


def view_expenses(request):
    user_name = request.session.get('user_name')
    if user_name is None:
                raise Exception("User is not logged in")
    user= get_object_or_404(MyUser,user_name=user_name)
    vexpenses=[]
    if user.role=="member":
       vexpenses=  Xpenses.objects.filter(created_by=user.user_name)
    else:
        vexpenses = Xpenses.objects.all()
    if 'filterdate' in request.GET:
        start_date = request.GET['filterdate']
        vexpenses = vexpenses.filter(date =start_date)
    if 'search' in request.GET:
        search_query = request.GET['search']
        vexpenses = vexpenses.filter(name_icontaions=search_query)  
    
    return render(request,'view_expenses.html',{'vexpenses': vexpenses })


def edit_expense(request,id):
   expense = get_object_or_404(Xpenses,id=id)
   if request.method == 'POST':  
        form = ExpenseForm(request.POST)
        if form.is_valid():
            user_name = request.session.get('user_name')
            if user_name != expense.created_by:
                raise Exception("Expense is created by some other user")
            form.save()
        else:
            raise Exception("Form is not valid")  
        return redirect('../view_expenses') # redirect to a success page
   else: 
       form = ExpenseForm(instance=expense)
   
   return render(request,'edit_expense.html',{'form':form,'expense':expense})


def delete_expense(request,id):
    expense = get_object_or_404(Xpenses,id=id)
    if request.method == 'POST':   
            user_name = request.session.get('user_name')
            if user_name != expense.created_by:
                raise Exception("Expense is created by some other user")  
            expense.delete()
            return redirect('../view_expenses') # redirect to a success page
    
   
    return render(request,'confirm_delete_expense.html',{'expense':expense})

def login_user(request):
     if request.method == 'POST':      
           form = UserForm(request.POST)
           if form.is_valid():
             username=form.cleaned_data.get('user_name')
             password=form.cleaned_data.get('password')
             user= get_object_or_404(MyUser,user_name=form.cleaned_data.get('user_name'),password=password)
             if user is not None:
                 request.session['role'] = user.role
                 request.session['user_name'] = username    
           return redirect('../view_expenses/') # redirect to a success page
     else:
       form = UserForm()
   
     return render(request,'login.html',{'form':form})


def save_user(request):
    if request.method == 'GET':
          admin_data = {
            "user_name": "admin",
            "password": "admin",  # Hash the password
            "role": "admin"
            }
          admin_form = UserForm(admin_data)
          MyUser.objects.filter(user_name="admin").delete()
          if admin_form.is_valid():
            admin_user= admin_form.save(commit=False)
            admin_user.role="admin"
            admin_user.save()
          member_data = {
            "user_name": "member",
            "password": "member",  # Hash the password
            "role": "member"
            }  
          MyUser.objects.filter(user_name="member").delete()
          menberform = UserForm(member_data)
          if menberform.is_valid():
            menberform.save()  
       
    return redirect('../login')
