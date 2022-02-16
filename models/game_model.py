#-*- coding: utf-8 -*-

from odoo import models, fields, api

class Game_Model(models.Model):
        _name = "game.model"
        _description = "Modelo juego"

        name = fields.Char('Nombre', required = True, help = 'Nombre')
        description = fields.Text('Descripción', required = True, help = 'Descripcion')
        cover = fields.Binary()
        date_availability = fields.Date('Disponibilidad', required = True, help = 'Fechas disponibles')
        price = fields.Float('Precio de venta', required = True, help = 'Precio')
        genre_ids = fields.Many2many('genre.model' , string="Género")
        platform_ids = fields.Many2many('platform.model', string="Plataforma")
        available_platforms = fields.Integer(compute='_compute_available_platforms', string="Plataformas disponibles")
        
        def _compute_available_platforms(self):
                self.available_platforms = 0
                for platform in self.platform_ids:
                        self.available_platforms += 1