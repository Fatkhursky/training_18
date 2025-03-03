# -*- coding: utf-8 -*-
# from odoo import http


# class SpsAccount(http.Controller):
#     @http.route('/sps_account/sps_account', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sps_account/sps_account/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sps_account.listing', {
#             'root': '/sps_account/sps_account',
#             'objects': http.request.env['sps_account.sps_account'].search([]),
#         })

#     @http.route('/sps_account/sps_account/objects/<model("sps_account.sps_account"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sps_account.object', {
#             'object': obj
#         })

