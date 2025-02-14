from odoo import models, fields, api

class Mazmorra(models.Model):
    _name = 'res.mazmorra'
    _description = 'Mazmorra'

    name = fields.Char(string='Nombre', required=True)
    descripcion = fields.Text(string='Descripción')
    reserva_id = fields.Many2one('res.booking', string='Reserva', ondelete='cascade')
