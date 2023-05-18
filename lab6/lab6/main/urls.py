from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('create', views.create, name="create"),
    path('main', views.mainPage, name="main"),
    path('delete_bank/<int:pk>', views.delete_bank, name='delete_bank'),
    path('delete_client/<int:pk>', views.delete_client, name='delete_client'),
    path('delete_sotr/<int:pk>', views.delete_sotr, name='delete_sotr'),
    path('delete_dolzh/<int:pk>', views.delete_dolzh, name='delete_dolzh'),
    path('delete_credit/<int:pk>', views.delete_credit, name='delete_credit'),
    path('delete_count/<int:pk>', views.delete_count, name='delete_count'),
    path('update_bank/<int:pk>', views.redact_bank.as_view(), name='update_bank'),
    path('update_client/<int:pk>', views.redact_client.as_view(), name='update_client'),
    path('update_sotr/<int:pk>', views.redact_sotr.as_view(), name='update_sotr'),
    path('update_dolzh/<int:pk>', views.redact_dolzh.as_view(), name='update_dolzh'),
    path('update_credit/<int:pk>', views.redact_credit.as_view(), name='update_credit'),
    path('update_count/<int:pk>', views.redact_count.as_view(), name='update_count'),
    path('clients', views.clients, name="clients"),
    path('poseschenie', views.poseschenie, name="poseschenie"),
    path('sotrudniki', views.sotrudniki, name="sotrudniki"),
    path('dolzhnosti', views.dolzhnosti, name="dolzhnosti"),
    path('credit', views.credit, name="credit"),
    path('count', views.count, name="count"),
    path('login', views.LoginUser.as_view(), name='auth'),
    path('register', views.RegisterUser.as_view(), name='registr'),
    path('logout', views.logout_user, name='logout')
]