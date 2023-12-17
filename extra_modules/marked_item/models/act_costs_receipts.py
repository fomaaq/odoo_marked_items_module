from odoo import models, fields


class ActCostsReferencesItem(models.Model):
    _name = 'act_costs_receipts_item'
    _description = 'Затраты/Приходы'

    cost_receipt = fields.Many2one(string='Наименование статьи', required=True, comodel_name='costs_receipts_item')
    price = fields.Float(string='Значение, руб.', required=True)
    act_of_changes = fields.Many2one(comodel_name='act_of_changes')
