from odoo import models, fields

class Category(models.Model):
    _name = 'institution.category'

    name = fields.Char(string="Name", required=True)
