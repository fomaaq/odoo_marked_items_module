from odoo import models, fields


class MarkedItemCostsReferencesItem(models.Model):
    _name = 'marked_item_costs_receipts_item'
    _description = 'Затраты/Приходы'

    cost_receipt = fields.Many2one(string='Наименование статьи', required=True, comodel_name='costs_receipts_item')
    price = fields.Float(string='Значение, руб.', required=True)
    marked_item = fields.Many2one(comodel_name='marked_product_item')
