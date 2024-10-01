from importlib.resources import path
from django.conf.urls.static import static
from operator import index
from django.conf import settings
from django.urls import path
from .views import *

app_name = 'net'


urlpatterns = [
    path('', index, name='index'),
    path('registro/', registro, name="registro"),
    # ------------netbooks----------------------
    path('agregar-netbook/', agregar_netbook, name='agregar_netbook'),
    path('detalle-netbook/<id>/', detalle_netbook, name='detalle_netbook'),
    path('listar-netbooks/', listar_netbooks, name='listar_netbooks'),
    path('modificar-netbook/<id>/', modificar_netbook, name='modificar_netbook'),
    path('eliminar-netbook/<id>/', eliminar_netbook, name='eliminar_netbook'),
    # ------------Escuelas----------------------------
    path('agregar-escuela/', agregar_escuela, name='agregar_escuela'),
    path('detalle-escuela/<id>/', detalle_escuela, name='detalle_escuela'),
    path('listar-escuelas/', listar_escuelas, name='listar_escuelas'),
    path('modificar-escuela/<id>/', modificar_escuela, name='modificar_escuela'),
    path('eliminar-escuela/<id>/', eliminar_escuela, name='eliminar_escuela'),
    # ------------Directivos----------------------------
    path('agregar-directivo/', agregar_directivo, name='agregar_directivo'),
    path('detalle-directivo/<id>/', detalle_directivo, name='detalle_directivo'),
    path('listar-directivos/', listar_directivos, name='listar_directivos'),
    path('modificar-directivo/<id>/', modificar_directivo, name='modificar_directivo'),
    path('eliminar-directivo/<id>/', eliminar_directivo, name='eliminar_directivo'),
    # -----------------------Informes---------------------------------
    path('agregar-informe/', agregar_informe, name='agregar_informe'),
    path('detalle-informe/<id>/', detalle_informe, name='detalle_informe'),
    path('listar-informes/', listar_informes, name='listar_informes'),
    path('modificar-informe/<id>/', modificar_informe, name='modificar_informe'),
    path('eliminar-informe/<id>/', eliminar_informe, name='eliminar_informe'),
    # ------------------------Reportes--------------------------------
    path('reporte/<id>/', crear_reporte, name='crear_reporte'),
]