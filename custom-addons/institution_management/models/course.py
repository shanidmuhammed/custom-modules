from odoo import models, fields
from odoo.odoo.orm.fields_relational import One2many
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

    batch_ids = fields.One2many(
        'institution.batch',
        'course_id',
        string="Batches"
    )

    student_ids = fields.One2many('institution.student', 'course_id', string='Students')

    def action_view_students(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Enrolled Students',
            'res_model': 'institution.student',
            'domain': [('course_id', '=', self.id)],
            'view_mode': 'tree,form',
        }