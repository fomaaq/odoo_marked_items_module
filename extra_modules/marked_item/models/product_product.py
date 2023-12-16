from odoo import models, fields


class Product(models.Model):
    _inherit = 'product.product'

    description = fields.Char(string='Описание')
