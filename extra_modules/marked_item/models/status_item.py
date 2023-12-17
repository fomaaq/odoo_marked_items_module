from odoo import models, fields


class StatusItem(models.Model):
    _name = 'status_item'
    _description = 'Статус состояния товара'

    name = fields.Char(string='Наименование состояния', required=True)
