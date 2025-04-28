from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar_carro/', views.cadastrar_carro, name="cadastrar_carro"),
    path('deletar_carro/<int:id>', views.deletar_carro, name="deletar_carro"),
    path('atualizar_carro/<int:id>', views.atualizar_carro, name="atualizar_carro")
]