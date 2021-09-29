from odoo import api, fields, models, _
import logging
_logger = logging.getLogger(__name__)


class Building(models.Model):
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _name = 'schematic_configurator.building'
    _description = 'Schematic Configurator Building'

    # fields
    name = fields.Char()
    partner_id = fields.Many2one('res.partner', required=True)
    level_ids = fields.One2many('schematic_configurator.level', 'building_id')
