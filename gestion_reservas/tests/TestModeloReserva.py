from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError

class TestModeloReserva(TransactionCase):
    
    def setUp(self):
        super().setUp()
        # Crear datos de prueba
        self.cliente = self.env['res.partner'].create({
            'name': 'Cliente Test',
            'esVip': True
        })
        self.servicio = self.env['res.service'].create({
            'name': 'Servicio Test',
            'precio': 100,
            'duracion': 30
        })
        self.reserva = self.env['res.booking'].create({
            'cliente_id': self.cliente.id,
            'fecha_hora': '2025-02-19 12:00:00',
        })

    def test_descuento_vip(self):
        # Verificar que el descuento VIP se aplique correctamente
        self.assertEqual(self.cliente.descuento_vip, 10.0)

    def test_calcular_precio(self):
        # Verificar que el precio se calcule correctamente con el descuento
        self.reserva.servicio_ids = [(6, 0, [self.servicio.id])]
        self.reserva._calcular_precio()
        self.assertEqual(self.reserva.precio, 90.0)

    def test_validar_fecha(self):
        # Verificar que no se puedan crear reservas en fechas pasadas
        with self.assertRaises(ValidationError):
            self.env['res.booking'].create({
                'cliente_id': self.cliente.id,
                'fecha_hora': '2020-02-19 12:00:00',
            })

    def test_cancelar_reserva(self):
        # Verificar que las reservas pendientes se cancelen automáticamente
        self.reserva.estado = 'pendiente'
        self.reserva.create({
            'cliente_id': self.cliente.id,
            'fecha_hora': '2025-02-19 12:00:00',
        })
        self.reserva.cancelar_reserva_automatica()
        self.assertEqual(self.reserva.estado, 'cancelada')

    def test_check_precio_negativo(self):
        # Verificar que se lanza un error si el precio es negativo
        with self.assertRaises(ValidationError):
            self.env['res.service'].create({
                'name': 'Servicio con precio negativo',
                'precio': -10,
                'duracion': 30
            })
    
    def test_check_duracion_negativa(self):
        # Verificar que se lanza un error si la duración es negativa
        with self.assertRaises(ValidationError):
            self.env['res.service'].create({
                'name': 'Servicio con duración negativa',
                'precio': 100,
                'duracion': -5
            })
    
    def test_check_nombre_unico_servicio(self):
        # Verificar que no se puedan crear servicios con el mismo nombre
        servicio1 = self.env['res.service'].create({
            'name': 'Servicio Unico',
            'precio': 100,
            'duracion': 30
        })
        with self.assertRaises(ValidationError):
            self.env['res.service'].create({
                'name': 'Servicio Unico',
                'precio': 150,
                'duracion': 45
            })
