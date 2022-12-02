from django.urls import path
from buat_sumbangan.views import *
from buat_sumbangan.views import add_donasi_flutter

app_name='buat_sumbangan'

urlpatterns = [
    path('<int:id_bank>', add_donasi, name='add_donasi'),
    path('history/', show_history, name='show_history'),
    path('json/', donasi_json, name='donasi_json'),
    path('flutter/', add_donasi_flutter, name='add_donasi_flutter'),
]
