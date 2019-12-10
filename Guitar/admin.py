from django.contrib import admin
from .models import Guitarra
from .models import Funcionario 
from .models import Baixo 
from .models import Bateria
from .models import ComprarGuitarra
from .models import ComprarBaixo
from .models import ComprarBateria
from .models import Pagamento
from .models import Cliente_Guitar
from .models import Cliente_Baixo
from .models import Cliente_Bateria



class GuitarAdmin(admin.ModelAdmin):
	model =	Guitarra
	list_display = ('nome', 'valor', 'estoque')
	search_fields = ['nome', 'valor', 'estoque']

class FuncionarioAdmin(admin.ModelAdmin):
	model =	Funcionario
	list_display = ('nome', 'funcao', 'idade', 'salario', 'cpf', 'rg', 'sexo')
	search_fields = ['nome','funcao','idade', 'salario', 'cpf', 'rg', 'sexo']

class BaixoAdmin(admin.ModelAdmin):
	model =	Baixo
	list_display = ('nome', 'valor', 'estoque')
	search_fields = ['nome', 'valor', 'estoque']

class BateriaAdmin(admin.ModelAdmin):
	model =	Bateria
	list_display = ('nome', 'valor', 'estoque')
	search_fields = ['nome', 'valor', 'estoque']

class ComprarGuitarraAdmin(admin.ModelAdmin):
	model =	ComprarGuitarra
	list_display = ('nome_comprador', 'quantidade_guitar')
	search_fields = ['nome_comprador', 'quantidade_guitar']

class ComprarBaixoAdmin(admin.ModelAdmin):
	model =	ComprarBaixo
	list_display = ('nome_comprador','quantidade_baixo')
	search_fields = ['nome_comprador', 'quantidade_baixo']

class ComprarBateriaAdmin(admin.ModelAdmin):
	model =	ComprarBateria
	list_display = ('nome_comprador','quantidade_drum')
	search_fields = ['nome_comprador','quantidade_drum']

class PagamentoAdmin(admin.ModelAdmin):	
	model =	Pagamento
	list_display = ('forma_pagamento', 'descricao')
	search_fields = ['forma_pagamento']

class Cliente_GuitarAdmin(admin.ModelAdmin):
	model =	Cliente_Guitar
	list_display = ('nome_guitar','repeat')
	search_fields = ['nome_guitar','repeat']

class Cliente_BaixoAdmin(admin.ModelAdmin):
	model =	Cliente_Baixo
	list_display = ('nome_baixo','repeat')
	search_fields = ['nome_baixo','repeat']

class Cliente_BateriaAdmin(admin.ModelAdmin):
	model =	Cliente_Bateria
	list_display = ('nome_drum','repeat')
	search_fields = ['nome_drum','repeat']



admin.site.register(Guitarra, GuitarAdmin)
admin.site.register(Funcionario, FuncionarioAdmin)
admin.site.register(Baixo, BaixoAdmin)
admin.site.register(Bateria, BateriaAdmin)
admin.site.register(ComprarGuitarra, ComprarGuitarraAdmin)
admin.site.register(ComprarBaixo, ComprarBaixoAdmin)
admin.site.register(ComprarBateria, ComprarBateriaAdmin)
admin.site.register(Pagamento, PagamentoAdmin)
admin.site.register(Cliente_Guitar, Cliente_GuitarAdmin)
admin.site.register(Cliente_Baixo, Cliente_BaixoAdmin)
admin.site.register(Cliente_Bateria, Cliente_BateriaAdmin)