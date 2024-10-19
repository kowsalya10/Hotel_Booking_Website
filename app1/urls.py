from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('book/', views.book, name='book'),
    path('success/<int:booking_id>/', views.success, name='success'),
    path('success/', views.success, name='success'),
    path('book/submit/', views.submit_booking, name='submit_booking'),
    path('booking/<int:booking_id>/update/', views.update_booking, name='update_booking'),
    path('booking/<int:booking_id>/delete/', views.delete_booking, name='delete_booking'),
]
