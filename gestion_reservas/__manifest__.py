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
    'depends': ['base','account','calendar'],
    'images': ['static/description/icon.png'],
    'data': [
        'security/ir.model.access.csv',
        'security/reservas_security.xml',
        # Vistas: asegúrate de que el archivo de calendario se cargue antes de las acciones
        'views/reservas_kanban.xml',
        'views/calendario_reservas.xml',  # Archivo con la vista calendario
        'views/actions.xml',
        'views/res_booking_views.xml',
        'views/menu.xml',
        'views/cliente_form.xml',
        'views/calendario_reservas.xml',
        'views/mazmorra_form.xml',
        'views/princesa_form.xml',
        'views/reserva_form.xml',
        'views/service_views.xml'
    ],
    'installable': True,
    'application': True,
}
