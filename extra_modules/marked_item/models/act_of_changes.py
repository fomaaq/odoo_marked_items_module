from datetime import date
from odoo import models, fields, api
from odoo.exceptions import UserError


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
    product = fields.Many2one(string='Товар', comodel_name='product_item')
    marked_product = fields.Many2one(string='Маркированный товар', comodel_name='marked_product_item')
    product_quantity = fields.Integer('Количество товаров')

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
        self.env['marked_product_item'].create({'product': self.product.id, 'product_quantity': self.product_quantity, 'last_status': self.applicable_status.name, 'stock': self.stock_where.id})

    def apply_movement(self):
        marked_item = self.env['marked_product_item'].search([('name', '=', self.marked_product.name), ('stock', '=', self.stock_from.id)])
        if marked_item:
            marked_item.write({'last_status': self.applicable_status.name, 'stock': self.stock_where.id})
        else:
            raise UserError('Указанный маркированный товар не найден на складе, указанном в акте')

    def apply_sell(self):
        marked_item = self.env['marked_product_item'].search([('name', '=', self.marked_product.name), ('stock', '=', self.stock_from.id)])
        if marked_item:
            marked_item.write({'last_status': self.applicable_status.name, 'stock': self.stock_from.id})
        else:
            raise UserError('Указанный маркированный товар не найден на складе, указанном в акте')
