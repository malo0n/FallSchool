from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


app_name = 'FallSchool'
router = DefaultRouter()
router.register('items', views.ItemViewSet, basename="item-viewset")

urlpatterns = [
    path('first__screen/', views.first__screen, name='first__screen'),
    path('second__screen/', views.second__screen, name='second__screen'),
    path('items/', views.ItemAPIView.as_view(), name='item-view'),
]
urlpatterns += [path(r'api/', include(router.urls))]
print(router.urls)