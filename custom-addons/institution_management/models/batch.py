from odoo import models, fields

class Batch(models.Model):
    _name = 'institution.batch'

    course_id=fields.Many2one(
        'institution.course',
        string='Course',
        required=True
    )
    name = fields.Char(string="Batch Name", required=True)
    code = fields.Char(string="Batch Code", required=True)
