# -*- coding: utf-8 -*-
# from odoo import http


# class SpsPurchaseStock(http.Controller):
#     @http.route('/sps_purchase_stock/sps_purchase_stock', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sps_purchase_stock/sps_purchase_stock/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sps_purchase_stock.listing', {
#             'root': '/sps_purchase_stock/sps_purchase_stock',
#             'objects': http.request.env['sps_purchase_stock.sps_purchase_stock'].search([]),
#         })

#     @http.route('/sps_purchase_stock/sps_purchase_stock/objects/<model("sps_purchase_stock.sps_purchase_stock"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sps_purchase_stock.object', {
#             'object': obj
#         })

