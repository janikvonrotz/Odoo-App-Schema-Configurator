from odoo import api, fields, models, _
import logging
_logger = logging.getLogger(__name__)


class Panel(models.Model):
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _name = 'schematic_configurator.panel'
    _description = 'Schematic Configurator Panel'

    # fields
    name = fields.Char(required=True)
    room_id = fields.Many2one('schematic_configurator.room', required=True)
    slots_x = fields.Integer(required=True)
    slots_y = fields.Integer(required=True)
    slot_ids = fields.One2many('schematic_configurator.panel.slot', 'panel_id', string="Slots")

    @api.model
    def create(self, values):
        res = super().create(values)
        
        for x in range(res.slots_x):
            for y in range(res.slots_y):
                _logger.info(res.id)
                self.env['schematic_configurator.panel.slot'].create({
                    'panel_id': res.id,
                    'position_x': x,
                    'position_y': y,
                })

        return res


class PanelSlot(models.Model):
    _name = 'schematic_configurator.panel.slot'
    _description = 'Schematic Configurator Panel Slot'
    _rec_name = 'panel_id'

    # fields
    panel_id = fields.Many2one('schematic_configurator.panel', required=True, ondelete="cascade")
    position_x = fields.Integer(required=True)
    position_y = fields.Integer(required=True)
    module_count = fields.Integer(compute='_compute_module_count')
    module_ids = fields.One2many('schematic_configurator.module', 'slot_id')

    def name_get(self):
        res = []
        for rec in self:
            res.append((rec.id, f'{rec.panel_id.name} ({rec.position_x}, {rec.position_y})'))
        return res

    def _compute_module_count(self):
        for rec in self:
            rec.module_count = len(rec.module_ids)

    def action_show_details(self):
        self.ensure_one()
        view = self.env.ref('schematic_configurator.panel_slot_form')
        return {
            'name': 'Slot',
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'res_model': 'schematic_configurator.panel.slot',
            'views': [(view.id, 'form')],
            'view_id': view.id,
            'target': 'new',
            'res_id': self.id,
            'context': dict(self.env.context),
        }