from django.conf.urls import include, url
from . import views


urlpatterns = [
	url(r'^$', views.home, name='Home'),
	url(r'^lista_guitarra/$', views.lista, name='lista_guitarra'), 
	url(r'^Listar_baixo/$', views.lista_baixo, name="Listar_baixo"),
	url(r'^Listar_bateria/$', views.lista_bateria, name="Listar_bateria"),
	url(r'^Listar_funcionarios/$', views.lista_funcionario, name="Listar_funcionarios"),
	url(r'^Comprar_guitar/$', views.Comprar_Guitarra, name="Comprar_guitar"),
	url(r'^Comprar_baixo/$', views.Comprar_Baixo, name="Comprar_baixo"),
	url(r'^Comprar_bateria/$', views.Comprar_Bateria, name="Comprar_bateria"),
	url(r'^rock/$', views.informacoes, name="rock"),
		
 ]