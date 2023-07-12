from django.urls import path
from api.views import TaskListCreateView, TaskRetrieveUpdateDestroyView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('tasks/', TaskListCreateView.as_view(), name='task-list'),
    path('tasks/<int:pk>/', TaskRetrieveUpdateDestroyView.as_view(),
         name='task-detail'),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), 
         name='docs'),
]
