from . import views
from django.urls import path
urlpatterns=[
    path('',views.index,name='index.html'),
    path('home',views.index,name='index.html'),
    path('data',views.datatable,name='table-datatable.html'),
    path('profile',views.profile,name='app-profile.html'),
    path('form',views.formedit,name='form-validation.html'),
    path('alldata',views.widgets,name='widgets.html'),
    path('404',views.page404,name='page-error-404.html'),
    path('403',views.page403,name='page-error-403.html'),
    path('400',views.page400,name='page-error-400.html'),
    path('500',views.page500,name='page-error-500.html'),
    path('503',views.page503,name='page-error-503.html'),
    path('lock',views.pagelock,name='page-lock.html'),
    path('login',views.login,name='page-login.html'),
    path('logout',views.logout,name='page-logout.html'),
    path('register',views.signup,name='page-register.html'),

]