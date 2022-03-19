from django.conf import settings
from django.conf.urls import static
from django.contrib import admin
from django.urls import path
from home import views
from django.conf import settings
from django.conf.urls.static import static
admin.site.site_header = "KU Project"
admin.site.site_title = "KU Project PHD thesis"
admin.site.index_title = "KU Project PHD thesis"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('instruction', views.instruction, name='2b'),
    path('login', views.login, name='3'),
    path('validate', views.validate, name='4'),
    path('success', views.success, name='5'),
    path('status', views.status, name='2a'),
    path('register', views.register),
    path('', views.check, name='1'),
    path('certificate', views.certificate, name="2a1"),
    path('delete', views.delete, name='2a2'),
    path('payverify', views.payverify, name='anonym'),
    path('paydetails', views.paydetails, name='anonym1'),
    path('paylogin', views.paylogin, name='flogin'),
    path('logverify', views.logverify, name='payverify'),
    path('test', views.test, name='test'),
    path('adminlogin', views.adminlogin),
    path('printform', views.printform, name='printform'),
    path('Approveds', views.ApprovedList, name='ApprovedList'),
    path('forgot', views.forgot),
    path('change', views.change),
    path('home', views.home),
    path('bcvdlogin', views.bcvdlogin),
    path('bcvdverify', views.bcvdverify),
    path('bosfill', views.bosfill),
    path('coelogin', views.coelogin),
    path('vclogin', views.vclogin),
    path('deptlogin', views.deptlogin),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
