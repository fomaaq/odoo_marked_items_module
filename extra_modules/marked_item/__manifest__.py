# -*- coding: utf-8 -*-
{
    'name': "Маркировка товара",

    'summary': "Маркирование и отслеживание товаров",

    'description': """
Информационная система "Маркировка товара" предназначена для того, чтобы оперативно получить информацию о месте нахождения товара и его себестоимости в любой момент времени.
    """,

    'author': "Viktor",
    'website': "https://github.com/fomaaq/odoo_marked_items_module",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'stock',
        ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/marked_item_view.xml',
        'views/marked_item_menus.xml',
        # 'views/views.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
}
