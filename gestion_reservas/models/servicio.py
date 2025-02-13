from odoo import models, fields
from odoo.exceptions import ValidationError

class Servicio(models.Model):
    _name = 'res.service'
    _description = 'Servicio de la mazmorra'
    
    name = fields.Char(string='Nombre',required=True)
    descripcion = fields.Text(string='Descripción')
    precio = fields.Float(string='Precio',required=True)
    duracion = fields.Integer(string='Duracion (en minutos)',required=True)
    disponible = fields.Boolean(string='Disponibilidad',default=True)
    reserva_ids = fields.Many2many('res.reserva', string='Reservas')

    @api.constrains('precio')
    def _check_precio(self):
        for record in self:
            if record.price<=0:
                raise ValidationError("El precio debe ser positivo y mayor que 0")
    @api.constrains('duracion')
    def _check_duracion(self):
        for record in self:
            if(record.duracion<=0):
                raise ValidationError("La duración debe ser mayor a 0 minutos")
    
    @api.constrains
    def _check_nombre_unico(self):
        for record in self:
            servicioExistente = self.search([('name','=',record.name),('id','!=',record.id)])
            if servicioExistente:
                raise ValidationError("El nombre del servicio debe ser único.")