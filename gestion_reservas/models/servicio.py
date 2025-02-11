from odoo import models, fields

class Servicio(models.Model):
    _name = 'res.service'
    _description = 'Servicio de la mazmorra'
    
    name = fields.Char(string='Nombre',required=True)
    descripcion = fields.Text(string='Descripción')
    precio = fields.Float(string='Precio',required=True)
    duracion = fields.Integer(string='Duracion (en minutos)',required=True)
    disponible = fields.Boolean(string='Disponibilidad',default=True)
    reserva_ids = fields.Many2many('res.reserva', string='Reservas')
