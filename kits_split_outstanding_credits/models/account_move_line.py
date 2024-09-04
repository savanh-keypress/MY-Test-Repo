from odoo import models
from odoo.exceptions import ValidationError

class account_move_line(models.Model):
    _inherit = 'account.move.line'

    def _create_reconciliation_partials(self):

        res = super(account_move_line,self)._create_reconciliation_partials()

        paying_amount = self._context.get('paying_amount')

        if paying_amount!=None:
            amount_pay = paying_amount
            if amount_pay <= 0:
                raise ValidationError("The amount must be positive.")

            res.amount = amount_pay
            res.credit_amount_currency = amount_pay
            res.debit_amount_currency = amount_pay

        return res
