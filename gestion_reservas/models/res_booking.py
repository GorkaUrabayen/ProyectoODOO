from odoo import models, fields, api

class ResBooking(models.Model):
    _name = 'res.booking'
    _description = 'Reserva de Mazmorra'

    cliente_id = fields.Many2one('res.partner', string="Cliente", required=True)
    fecha_hora = fields.Datetime(string="Fecha y Hora", required=True)
    estado = fields.Selection([
        ('pendiente', 'Pendiente'),
        ('confirmado', 'Confirmado'),
        ('cancelado', 'Cancelado')
    ], string="Estado", default='pendiente')
    precio = fields.Float(string="Precio", compute="_calcular_precio", store=True)
    mazmorra_ids = fields.One2many('res.mazmorra', 'reserva_ids', string="Mazmorras")
    princesa_ids = fields.One2many('res.princesa', 'reserva_id', string="Princesas")
    servicio_ids = fields.Many2many('res.service', string="Servicios")

    @api.depends('servicio_ids')
    def _calcular_precio(self):
        """Calcula el precio total de la reserva basado en los servicios seleccionados."""
        for record in self:
            record.precio = sum(service.precio for service in record.servicio_ids)

    def confirmar_reserva(self):
        """Cambia el estado de la reserva a Confirmado."""
        self.write({'estado': 'confirmado'})

    def cancelar_reserva(self):
        """Cambia el estado de la reserva a Cancelado."""
        self.write({'estado': 'cancelado'})
