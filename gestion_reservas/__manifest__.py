{
    'name': '',
    'version': '1.0',
    'summary': 'Módulo de reservas de mazmorras y princesas',
    'author': 'Gorka Urabaye, Izan Ramos y Paula Iturbide',
    'depends': ['base','account'],
    #Data por definir
    'data': [
        'security/ir.model.access.csv',  # Permisos de acceso a los modelos
        'views/mi_modelo_views.xml',  # Definiciones de vistas
        'data/mi_modelo_data.xml',  # Datos predefinidos
    ],
    'installable': True,
    'application': True,
}
