# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _
from datetime import timedelta, datetime, date
from odoo.exceptions import UserError

class StockWarehouseOrderpoint(models.Model):
    _inherit = "stock.warehouse.orderpoint"

    def _set_default_route_id(self):
        """ Write the `route_id` field on `self`. This method is intendend to be called on the
        orderpoints generated when openning the replenish report.
        """
        self = self.filtered(lambda o: not o.route_id)
        rules_groups = self.env['stock.rule']._read_group([
            ('route_id.product_selectable', '!=', False),
            ('location_dest_id', 'in', self.location_id.ids),
            ('action', 'in', ['pull_push', 'pull']),
            ('route_id.active', '!=', False)
        ], ['location_dest_id', 'route_id'])
        for location_dest, route in rules_groups:
            orderpoints = self.filtered(lambda o: o.location_id.id == location_dest.id)
            # Custom YP
            if route in orderpoints.product_id.route_ids:
                orderpoints.route_id = route