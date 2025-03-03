# -*- coding: utf-8 -*-
# from odoo import http


# class SpsReport(http.Controller):
#     @http.route('/sps_report/sps_report', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sps_report/sps_report/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sps_report.listing', {
#             'root': '/sps_report/sps_report',
#             'objects': http.request.env['sps_report.sps_report'].search([]),
#         })

#     @http.route('/sps_report/sps_report/objects/<model("sps_report.sps_report"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sps_report.object', {
#             'object': obj
#         })

