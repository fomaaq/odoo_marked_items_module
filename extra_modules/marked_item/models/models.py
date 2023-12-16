from odoo import models, fields


class product_item(models.Model):
    _name = 'product.item'
    _description = 'Товар (без маркировки)'

    name = fields.Char('Наименование товара', required=True)
    description = fields.Text('Описание товара', required=True)
