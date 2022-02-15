#-*- coding: utf-8 -*-

from odoo import models, fields, api

class Genre_Model(models.Model):
	_name = "genre.model"
	_description = "Permite agregar etiquetas de género a los juegos"
	name = fields.Char('Etiqueta', required = True)
	color = fields.Integer('Color')