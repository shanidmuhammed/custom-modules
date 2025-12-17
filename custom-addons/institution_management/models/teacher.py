from odoo import models, fields

class Teacher(models.Model):
    _name = "institution.teacher"

    name = fields.Char(string="Name", required=True)
    subject = fields.Char(string="Subject Specialization")
    phone = fields.Char(string="Phone")