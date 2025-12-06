from django.urls import path
from . import views

urlpatterns = [
    path('user/signUp', views.signup, name='signup'),
    path('user/signIn', views.signin, name='signin'),
    path('user/dashboard', views.dashboard, name='dashboard'),
    path('user/logout', views.logout_view, name='logout'),
    
    path('submit', views.submit_resume, name='submit'),
    path('form/index', views.resume_form, name='resume_form'),
    
    path('getData/<str:template_name>', views.view_resume, name='view_resume'),
    
    # Initial redirect or home?
    # app.js mapping: /template2/pages/about
    path('<str:template_name>/pages/<str:page>', views.template_page, name='template_page'),
    
    path('admin/adminDashboard', views.admin_dashboard, name='admin_dashboard'),
    path('admin/adminSignIn', views.admin_signin, name='admin_signin'),
]
