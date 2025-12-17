from odoo import models, fields
from odoo.odoo.tools.sql import set_not_null


class Course(models.Model):
    _name = 'institution.course'

    name = fields.Char(string="Course Title", required=True)
    fee=fields.Char(string="Fee of Course", required=True)
    code = fields.Char(string="Course Code", required=True)
    description = fields.Text(string="Course Description", required=True)
    duration = fields.Integer(string="Course Duration", required=True)

    teacher_id = fields.Many2one(
        'institution.teacher',
        string="Assigned Teacher",
        ondelete='set null',
    )

    category_ids = fields.Many2many(
        'institution.category',
        string="Categories"
    )