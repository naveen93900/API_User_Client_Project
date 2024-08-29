from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClientViewSet, ProjectViewSet, UserProjectsView

router = DefaultRouter()
router.register(r'clients', ClientViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('clients/<int:client_id>/projects/', ProjectViewSet.as_view({'post': 'create'}), name='client-projects'),
    path('projects/', UserProjectsView.as_view(), name='user-projects'),
]
