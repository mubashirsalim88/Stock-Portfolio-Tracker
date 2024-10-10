from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from portfolio.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', portfolio_view, name='portfolio_view'),
    path('delete/<int:stock_id>/', delete_stock, name='delete_stock'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('update/<int:stock_id>/', update_stock, name='update_stock'),
    path('add/', add_stock, name='add_stock'),

]