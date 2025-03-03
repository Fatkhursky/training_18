# -*- coding: utf-8 -*-
# from odoo import http


# class SpsPurchaseRequest(http.Controller):
#     @http.route('/sps_purchase_request/sps_purchase_request', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sps_purchase_request/sps_purchase_request/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sps_purchase_request.listing', {
#             'root': '/sps_purchase_request/sps_purchase_request',
#             'objects': http.request.env['sps_purchase_request.sps_purchase_request'].search([]),
#         })

#     @http.route('/sps_purchase_request/sps_purchase_request/objects/<model("sps_purchase_request.sps_purchase_request"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sps_purchase_request.object', {
#             'object': obj
#         })

