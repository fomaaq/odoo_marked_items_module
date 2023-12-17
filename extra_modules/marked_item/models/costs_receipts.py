from odoo import models, fields


class CostsReferencesItem(models.Model):
    _name = 'costs_receipts_item'
    _description = 'Затраты/Приходы'

    name = fields.Char(string='Наименование статьи', required=True)
