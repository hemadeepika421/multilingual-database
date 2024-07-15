from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('index2.html',views.index2, name="index"),
    path('index',views.index, name="index"),
    path('admin1',views.admin_page, name="admin_page"),
    path('admin1/contacts',views.contacts, name="contacts"),
    path('admin1/del_contacts/<int:id>',views.delcont, name="delete_contacts"),
    path('sindhi/',views.main_page, name="sindhi"),
    path('literary/<int:id>',views.main_page_id, name="sindhi1"),
    path('northeast/',views.Northeast, name="northeast"),
    path('malayalam/',views.Malayalam, name="malayalam"),
    path('literaryDesc/<int:id>',views.sindhidesc, name="sindhidesc"),
    path('northeast/<int:id>',views.northeastdesc, name="northeastdesc"),
    path('malayalam/<int:id>',views.malayalamdesc, name="malayalamdesc"),
    path('textextract',views.textextr,name="textextr")
]