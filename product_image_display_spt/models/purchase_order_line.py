
# -*- coding: utf-8 -*-

from odoo import fields, models

class purchase_order_line(models.Model):
    _inherit = 'purchase.order.line'
    _description = 'Image in line'

    image = fields.Binary("image", related="product_id.image_128")