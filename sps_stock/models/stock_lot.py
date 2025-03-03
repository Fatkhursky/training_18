# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import _, api, fields, models
from odoo.exceptions import UserError, ValidationError
from odoo.osv import expression


class StockLot(models.Model):
    _inherit = 'stock.lot'
    
    panjang = fields.Float("Panjang(M)")
    density = fields.Float("Density")
    ketebalan = fields.Float("Ketebalan (Micron)")


    # def create(self, vals_list):
    #     res = super().create(vals_list)
        
    #     return res