# -*- coding: utf-8 -*-
# from odoo import http


# class SpsPurchase(http.Controller):
#     @http.route('/sps_purchase/sps_purchase', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sps_purchase/sps_purchase/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sps_purchase.listing', {
#             'root': '/sps_purchase/sps_purchase',
#             'objects': http.request.env['sps_purchase.sps_purchase'].search([]),
#         })

#     @http.route('/sps_purchase/sps_purchase/objects/<model("sps_purchase.sps_purchase"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sps_purchase.object', {
#             'object': obj
#         })

