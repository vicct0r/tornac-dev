from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.HomePageTemplateView.as_view(), name='home'),
    path('projetos/novo/', views.AplicativoCreateView.as_view(), name='create'),
    path('projetos/<int:pk>/atualizar/', views.AplicativoUpdateView.as_view(), name='update'),
    path('projetos/<int:pk>/apagar/', views.AplicativoDeleteView.as_view(), name='delete'),
]