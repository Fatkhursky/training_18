# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class sps_purchase_stock(models.Model):
#     _name = 'sps_purchase_stock.sps_purchase_stock'
#     _description = 'sps_purchase_stock.sps_purchase_stock'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

