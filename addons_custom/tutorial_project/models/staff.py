from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class RestStaff(models.Model):
    _name = 'rest.staff'
    _description = 'This model store data of staff'
    _rec_name = 'name'  # rec_name is used to show records according to specidief field like age,dob,email, etc...
    _order = 'age'  # _order is used to show list or tree according to specified filed , bydefault its shows by id , we canalso specified asc or desc
    _inherit = ['mail.thread', 'mail.activity.mixin']

    # if we want to see any changes in any field then we added this (track_visibilty='always')in specific field
    name = fields.Char(string='Name', size=50, track_visibility="always")
    age = fields.Integer(string='Age')
    dob = fields.Date(string='Date_Of_Birth')
    mobile = fields.Char(string='Mobile_Number')
    email = fields.Char(string="Email")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender")
    country_id = fields.Many2one('res.country',
                                 string="Country")  # when we want to get 1 record from multiple records of other models or objects
    country_ids = fields.Many2many('res.country', string="Countries")
    country_code = fields.Char(string="Country_code",
                               related="country_id.code")  # if we want to get related data of any field of many2one object then...
    staff_line_ids = fields.One2many('rest.staff.lines', 'connecting_field', string="Staff Line")
    sequence = fields.Integer(string="Seq.")
    status = fields.Selection([('active', 'Active'), ('resigned', 'Resigned')], string="status", readonly=True,
                              default='active')
    image = fields.Binary(string="Image")
    hand_salary = fields.Float(string="In Hand Salary")
    epf_efi = fields.Float(string="EPF+ESI")
    ctc_salary = fields.Float(string="CTC", compute="calc_ctc")

    def new_function(self):
        print("Hello!.")

    # this function is used to delete all rows of current record line items.
    def delete_one2many(self):
        for record in self:
            if record.staff_line_ids:
                record.staff_line_ids = [(5, 0, 0)]
                # if we want to return some messages with rainbow effect
                return {
                    'effect': {
                        'fadeout': 'slow',
                        'type': 'rainbow_man',
                        'message': 'record has been deleted',
                    }
                }

    def changestatus(self):
        for record in self:
            if record.status == 'active':
                record.status = 'resigned'
            else:
                record.status = 'active'

    # @api.constrains is used for specified field validation e.g.. @api.constrains('age')
    #     from odoo import api, and underscore(_)
    #     create function and put filed name in constrains on which we want to set validation
    #     _ is used to popup validation error e.g... raise ValidationError(_("Age must be 18+"))

    @api.constrains('age')
    def age_validation(self):
        for record in self:
            if record.age <= 18:
                raise ValidationError(_(f"Age must be 18+ {record.age} is not acceptable"))

    # @api.depends is used to set compute attribute
    # create field with compute attribute(compute="function name")
    # create function and define logic in it
    # put fields in api.depends on which this calculation depends e.g..(@api.depends('hand_salary', 'epf_efi'))
    @api.depends('hand_salary', 'epf_efi')
    def calc_ctc(self):
        ctc = 0
        for record in self:
            if record.hand_salary:
                ctc = ctc + record.hand_salary
            if record.epf_efi:
                ctc = ctc + record.epf_efi
            record.ctc_salary = ctc
            break


class RestStaffLines(models.Model):
    _name = 'rest.staff.lines'
    _description = 'This model store line data of staff'

    name = fields.Char(string="Name", size=50)
    connecting_field = fields.Many2one('rest.staff', string="staff ID")
    product_id = fields.Many2one('product.product', string="Products")
    sequence = fields.Integer(string="Seq.")
