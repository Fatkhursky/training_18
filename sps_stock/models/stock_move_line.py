# -*- coding: utf-8 -*-

from odoo import models, fields, api
from collections import defaultdict

class StockMoveLine(models.Model):
    _inherit = 'stock.move.line'

    panjang = fields.Float("Panjang(M)")
    density = fields.Float("Density")
    ketebalan = fields.Float("Ketebalan (Micron)")


    def _prepare_new_lot_vals(self):
        return {**super()._prepare_new_lot_vals(), 'panjang': self.panjang, 'density': self.density, 'ketebalan': self.ketebalan}
        
