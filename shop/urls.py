from django.urls import path
from .views import Account_Register, Account_Detail,Account_List,delete,Account_Update

app_name = 'shop'

urlpatterns =[
    path('Account_List',Account_List, name='Account_List'),
    path('Account_Register/',Account_Register, name='Account_Register'),
    path('Account_Detail/<int:pk>/',Account_Detail, name='Account_Detail'),
    path('delete/<int:pk>/', delete, name='delete'),
    path('Account_Update/<int:pk>/',Account_Update, name='Account_Update'),
]

