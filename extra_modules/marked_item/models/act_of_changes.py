from datetime import date
from odoo import models, fields, api
from odoo.exceptions import UserError

# SELECTION_LIST = [
#     ('buy', 'Покупка'),
#     ('movement', 'Внутреннее перемещение'),
#     ('sell', 'Продажа'),
# ]


class ActOfChanges(models.Model):
    _name = 'act_of_changes'
    _description = 'Акт изменения состояния товара'

    name = fields.Char(string='Наименование документа', required=True, default='Акт изменения состояния товара № ')
    date = fields.Date(string='Дата документа', required=True, default=date.today())
    applicable_status = fields.Many2one(string='Применяемый статус', comodel_name='status_item')
    is_status_buy = fields.Boolean(compute='compute_is_buy')
    is_status_sell = fields.Boolean(compute='compute_is_sell')
    stock_from = fields.Many2one(string='Применить для маркированных товаров со склада', comodel_name='stock.warehouse')
    stock_where = fields.Many2one(string='Назначить новый склад', comodel_name='stock.warehouse')
    product = fields.Many2one(string='Товар', required=True, comodel_name='product_item')
    product_quantity = fields.Integer('Количество товаров', required=True)

    @api.depends('applicable_status')
    def compute_is_buy(self):
        status = self.env.ref('marked_item.status_item_action_buy')
        for record in self:
            if record.applicable_status == status:
                record.is_status_buy = True
            else:
                record.is_status_buy = False

    @api.depends('applicable_status')
    def compute_is_sell(self):
        status = self.env.ref('marked_item.status_item_action_sell')
        for record in self:
            if record.applicable_status == status:
                record.is_status_sell = True
            else:
                record.is_status_sell = False

    def action_apply(self):
        if self.applicable_status == self.env.ref('marked_item.status_item_action_buy'):
            self.apply_buy()
    
        if self.applicable_status == self.env.ref('marked_item.status_item_action_movement'):
            self.apply_movement()
            
        if self.applicable_status == self.env.ref('marked_item.status_item_action_sell'):
            self.apply_sell()

    def apply_buy(self):
        marked_item = self.env['marked_product_item'].search([('product', '=', self.product.id), ('stock', '=', self.stock_where.id)])
        if marked_item:
            new_quantity = marked_item.product_quantity + self.product_quantity
            marked_item.write({'product_quantity': new_quantity})
        else:
            marked_item.create({'product': self.product.id, 'product_quantity': self.product_quantity, 'stock': self.stock_where.id})

    def apply_movement(self):
        marked_item_from = self.env['marked_product_item'].search([('product', '=', self.product.id), ('stock', '=', self.stock_from.id), ('product_quantity', '>', self.product_quantity)])
        if marked_item_from:
            marked_item_from.write({'product_quantity': marked_item_from.product_quantity - self.product_quantity})
        else:
            raise UserError('Товар не найден на складе в количестве, указанном в акте')
        
        marked_item_where = self.env['marked_product_item'].search([('product', '=', self.product.id), ('stock', '=', self.stock_where.id)])
        if marked_item_where:
            new_quantity = marked_item_where.product_quantity + self.product_quantity
            marked_item_where.write({'product_quantity': new_quantity})
        else:
            marked_item_where.create({'product': self.product.id, 'product_quantity': self.product_quantity, 'stock': self.stock_where.id})

    def apply_sell(self):
        marked_item = self.env['marked_product_item'].search([('product', '=', self.product.id), ('stock', '=', self.stock_from.id), ('product_quantity', '>', self.product_quantity)])
        if marked_item:
            new_quantity = marked_item.product_quantity - self.product_quantity
            marked_item.write({'product_quantity': new_quantity})
        else:
            raise UserError('Товар не найден на складе в количестве, указанном в акте')
