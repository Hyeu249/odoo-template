# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from ..models import const
from odoo.exceptions import ValidationError


class AddSheet(models.TransientModel):
    _name = "studio.add.sheet.wiz"
    _description = "Add Sheet"

    # core ram
    name = fields.Char("Name", tracking=True)
    description = fields.Char("Description", tracking=True)

    def add_sheet(self):
        self.ensure_one()
        raise ValidationError("Whats up")
