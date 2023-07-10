from odoo import models, fields, api, _


class RestDepartment(models.Model):
    _name = 'rest.department'
    _description = " This model will store data of department"
    _rec_name = 'name'

    name = fields.Char(string="Name")
    seq_num = fields.Char(string='Seq No.', readonly=True, copy=False, index=True, default=lambda self: _('New'))
    sequence = fields.Integer(string='Seq.')

    # def create(self, vals):
    #     if vals.get('seq_num', _('New')) == _('New'):
    #         vals['seq_num'] = self.env['ir.sequence'].next_by_code('rest.seq.department') or _('New')
    #     res = super(RestDepartment, self).create(vals)
    #     return res

    # when we select any record from many2one by-default name_get function work on _rec_name field and its shows record name but ,
    # if we want to get different name or any specified word or syntex then we overwrite this function like this
    def name_get(self):
        result = []
        for rec in self:
            name = f'[ + {rec.name}+ ]'
            result.append((rec.id, name))  # append in result list must be in form of tuple record id and name field
        return result

    # there are three methods tto get default values in any record 1. pass condition in context attribute, 2. pass value in default attribute,
    # 3. use default_get function by this we can get default value on form view


