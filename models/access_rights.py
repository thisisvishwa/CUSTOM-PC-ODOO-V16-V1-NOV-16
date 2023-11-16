```python
from odoo import models, fields, api

class AccessRights(models.Model):
    _name = 'access.rights'
    _description = 'Access Rights for Custom PC Building Module'

    name = fields.Char('Name', required=True)
    model_id = fields.Many2one('ir.model', 'Model', required=True)
    group_id = fields.Many2one('res.groups', 'Group')
    perm_read = fields.Boolean('Read Access')
    perm_write = fields.Boolean('Write Access')
    perm_create = fields.Boolean('Create Access')
    perm_unlink = fields.Boolean('Delete Access')

    @api.model
    def create(self, vals):
        record = super(AccessRights, self).create(vals)
        self.env['ir.model.access'].sudo().create({
            'name': record.name,
            'model_id': record.model_id.id,
            'group_id': record.group_id.id,
            'perm_read': record.perm_read,
            'perm_write': record.perm_write,
            'perm_create': record.perm_create,
            'perm_unlink': record.perm_unlink,
        })
        return record

    def write(self, vals):
        res = super(AccessRights, self).write(vals)
        for record in self:
            access = self.env['ir.model.access'].sudo().search([
                ('model_id', '=', record.model_id.id),
                ('group_id', '=', record.group_id.id),
            ], limit=1)
            if access:
                access.write({
                    'name': record.name,
                    'perm_read': record.perm_read,
                    'perm_write': record.perm_write,
                    'perm_create': record.perm_create,
                    'perm_unlink': record.perm_unlink,
                })
        return res

    def unlink(self):
        for record in self:
            access = self.env['ir.model.access'].sudo().search([
                ('model_id', '=', record.model_id.id),
                ('group_id', '=', record.group_id.id),
            ])
            if access:
                access.unlink()
        return super(AccessRights, self).unlink()
```