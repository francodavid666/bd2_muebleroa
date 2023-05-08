from django.contrib import admin
from .views import * 
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from django.urls import re_path
from django.views.static import serve



urlpatterns =[
    path('',inicio,name='inicio'),
    #path('refresh/',refresh,name='refresh'),
    path('delete/<id>',delete,name='delete'),
    #path('inicio_za/',inicio_za,name='inicio_za'),
    path('inicio_mascaro/',inicio_mascaro,name='inicio_mascaro'),
    path('inicio_masbarato/',inicio_masbarato,name='inicio_masbarato'),
    path('inicio_caracteristicas/',inicio_caracteristicas,name='inicio_caracteristicas'),
    path('inicio_refresh/',inicio_refresh,name='inicio_refresh'),
    path('inicio_propiedades/',inicio_propiedades,name='inicio_propiedades'),
    path('propiedades_za/',propiedades_za,name='propiedades_za'),
    
    #formulario
    path('form_add/',form_add,name='form_add'),
    path('form_edit/<id>',form_edit,name='form_edit'),
    
    
    #direccion

    path('dueño_az/',dueño_az,name='dueño_az'),
    path('dueño_za/',dueño_za,name='dueño_za'),
    
    
    path('direccion_az/',direccion_az,name='direccion_az'),
    path('direccion_za/',direccion_za,name='direccion_za'),
    
    
    path('localidad_za/',localidad_za,name='localidad_za'),
    path('localidad_az/',localidad_az,name='localidad_az'),
    
    
    path('estado_az/',estado_az,name='estado_az'),
    path('estado_za/',estado_za,name='estado_za'),
    
    path('propiedad_az/',propiedad_az,name='propiedad_az'),
    path('propiedad_za/',propiedad_za,name='propiedad_za'),
    
    path('tipo_az/',tipo_az,name='tipo_az'),
    path('tipo_za/',tipo_za,name='tipo_za'),
    
    path('precio_az/',precio_az,name='precio_az'),
    path('precio_za/',precio_za,name='precio_za'),
    
    path('descripcion_az/',descripcion_az,name='descripcion_az'),
    path('descripcion_za/',descripcion_za,name='descripcion_za'),
  #CATASTRALES
    path('catastrales_dueño_az/',catastrales_dueño_az,name='catastrales_dueño_az'),
    path('catastrales_dueño_za/',catastrales_dueño_za,name='catastrales_dueño_za'),
    
    path('catastrales_localidad_za/',catastrales_localidad_za,name='catastrales_localidad_za'),
    path('catastrales_localidad_az/',catastrales_localidad_az,name='catastrales_localidad_az'),
    
    path('catastrales_estado_az/',catastrales_estado_az,name='catastrales_estado_az'),
    path('catastrales_estado_za/',catastrales_estado_za,name='catastrales_estado_za'),
    
    path('catastrales_tipo_az/',catastrales_tipo_az,name='catastrales_tipo_az'),
    path('catastrales_tipo_za/',catastrales_tipo_za,name='catastrales_tipo_za'),
    
    
    path('catastrales_precio_az/',catastrales_precio_az,name='catastrales_precio_az'),
    path('catastrales_precio_za/',catastrales_precio_za,name='catastrales_precio_za'),
    
    
    path('ambiente_az/',ambiente_az,name='ambiente_az'),
    path('ambiente_za/',ambiente_za,name='ambiente_za'),

    path('baños_az/',baños_az,name='baños_az'),
    path('baños_za/',baños_za,name='baños_za'),
    
    path('cocina_az/',cocina_az,name='cocina_az'),
    path('cocina_za/',cocina_za,name='cocina_za'),
    
    
    path('dormitorios_az/',dormitorios_az,name='dormitorios_az'),
    path('dormitorios_za/',dormitorios_za,name='dormitorios_za'),
    
    path('living_az/',living_az,name='living_az'),
    path('living_za/',living_za,name='living_za'),
    
    path('garage_az/',garage_az,name='garage_az'),
    path('garage_za/',garage_za,name='garage_za'),
    
    path('sotano_az/',sotano_az,name='sotano_az'),
    path('sotano_za/',sotano_za,name='sotano_za'),
    
    path('terrasa_az/',terrasa_az,name='terrasa_az'),
    path('terrasa_za/',terrasa_za,name='terrasa_za'),
    
]+ static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

urlpatterns += [                    #serve
    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    }),
]
