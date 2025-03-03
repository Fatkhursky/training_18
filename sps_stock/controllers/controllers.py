# -*- coding: utf-8 -*-
# from odoo import http


# class SpsStock(http.Controller):
#     @http.route('/sps_stock/sps_stock', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sps_stock/sps_stock/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sps_stock.listing', {
#             'root': '/sps_stock/sps_stock',
#             'objects': http.request.env['sps_stock.sps_stock'].search([]),
#         })

#     @http.route('/sps_stock/sps_stock/objects/<model("sps_stock.sps_stock"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sps_stock.object', {
#             'object': obj
#         })

