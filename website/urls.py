from django.urls import path
from .import views as v

urlpatterns = [
    path('',v.home, name='home'),
    path('about/', v.about, name='about'),
    path('indexx/', v.indexx, name='indexx'),
    path('base/', v.base, name='base'),
    path('contact/', v.contact, name='contact'),
    path('success/', v.success, name='sucess'),
    path('test/', v.subform, name='subform'),
    path('modelform/', v.modelfrm, name='modelfrm'),
    path('register/', v.register, name='register'),
    path('login/', v.uslogin, name='login'),
    path('logout/', v.uslogout, name='logout'),
    path('additem/', v.additem, name='additem'),
    path('display/', v.display, name='display'),
    path('item/<int:pk>/delete', v.delt, name='delt'),
    path('item/<int:pk>/edit', v.editt, name='editt'),

   
]
