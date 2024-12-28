from django.urls import path
from . import views

urlpatterns = [
    path('', views.portfolio_view),
    path('detailsview/<int:user_id>/', views.detailsview, name="details"),
    path('updateview/<int:user_id>/', views.updateuser,name="update"),
]
