# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError, UserError

class StockPicking(models.Model):
    _inherit = 'stock.picking'
    
    def button_validate(self):
        for rec in self:
            for line in rec.move_ids_without_package:
                if line.purchase_line_id and line.purchase_line_id.tolerance_receipt_qty > 0:
                    if line.quantity > line.purchase_line_id.tolerance_receipt_qty:
                        raise ValidationError(_('You can not receive more than %s tolerance quantity for product %s') % (line.purchase_line_id.tolerance_receipt_qty, line.product_id.name))
        return super().button_validate() 

    