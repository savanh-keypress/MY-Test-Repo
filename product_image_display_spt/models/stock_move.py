
# -*- coding: utf-8 -*-

from odoo import api, fields, models

class stock_move(models.Model):
    _inherit = 'stock.move'
    _description = 'Image in line'

    image = fields.Binary("image", related="product_id.image_128")