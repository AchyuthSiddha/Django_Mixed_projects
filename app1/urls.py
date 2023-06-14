from django.urls import path
from app1.views import *

app_name='app1'

urlpatterns=([
    # path('Achyuth/',Achyuth,name='Achyuth'),
    # path('Krishna/',Krishna,name='Krishna'),
    # path('FirstPage/',FirstPage,name='FirstPage'),
    # path('CSK/',CSK,name='CSK'),
    # path('Achyuth/',Achyuth,name='Achyuth'),
    # path('Dhoni/',Dhoni,name='Dhoni'),
    # path('Raina/',Raina,name='Raina'),
    
    path('Insert_image/',Insert_image,name='Insert_image'),
])