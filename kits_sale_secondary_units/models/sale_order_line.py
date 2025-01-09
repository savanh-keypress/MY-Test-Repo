# -*- coding: utf-8 -*-
# Part of Keypress IT Services. See LICENSE file for full copyright and licensing details.##
###############################################################################
from odoo import fields,api,models

class sale_order_line(models.Model):
    _inherit = 'sale.order.line'

    secondary_uom_id = fields.Many2one('uom.uom','Secondary UOM', domain="[('category_id', '=', product_uom_category_id)]")
    secondary_qty = fields.Float('Secondary Qty')

    @api.onchange('product_id')
    def product_id_change(self):
        for record in self:
            if record.product_id.secondary_uom_id.id:
                record.secondary_uom_id = record.product_id.secondary_uom_id.id
                record.secondary_qty =  round(record.product_uom._compute_quantity(record.product_uom_qty,record.product_id.secondary_uom_id) ,2)
    
    @api.onchange('product_uom', 'product_uom_qty')
    def kits_product_uom_change(self):
        for record in self:
            if record.product_id.secondary_uom_id.id and not self._context.get('secondary_uom',False):
                record.secondary_uom_id = record.product_id.secondary_uom_id.id
                record.secondary_qty =  round(record.product_uom._compute_quantity(record.product_uom_qty,record.product_id.secondary_uom_id) ,2)
        ctx = self._context.copy()
        ctx['secondary_uom'] = True
        self.env.context = ctx

    @api.onchange('secondary_uom_id', 'secondary_qty')
    def kits_product_secondary_uom_change(self):
        for record in self:
            if record.product_uom.id and record.secondary_uom_id and not self._context.get('secondary_uom',False):
                record.product_uom_qty = record.secondary_uom_id._compute_quantity(record.secondary_qty,record.product_uom) 
        ctx = self._context.copy()
        ctx['secondary_uom'] = True
        self.env.context = ctx
