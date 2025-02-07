from odoo import models, fields, api

class Reserva(models.Model):
    _name = 'res.booking'
    _description = 'Reservas de Mazmorras'
    
    cliente_id = fields.Many2one('res.partner',string='Cliente',required=True)
    servicio_id = fields.Many2one('res.service',string='Servicio',required=True)
    fecha_y_hora= fields.DateTime(string='Fecha y hora')
    
    estado = fields.Selection([
        ('pendiente','Pendiente'),
        ('confirmada','Confirmada'),
        ('cancelada','Cancelada')
    ], string='Estado',default='pendiente')
    
    precio = fields.Float(string='Precio',compute='_calcular_precio',store=True)
    factura_id = fields.Many2one('account.move',string='Factura',readonly=True)
    
    mazmorra_ids = fields.One2Many('res.mazmorra', string='Mazmorras')
    princesa_ids = fields.One2Many('res.princesa', string='Princesas')
    servicio_ids = fields.Many2many('res.servicio', string='Servicios')
    fecha_hora = fields.Datetime(string='Fecha y Hora', required=True)
    
    # Funciones de calculo de precio y confirmar reservas
    @api.depends('servicio_ids','cliente_ids')
    def _calcular_precio(self):
        for record in self:
            precio_base= record.servicio_id.precio
            descuento = record.cliente_id._caclular_descuento
            record.precio = precio_base * (1-descuento)
    def confirmar_reserva(self):
        for record in self:
            return