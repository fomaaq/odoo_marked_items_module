# -*- coding: utf-8 -*-
# from odoo import http


# class MarkedItem(http.Controller):
#     @http.route('/marked_item/marked_item', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/marked_item/marked_item/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('marked_item.listing', {
#             'root': '/marked_item/marked_item',
#             'objects': http.request.env['marked_item.marked_item'].search([]),
#         })

#     @http.route('/marked_item/marked_item/objects/<model("marked_item.marked_item"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('marked_item.object', {
#             'object': obj
#         })

