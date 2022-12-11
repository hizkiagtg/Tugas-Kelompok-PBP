from django.urls import path
from for_profile.views import *


app_name = 'for_profile'

urlpatterns = [
    path('show_profile/', show_profile, name = 'show_profile'),
    path('edit_profile/', edit_profile, name = 'edit_profile'),
    # path('show_profile_flutter/', show_profile_flutter, name = 'show_profile_flutter'),
    path('edit_reg_flutter/', edit_reg_flutter, name = 'edit_reg_flutter'),
    path('edit_bank_flutter/', edit_bank_flutter, name = 'edit_bank_flutter'),
    path('flutter/<int:id_user>/', user_json_flutter, name='user_json_flutter'),
]
