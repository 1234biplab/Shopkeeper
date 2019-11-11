from django.urls import path
from . import views as cus_views
urlpatterns =[
    path('',cus_views.customer_dashboard, name='dashboard'),
    path('signup/',cus_views.customer_signup, name='signup'),
    path('customers/',cus_views.show_customer, name='all_customers'),
    path('update/<int:id>/',cus_views.update_customer, name='update_customer'),
    path('delete/<int:id>/',cus_views.delete_customer, name='delete_customer'),
    path('exa/',cus_views.matltiplae, name='exa'),

]
