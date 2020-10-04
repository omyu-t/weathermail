from django.urls import path
from .views import Register, delete, registercomp, deletecomp, update, loginfunc, logoutfunc

urlpatterns = [
    path('', Register.as_view(), name='register'),
    path('delete/<int:pk>', delete, name='delete'),
    path('register_comp/', registercomp, name='register_comp'),
    path('delete_comp/', deletecomp, name='delete_comp'),
    path('update/<int:pk>', update, name='update'),
    #path('login/', Login.as_view(), name='login'),
    path('login/', loginfunc, name='login'),
    path('logout/', logoutfunc, name='logout'),
    #path('signup/', signupfunc, name='signup'),
]
