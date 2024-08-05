from django.urls import path
from .  import views
urlpatterns = [
    path('login/', views.login_user, name='login_user'),
    path('register/', views.save_user, name='save_user'),
    path('create_expense/', views.create_expense, name='create_expense'),
    path('view_expenses/', views.view_expenses, name='view_expenses'),
    path('edit_expense/<int:id>', views.edit_expense, name='edit_expense'),
    path('delete_expense/<int:id>', views.delete_expense, name='delete_expense'),
]