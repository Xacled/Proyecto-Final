from django.urls import path
from . import views

app_name = 'comentarios'

urlpatterns = [
  	path('agergar/<int:pk>',views.Agregar_Comentario, name = 'agregar'),
  	path('Borrar/<int:pk>', views.BorrarComentario.as_view(), name="borrar_comentario"),
	path('Modificar/<int:pk>', views.ModificaComentario.as_view(), name="modificar_comentario"),
]