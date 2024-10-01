from django import forms
from .models import Netbook, Escuela, Informe, Actividad, Directivo
from django.forms import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class DirectivoForm(forms.ModelForm):

    class Meta:
        model = Directivo
        fields = '__all__'


class NetbookForm(forms.ModelForm):
    estado_pila_choices = (
        ('ok', 'ok'),
        ('agotada', 'agotada'),
        ('cambiada', 'cambiada')
    )
    estado_pila = forms.ChoiceField(
        choices=estado_pila_choices, widget=forms.RadioSelect())
    fecha_expiracion = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}))
    estado_disco_choices = (
        ('llevado', 'llevado'),
        ('flasheado', 'flasheado'),
        ('sin flashear', 'sin flashear')
    )
    estado_disco = forms.ChoiceField(
        choices=estado_disco_choices, widget=forms.RadioSelect())

    Estado_CHOICES = (
        ('ok', 'ok'),
        ('no funciona', 'no funciona'),
        ('falta', 'falta'),
        ('bloqueada', 'bloqueada'),
        ('pendiente de revision', 'pendiente de revision'),
        ('pendiente migracion', 'pendiente migracion'),
        ('robada', 'robada')
    )
    estado = forms.ChoiceField(choices=Estado_CHOICES, widget=forms.RadioSelect())

    class Meta:
        model = Netbook
        fields = '__all__'


class EscuelaForm(forms.ModelForm):

    class Meta:
        model = Escuela
        fields = '__all__'


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class InformeForm(forms.ModelForm):

    class Meta:
        model = Informe
        fields = '__all__'
        exclude = ('autor', 'fecha', 'estado')


class ActividadForm(forms.ModelForm):

    class Meta:
        model = Actividad
        fields = '__all__'
