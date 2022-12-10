from django.urls import path
from authentication.views import *

app_name = 'authentication'

urlpatterns = [
    path('login_flutter/', login_flutter, name='login_flutter'),
    path('signup_reg/', signup_reg_flutter, name='signup_reg_flutter'),
    path('signup_bank/', signup_bank_flutter, name='signup_bank_flutter'),
    path('logout_flutter/', logout_flutter, name='logout_flutter'),
]