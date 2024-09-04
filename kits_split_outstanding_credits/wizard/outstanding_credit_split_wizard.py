from odoo import api, fields, models
from odoo.exceptions import ValidationError
 
class outstanding_credit_split_wizard(models.TransientModel):
    _name = "outstanding.credit.split.wizard"

    account_move_id = fields.Many2one('account.move',"Account Move")
    outstanding_move_line_id = fields.Many2one('account.move.line',"Account Move Line")
    amount_due = fields.Float(compute='compute_credit_amount',string = "Amount Due")
    available_credit_amount = fields.Float(compute='compute_credit_amount',string = "Available Credit Amount")
    paying_amount = fields.Float("Amount Paying")

    @api.depends('outstanding_move_line_id')
    def compute_credit_amount(self):
        if self.outstanding_move_line_id.amount_residual<0:
            self.available_credit_amount = self.outstanding_move_line_id.amount_residual*-1
            self.amount_due = self.account_move_id.amount_residual
            
        if self.outstanding_move_line_id.amount_residual>0:
            self.available_credit_amount = self.outstanding_move_line_id.amount_residual
            self.amount_due = self.account_move_id.amount_residual

    def kits_create_payment(self):
        context=self._context.copy()
        context['paying_amount'] = self.paying_amount
        self.account_move_id.with_context(context).js_assign_outstanding_line(self.outstanding_move_line_id.id)

        return {
        'type': 'ir.actions.client',
        'tag': 'reload',
        }

    @api.onchange('paying_amount')
    def kits_paying_amount_onchange(self):
        if self.paying_amount>0:
            if self.paying_amount>self.available_credit_amount:
                raise ValidationError("You cannot exceed the available credit amount with your payment.")

            if self.paying_amount>self.amount_due:
                raise ValidationError("You cannot exceed the amount due with your payment.")
