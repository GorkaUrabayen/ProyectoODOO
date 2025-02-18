{
    'name': 'Gestión de Mazmorras y Reservas',
    'version': '1.0',
    'description': """
        Este módulo permite gestionar reservas de mazmorras, 
        incluyendo clientes VIP, princesas y servicios.
    """,
    'category': 'Services',
    'summary': 'Módulo de reservas de mazmorras y princesas',
    'author': 'Gorka Urabayen, Izan Ramos y Paula Iturbide',
    'depends': ['base','account'],
    'images': ['static/description/icon.png'],
    'data': [
        'security/ir.model.access.csv',
        'security/reservas_security.xml',
        'views/menu.xml'

    ],
    'installable': True,
    'application': True,
}
