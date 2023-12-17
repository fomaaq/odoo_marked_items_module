from odoo import models, fields


class MarkedProductItem(models.Model):
    _name = 'marked_product_item'
    _description = 'Товар (маркированный)'

    name = fields.Char(related='product.name')
    description = fields.Text(related='product.description')
    product_quantity = fields.Integer('Количество товаров', required=True)
    product = fields.Many2one(string='Товар', required=True, comodel_name='product_item')
    last_status = fields.Char('Последний назначенный статус', required=True)
    stock = fields.Many2one(string='Последний назначенный cклад', comodel_name='stock.warehouse')
