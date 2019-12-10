from django import forms
from .models import Guitarra, Funcionario, Baixo, Bateria, ComprarGuitarra, ComprarBaixo, ComprarBateria

class FormularioGuitarra(forms.ModelForm):
	class Meta:
		model = Guitarra
		exclude = ['']

class FormularioBaixo(forms.ModelForm):
	class Meta:
		model = Baixo
		
		exclude=['']

class FormularioBateria(forms.ModelForm):
	class Meta:
		model = Bateria
		
		exclude=['']
		
class FormularioFuncionario(forms.ModelForm):
	class Meta:
		model = Funcionario
		
		exclude=['']

class ComprarGuitarraForm(forms.ModelForm):
	class Meta:
		model = ComprarGuitarra
		
		exclude=['']

class ComprarBaixoForm(forms.ModelForm):
	class Meta:
		model = ComprarBaixo
		
		exclude=['']

class ComprarBateriaForm(forms.ModelForm):
	class Meta:
		model = ComprarBateria
		
		exclude=['']