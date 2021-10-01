from odoo import api, fields, models, _
import logging
_logger = logging.getLogger(__name__)


class Level(models.Model):
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _name = 'schematic_configurator.level'
    _description = 'Schematic Configurator Level'
    _order = 'sequence'

    # fields
    name = fields.Char()
    sequence = fields.Integer()
    building_id = fields.Many2one('schematic_configurator.building', required=True)
    room_ids = fields.One2many('schematic_configurator.room', 'level_id', string="Rooms")

    def action_show_details(self):
        self.ensure_one()
        view = self.env.ref('schematic_configurator.level_form')
        return {
            'name': _('%s') % self.name,
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'res_model': 'schematic_configurator.level',
            'views': [(view.id, 'form')],
            'view_id': view.id,
            'target': 'new',
            'res_id': self.id,
            'context': dict(self.env.context),
        }