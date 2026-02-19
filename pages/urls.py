from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.HomePageTemplateView.as_view(), name='home'),
    path('novo/', views.AplicativoCreateView.as_view(), name='create'),
    path('<int:pk>/atualizar/', views.AplicativoUpdateView.as_view(), name='update'),
    path('<int:pk>/apagar/', views.AplicativoDeleteView.as_view(), name='delete'),
]