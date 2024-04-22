from django.urls import path
from .import views as v

urlpatterns = [w
    path('register',v.adduser, name='reg'),
    # path('login',v.login_view, name='login'),
    # path('logout',v.logout_view, name='logout'),
]
