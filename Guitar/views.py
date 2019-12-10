from django.shortcuts import render, redirect
from .models import Guitarra, Baixo, Funcionario, Bateria
from django.contrib.auth.models import User
from .forms import FormularioGuitarra, FormularioBaixo, FormularioBateria, FormularioFuncionario, ComprarGuitarraForm, ComprarBaixoForm, ComprarBateriaForm


def home(request):
	return render(request, 'Guitar/base.html')

def lista(request):
	lista_guitarra = Guitarra.objects.all()
	return render(request, 'Guitar/lista_guitarra.html', {'lista' : lista_guitarra})

def lista_baixo(request):
	lista_baixo =  Baixo.objects.all()
	return render(request, 'Guitar/lista_baixo.html', {'lista_baixo': lista_baixo})

def lista_bateria(request):
	lista_bateria = Bateria.objects.all()
	return render(request, 'Guitar/lista_bateria.html', {'lista_bateria' : lista_bateria})

def lista_funcionario(request):
	lista_funcionario = Funcionario.objects.all()
	return render(request, 'Guitar/lista_Funcionarios.html', {'lista_funcionario' : lista_funcionario})

def Comprar_Guitarra(request):
	form = ComprarGuitarraForm(request.POST or None)

	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return redirect(Comprar_Guitarra)


	return render(request, 'Guitar/comprar_guitar.html', {'form': form})

def Comprar_Baixo(request):
	formL = ComprarBaixoForm(request.POST or None)

	if request.method == 'POST':
		if formL.is_valid():
			formL.save()
			return redirect(Comprar_Baixo)


	return render(request, 'Guitar/comprar_baixo.html', {'formL': formL})

def Comprar_Bateria(request):
	formB = ComprarBateriaForm(request.POST or None)

	if request.method == 'POST':
		if formB.is_valid():
			formB.save()
			return redirect(Comprar_Bateria)


	return render(request, 'Guitar/comprar_bateria.html', {'formB': formB})


def informacoes(request):
	return render(request, 'Guitar/informacoes.html')
