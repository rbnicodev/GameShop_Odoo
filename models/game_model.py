#-*- coding: utf-8 -*-

from odoo import models, fields, api

class Game_Model(models.Model):
        _name = "game.model"
        _description = "Modelo juego"

        name = fields.Char('Nombre', required = True, help = 'Nombre')
        description = fields.Text('Descripción', required = True, help = 'Descripcion')
        cover = fields.Binary()
        date_availability = fields.Date('Disponibilidad', required = True, help = 'Fechas disponibles')
        #precio de venta
        price = fields.Float('Precio de venta', required = True, help = 'Precio')
        starting_price = fields.Float('Precio de salida', required = False, help = 'Precio original')
        owned = fields.Boolean('En posesión')
        
        genre_ids = fields.Many2many('genre.model' , string="Género")
        platform_ids = fields.Many2many('platform.model', string="Plataforma")
        
        revaluation = fields.Float(compute='_compute_revaluation', string='Revalorización (%)')
        num_genres = fields.Integer(compute='_compute_num_genres', string="Cantidad de Géneros")
        
        @api.onchange("genre_ids")
        def _compute_num_genres(self):
                for record in self:
                        record.num_genres = 0
                        for n in range(len(record.genre_ids)):
                                record.num_genres += 1
        
        @api.onchange("price", "starting_price")               
        def _compute_revaluation(self):
                for record in self:
                        if record.starting_price > 0:
                                record.revaluation = record.price / record.starting_price
                        else:
                                record.revaluation = 0