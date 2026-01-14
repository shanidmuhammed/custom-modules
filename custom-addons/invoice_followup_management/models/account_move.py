from odoo import fields, models, api

class AccountMove(models.Model):
    _inherit = "account.move"

    followup_status = fields.Selection([
        ('not contacted', 'Not contacted'),
        ('called', 'Called'),
        ('email sent', 'Email sent'),
        ('payment promise', 'Payment promise'),
        ('escalated', 'Escalated')
    ], string="Follow-up Status", default='not contacted')

    followup_remark = fields.Text(string="Follow-up Remarks")

    next_followup_date = fields.Date(string="Next Follow-up Date")

    is_overdue = fields.Char(
        string="Overdue",
        compute="_compute_is_overdue",
        store=True
    )

    @api.onchange('next_followup_date')
    def _onchange_next_followup_date(self):
        if self.next_followup_date and self.next_followup_date < fields.Date.today():
            return {
                'warning': {
                    'title': "Invalid Date",
                    'message': "You cannot select a past date for next follow-up.",
                }
            }

    @api.depends('invoice_date_due', 'payment_state', 'state')
    def _compute_is_overdue(self):
        today = fields.Date.today()
        for move in self:
            is_overdue = (
                    move.move_type == 'out_invoice'
                    and move.state == 'posted'
                    and move.payment_state != 'paid'
                    and move.invoice_date_due
                    and move.invoice_date_due < today
            )

            if is_overdue:
                move.is_overdue = 'OVERDUE'
            else:
                move.is_overdue = False




