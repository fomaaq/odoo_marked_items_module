from odoo import models, fields


class ProductItem(models.Model):
    _name = 'product_item'
    _description = 'Товар (без маркировки)'

    name = fields.Char('Наименование товара', required=True)
    description = fields.Text('Описание товара', required=True)
