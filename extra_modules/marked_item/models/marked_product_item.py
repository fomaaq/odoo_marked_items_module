from odoo import models, fields


class MarkedProductItem(models.Model):
    _name = 'marked_product_item'
    _description = 'Товар (маркированный)'

    name = fields.Char(string='Наименование маркированного товара')
    description = fields.Text(related='product.description')
    product_quantity = fields.Integer(string='Количество товаров', required=True)
    product_name = fields.Char(related='product.name')
    product = fields.Many2one(string='Товар', required=True, comodel_name='product_item')
    last_status = fields.Char(string='Последний назначенный статус', required=True)
    stock = fields.Many2one(string='Последний назначенный cклад', comodel_name='stock.warehouse')
    costs_receipts_ids = fields.One2many(string='Затраты/приходы', comodel_name='marked_item_costs_receipts_item', inverse_name='marked_item')

    def create(self, vals):
        product = vals.get('product', False)
        product_name = self.env['product_item'].browse([product,]).name
        vals['name'] = product_name + '-' + self.env['ir.sequence'].next_by_code('marked_product_item')
        return super().create(vals)
