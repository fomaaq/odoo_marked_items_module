from datetime import date
from odoo import models, fields


class ActOfChanges(models.Model):
    _name = 'act_of_changes'
    _description = 'Акт изменения состояния товара'

    name = fields.Char(string='Наименование документа', required=True, default='Акт изменения состояния товара № ')
    date = fields.Date(string='Дата документа', required=True, default=date.today())
    applicable_status = fields.Selection(string='Применяемый статус', required=True, selection=
                                         [
                                             ('buy', 'Покупка'),
                                             ('movement', 'Внутреннее перемещение'),
                                             ('sell', 'Продажа'),
                                         ])
    stock_from = fields.Many2one(string='Применить для маркированных товаров со склада', comodel_name='stock.warehouse')
    stock_where = fields.Many2one(string='Назначить новый склад', required=True, comodel_name='stock.warehouse')
    product = fields.Many2one(string='Товар', required=True, comodel_name='product_item')
    product_quantity = fields.Integer('Количество товаров', required=True)

    def action_apply(self):
        marked_item = self.env['marked_product_item'].search(['&', ('product_quantity', '=', self.product.id), ('stock', '=', self.warehouse.id)])
        if marked_item:
            marked_item.write({'product_quantity': marked_item.product_quantity + self.product_quantity})
        else:
            marked_item.create({'product': self.product.id, 'product_quantity': self.product_quantity, 'stock': self.warehouse.id})

# TODO
# Если назначаемый статус Покупка, то поле Склад откуда (Применить для товаров со склада) может быть необязательным или скрытым
