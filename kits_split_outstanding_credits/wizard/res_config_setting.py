from odoo import fields, models

class res_config_settings(models.TransientModel):
    _inherit = 'res.config.settings'

    allow_outstanding_credit_split = fields.Boolean(string='Enable Outstanding Credit Split',config_parameter='kits_split_outstanding_credits.allow_outstanding_credit_split')
