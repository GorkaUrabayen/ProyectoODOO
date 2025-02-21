from odoo import models, fields, api

class Cliente(models.Model):
    _inherit = 'res.partner'

    esVip = fields.Boolean(string='Descuento cliente VIP',default=False)
    descuento_vip = fields.Float(string='Descuento VIP', compute='_calcular_descuento')
    reservas = fields.One2many('res.booking', 'cliente_id', string='Reservas')
    @api.onchange('esVip')
    def _onchange_esVip(self):
        for record in self:
            if record.esVip:
                record.descuento_vip = 10.0
            else:
                record.descuento_vip = 0.0