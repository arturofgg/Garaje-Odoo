from odoo import models, fields, api
from dateutil.relativedelta import *
from datetime import date

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
    annos = fields.Integer('Años', compute='get_annos')
    descripcion = fields.Text('Descripcion')

    #relaciones entre tablas
    aparcamiento_id = fields.Many2one(
        'garaje.aparcamiento', string='Aparcamiento')
    mantenimiento_ids = fields.Many2many('garaje.mantenimiento', string='Mantenimientos')

    @api.depends('construido')
    def get_annos(self):
        #TODO: luego
        for coche in self:
            hoy = date.today()
            coche.annos = relativedelta(hoy, coche.construido).years

    #restricciones mismo formato que en la bd
        _sql_constraints=[('name_uniq', 'unique(name)', 'La matrícula ya existe')]

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

    def name_get(self):
        resultados=[]
        for mantenimiento in self:
            descripcion = f'{len(mantenimiento.coche_ids)} coches - {mantenimiento.coste} €'
            resultados.append((mantenimiento.id, descripcion))
        return resultados