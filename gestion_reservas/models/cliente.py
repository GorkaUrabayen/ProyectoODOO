from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    es_vip = fields.Boolean(string="Cliente VIP", compute="_compute_es_vip")
    descuento_vip = fields.Float(string="Descuento VIP", compute="_compute_descuento_vip")

    @api.depends('category_id')
    def _compute_es_vip(self):
        for record in self:
            record.es_vip = any(category.name == 'VIP' for category in record.category_id)

    @api.depends('es_vip')
    def _compute_descuento_vip(self):
        for record in self:
            if record.es_vip:
                record.descuento_vip = 10.0  # 10% de descuento
            else:
                record.descuento_vip = 0.0
