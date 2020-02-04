from django.urls import path, include
from reservations import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'tables', views.TableViewSet)
router.register(r'time', views.TimestartViewSet)
router.register(r'avail', views.AvailViewSet)

app_name= 'reservation'
urlpatterns = [
    path('', views.home, name='home'),
    path('reservation/listapi/', include(router.urls), name='listapi'),
    path('reservation/list/', views.reservation_list2, name='list'),
    path('reservation/list/<str:date>/', views.reservation_list_date, name='list_date'),
    path('reservation/update/', views.reservation_update, name='update'),
    path('reservation/detail/', views.reservation_detail, name='detail'),
    path('reservation/delete/', views.reservation_delete, name='delete'),
]