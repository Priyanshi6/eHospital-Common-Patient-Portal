"""eHospital URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp.views import views_alpha

urlpatterns = [
    path('admin/', admin.site.urls),
    path('preg/',views_alpha.preg),
    path('dreg/',views_alpha.dreg),
    path('hreg/',views_alpha.hreg),
    path('docreg/',views_alpha.docreg),
    path('hospitalreg/',views_alpha.hospitalreg),
    path('patientreg/',views_alpha.patientreg),
    path('patientlogin/',views_alpha.patientlogin),
    path('hospitalogin/',views_alpha.hospitalogin),
    path('p_dashboard/',views_alpha.p_dashboard),
    path('patientlog/',views_alpha.patientlog),
    path('patientlogout/',views_alpha.patientlogout),
    path('hospitalog/',views_alpha.hospitalog),
    path('h_dashboard/',views_alpha.h_dashboard),
    path('hospitalogout/',views_alpha.hospitalogout),
    path('p_changepass/',views_alpha.p_changepass),
    path('forgotpass/',views_alpha.forgotpass),
    path('p_confirm/',views_alpha.p_confirm),
    path('p_editpass/',views_alpha.p_editpass),
    path('patient_dashboard/',views_alpha.patient_dashboard),
    path('appointments/',views_alpha.appointments),
    path('bookappointment/',views_alpha.bookappointment),
    path('manage_appointments/',views_alpha.manage_appointment),
    path('d_changepass/',views_alpha.d_changepass),
    path('d_confirm/',views_alpha.d_confirm),
    path('d_editpass/',views_alpha.d_editpass),
    path('doctorlog/',views_alpha.doctorlog),
    path('doctorlogin/',views_alpha.doctorlogin),
    path('d_dashboard/',views_alpha.d_dashboard),
    path('dforgotpass/',views_alpha.dforgotpass),
    path('hforgotpass/',views_alpha.hforgotpass),
]
