# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
import re
from odoo.exceptions import UserError, ValidationError

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    def button_validate(self):
        for rec in self:
            if rec.sale_id and not rec.sale_id.allow_delivery:
                raise ValidationError(_('Yout process is not allowed, please check sales order DP'))
        return super().button_validate()


   

