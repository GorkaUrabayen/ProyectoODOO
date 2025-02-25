from odoo import models, fields, api
from datetime import datetime, timedelta

class Reserva(models.Model):
    _name = 'res.booking'
    _description = 'Reservas de Mazmorras'
    
    cliente_id = fields.Many2one('res.partner', string='Cliente', required=True)
    fecha_hora = fields.Datetime(string='Fecha y Hora', required=True)
    
    estado = fields.Selection([
        ('pendiente', 'Pendiente'),
        ('confirmada', 'Confirmada'),
        ('cancelada', 'Cancelada')
    ], string='Estado', default='pendiente')
    
    precio = fields.Float(string='Precio', compute='_calcular_precio', store=True)
    factura_id = fields.Many2one('account.move', string='Factura', readonly=True)
    
    # Cambiar a Many2many
    mazmorra_ids = fields.Many2many('res.mazmorra', string='Mazmorras Asociadas')
    princesa_ids = fields.Many2many('res.princesa', string='Princesas Asociadas')

    servicio_ids = fields.Many2many('res.service', string='Servicios')

    @api.depends('servicio_ids', 'cliente_id')
    def _calcular_precio(self):
        for record in self:
            precio_total = sum(record.servicio_ids.mapped('precio_servicio'))
            descuento = (record.cliente_id.descuento_vip / 100) if record.cliente_id.descuento_vip > 0 else 0.0
            record.precio = precio_total * (1 - descuento)
    
    def confirmar_reserva(self):
        for record in self:
            if record.estado == 'pendiente' and all(servicio.disponible for servicio in record.servicio_ids):
                record.estado = 'confirmada'
                record._generar_factura()

    def _generar_factura(self):
        for record in self:
            if not record.servicio_ids:
                continue
            factura = self.env['account.move'].create({
                'partner_id': record.cliente_id.id,
                'move_type': 'out_invoice',
                'invoice_line_ids': [(0, 0, {
                    'name': ', '.join(record.servicio_ids.mapped('name')),
                    'quantity': 1,
                    'price_unit': record.precio,
                })]
            })
            record.factura_id = factura.id

    def cancelar_reserva_automatica(self):
        limite = datetime.now() - timedelta(hours=24)
        reservas_pendientes = self.search([
            ('estado', '=', 'pendiente'),
            ('create_date', '<', limite)
        ])
        reservas_pendientes.write({'estado': 'cancelada'})

    @api.model
    def cancelar_reserva(self):
        self.cancelar_reserva_automatica()
    
    @api.constrains('fecha_hora')
    def _validar_fecha(self):
        for record in self:
            if record.fecha_hora < fields.Datetime.now():
                raise models.ValidationError('No se pueden hacer reservas en fechas pasadas.')
