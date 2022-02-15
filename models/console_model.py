#-*- coding: utf-8 -*-

from odoo import models, fields, api

class Platform_Model(models.Model):
	_name = "platform.model"
	_description = "Permite agregar plataformas disponibles a los juegos"
	name = fields.Char('Etiqueta', required = True)
	date = fields.Date('Lanzamiento', help = 'Fecha de lanzamiento')
	color = fields.Integer('Color')