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
        # Cron job para cancelar reservas automáticamente
        'data/cron.xml',
        # Vistas
        'views/actions.xml',
        'views/menu.xml',
        'views/cliente_form.xml',
        'views/mazmorra_form.xml',
        'views/princesa_form.xml',
        'views/reserva_form.xml',
        'views/servicio_form.xml'
    ],
    'installable': True,
    'application': True,
}
