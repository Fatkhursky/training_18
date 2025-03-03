# -*- coding: utf-8 -*-
# from odoo import http


# class SpsSale(http.Controller):
#     @http.route('/sps_sale/sps_sale', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sps_sale/sps_sale/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sps_sale.listing', {
#             'root': '/sps_sale/sps_sale',
#             'objects': http.request.env['sps_sale.sps_sale'].search([]),
#         })

#     @http.route('/sps_sale/sps_sale/objects/<model("sps_sale.sps_sale"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sps_sale.object', {
#             'object': obj
#         })

