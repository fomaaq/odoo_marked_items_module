from odoo import models, fields


class CostReference(models.Model):
    _name = 'cost_reference'
    _description = 'Затраты/Приходы'

    name = fields.Char('Наименование статьи', required=True)
    description = fields.Float('Сумма, руб.', required=True)
