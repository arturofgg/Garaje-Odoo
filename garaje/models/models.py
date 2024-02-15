# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class ./garaje(models.Model):
#     _name = './garaje../garaje'
#     _description = './garaje../garaje'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

from odoo import models, fields, api


class aparcamiento(models.Model):
    _name = 'garaje.aparcamiento'
    _description = 'Permite definir las caracteristicas de un aparcamiento'

    name = fields.Char('Direccion', required=True)
    plazas = fields.Integer(string='Plazas', required=True)

    #relaciones entre tablas
    coche_ids = fields.One2many(
        'garaje.coche', 'aparcamiento_id', string='Coches')


class coche(models.Model):
    _name = 'garaje.coche'
    _description = 'Permite definir las caracteristicas de un coche'
    _order = 'name'

    name = fields.Char(string='Matricula', required=True, size=7)
    modelo = fields.Char(string='Modelo', required=True)
    construido = fields.Date(string='Fecha de construccion')
    consumo = fields.Float('Consumo', (4,1), default=0.0,
                            help='Consumo promendio cada 100 kms')
    averiado = fields.Boolean(string='Averiado', default=False)
    #store=True
    annos = fields.Integer('Años', compute='_get_annos')
    descripcion = fields.Text('Descripcion')

    #relaciones entre tablas
    aparcamiento_id = fields.Many2one(
        'garaje.aparcamiento', string='Aparcamiento')
    mantenimiento_ids = fields.Many2many('garaje.mantenimiento', string='Mantenimientos')

    @api.depends('construido')
    def get_annos(self):
        #TODO: luego
        for coche in self:
            coche.annos = 0


class mantenimiento(models.Model):
    _name = 'garaje.mantenimiento'
    _description = 'Permite definir mantenimientos rutinarios sobre conjuntos de coches'
    _order = 'fecha'

    #name = fields.Char()
    fecha = fields.Date('Fecha', required=True, default = fields.date.today())
    tipo = fields.Selection(string='Tipo', selection=[(
        'l', 'Lavar'),('r', 'Revision'),('m', 'Mecanica'),('p', 'Pintura')], default='l')
    coste = fields.Float('Coste', (8,2), help='Coste total del mantenimiento')

    #relaciones entre tablas
    coche_ids = fields.Many2many('garaje.coche', string='Coches')
    