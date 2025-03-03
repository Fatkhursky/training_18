# Copyright 2018-2019 ForgeFlow, S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0).
from datetime import datetime

import pytz

from odoo import _, api, fields, models
from odoo.exceptions import UserError
from odoo.tools import get_lang


class PurchaseRequestLineMakePurchaseOrder(models.TransientModel):
    _inherit = "purchase.request.line.make.purchase.order"

   
    @api.model
    def _prepare_item(self, line):
        res = super(PurchaseRequestLineMakePurchaseOrder, self)._prepare_item(line)
        res['product_qty'] = line.product_qty - line.purchased_qty
        return res
    
    # @api.model
    # def _prepare_purchase_order(self, picking_type, group_id, company, origin):
    #     data = super(PurchaseRequestLineMakePurchaseOrder, self)._prepare_purchase_order(picking_type, group_id, company, origin)
    #     data['origin']  = self.item_ids.mapped('request_id.name')[0]
    #     data['request_id'] = self.item_ids.mapped('request_id')[0].id
    #     return data
    
    @api.model
    def _prepare_purchase_order(self, picking_type, group_id, company, origin):
        data = super()._prepare_purchase_order(picking_type, group_id, company, origin)
        if self.item_ids:
            first_request = self.item_ids[0].request_id
            data.update({
                'origin': first_request.name,
                'request_id': first_request.id
            })
        return data

            

   