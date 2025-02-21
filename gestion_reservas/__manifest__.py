{
    'name': 'Gestión de Mazmorras y Reservas',
    'version': '1.0',
    'summary': 'Gestiona mazmorras, reservas y princesas',
    'description': """
        Este módulo permite gestionar reservas de mazmorras, 
        incluyendo clientes VIP, princesas y servicios.
    """,
    'category': 'Services',
    'author': 'Gorka Urabayen, Izan Ramos y Paula Iturbide',
    'depends': ['base', 'account'],
    'images': ['static/description/icon.png'],
    'data': [
        'security/ir.model.access.csv',
        'security/reservas_security.xml',
        # Vistas
        'views/reservas_mazmorras_menus.xml',  # Menús principales
        'views/reservas_mazmorras_views.xml',  # Vistas generales
        'views/res_booking_views.xml',         # Vistas de reservas
        'views/res_princesa_views.xml',        # Vistas de princesas
        'views/res_mazmorra_views.xml',        # Vistas de mazmorras
        'views/res_service_views.xml',         # Vistas de servicios
        'views/res_partner_views.xml',         # Vistas de clientes
    ],
    'installable': True,
    'application': True,
}
