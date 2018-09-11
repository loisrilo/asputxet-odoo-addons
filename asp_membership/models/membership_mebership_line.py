# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models, _


class MembershipMembershipLine(models.Model):
    _inherit = "membership.membership_line"

    centre_id = fields.Many2one(
        related="partner.centre_id",
        store=True,
        readonly=True,
    )
