from odoo import models, fields, api

class Princesa(models.Model):
    _name = 'res.princesa'
    _description = 'Princesa'
    
    name = fields.Char(string='Nombre', required=True)
    descripcion = fields.Text(string='Descripción')
    reserva_id = fields.Many2one('res.booking', string='Reserva', ondelete='cascade')
