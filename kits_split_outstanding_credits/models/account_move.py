from odoo import models,fields,api

class account_move(models.Model):
    _inherit = 'account.move'

    def open_prepayment_wizard_action(self,outstanding_credit_id):
        allow_split = self.env['ir.config_parameter'].sudo().get_param('kits_split_outstanding_credits.allow_outstanding_credit_split')

        if allow_split:
            self.ensure_one()
            return {
                'name': 'Outstanding Credit Payment',
                'type': 'ir.actions.act_window',
                'view_mode': 'form',
                'views': [(False, 'form')],
                'res_model': 'outstanding.credit.split.wizard',
                'target':'new',
                'context': {
                    "default_account_move_id":self.id,
                    "default_outstanding_move_line_id":outstanding_credit_id
                },
            }
        else:
            return False