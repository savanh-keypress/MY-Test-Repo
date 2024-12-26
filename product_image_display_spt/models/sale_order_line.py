
# -*- coding: utf-8 -*-

from odoo import api, fields, models

class sale_order_line(models.Model):
    _inherit = 'sale.order.line'
    _description = 'Image in line'

    image = fields.Binary("image", related="product_id.image_128")