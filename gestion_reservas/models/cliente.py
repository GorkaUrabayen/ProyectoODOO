from odoo import models, fields, api

class Cliente(models.Model):
    _inherit = 'res.partner'
    
    esVip = fields.Boolean(string='Descuento cliente VIP',default=False)
    descuento_vip = fields.Float(string='Descuento VIP', compute='_calcular_descuento')
    reservas = fields.One2many('res.booking','cliente_id',string='Reservas')
    @api.depends('esVip')
    def _caclular_descuento(self):
        # Calcular descuento si el usuario es vip
        for record in self:
            record.descuento_vip = 10.0
