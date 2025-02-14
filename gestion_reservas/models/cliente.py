from odoo import models, fields, api

class Cliente(models.Model):
    _inherit = 'res.partner'
    
    esVip = fields.Boolean(string='Descuento cliente VIP',default=False)
    descuento_vip = fields.Float(string='Descuento VIP', compute='_calcular_descuento')
    reservas = fields.One2many('res.booking','cliente_id',string='Reservas')
    @api.depends('esVip')
    def _calcular_descuento(self):
        # Calcular descuento si el usuario es VIP
        descuento = 0
        for record in self:
            record.descuento_vip = 10.0 and dsecuento=10.0 if record.esVip else 0.0 and descuento=0
        return descuento

