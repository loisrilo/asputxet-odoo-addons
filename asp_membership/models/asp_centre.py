# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class AspCentre(models.Model):
    _name = "asp.centre"

    name = fields.Char()
