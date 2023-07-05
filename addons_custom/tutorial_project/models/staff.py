from odoo import models, fields, api, _
from odoo.exceptions import ValidationError, UserError


# in seq_num filed copy attribute is used to ensure not take repeated value in this field
# some of the fields not generated in database so index=True is used create this field in database mandatory
# create data folder in project --> create sequence.xml file in it and define this path in manifest file 'data/sequence.xml'
#
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
    seq_num = fields.Char(string="Seq no.", readonly=True, copy=False, index=True, default=lambda self: _('New'))

    # this function is used to update any record in selected model's object
    def new_function(self):
        print("Hello!.")
        selected_id = self.env['rest.staff'].browse(11)
        # selected_id.copy() # this method is used to copy selected order
        # selected_id.unlink() # this method is used to delete selected order
        selected_id.write({
            'name': 'check write method',
            'age': 45,
            'gender': 'male',
            'dob': '2000-1-1',
        })

    # search method give all records id  inform of tuple
    # we can also define specific conditions in search method
    # after getting orders applying loop to it and access singal record.field data
    #
    # browse method take singal id or list of id's '
    # for ref method--> copy any view id and find its External id in seeting-- techinical-- views and do this (search_ref = self.env.ref('tutorial_project.rest_staff_view_form'))
    # it give browsable id now we can access any field of this id
    def check_orm(self):

        search_ref = self.env.ref('tutorial_project.rest_staff_view_form')
        search_var = self.env['rest.staff'].search([])
        # search_var = self.env['rest.staff'].search([('gender', '=', 'male'), ('status', '=', 'active')]) # by default and condition is apply
        # search_var = self.env['rest.staff'].search(['|',('gender', '=', 'male'), ('status', '=', 'active')]) # this is or condition is apply
        # search_var = self.env['rest.staff'].search_count([])
        print(search_var)
        print("search_ref------", search_ref, "priority-----", search_ref.priority, "active ------", search_ref.active)
        for rec in search_var:
            print("rec :-----", rec)
            # print(rec.name, rec.country_id.name, rec.country_ids)
            for country in rec.country_ids:
                print(rec.name, rec.country_id.name, country.name)
            # browse_id = self.env['rest.staff'].browse(rec.id)
            # print(browse_id.name,browse_id.country_id.name)

    # this function is used to create record in defined object through code
    def orm_create(self):
        self.env['rest.staff'].create({
            'name': 'check create method',
            'age': 25,
            'gender': 'male',
            'dob': '2000-1-1',
        })

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

    @api.model
    def create(self, values):
        if values.get('seq_num', _('New')) == _('New'):
            values['seq_num'] = self.env['ir.sequence'].next_by_code('res.seq.staff') or _('New')
        res = super(RestStaff, self).create(values)
        # if not values.get('staff_line_ids'):
        #     raise ValidationError(_("line items necessary"))
        if values.get('gender') == 'male':
            res['name'] = 'Mr.' + values['name']
        elif values.get('gender') == 'female':
            res['name'] = 'Mrs.' + values['name']
        else:
            return res
        print("self----", self, "res-----", res, "values-----", values)
        return res

    def write(self, values):
        res = super(RestStaff, self).write(values)
        # if not values.get('staff_line_ids'):
        #     raise ValidationError(_("line items necessary"))
        if values.get('gender') == 'male':
            self.name = 'Mr.' + values['name']
        elif values.get('gender') == 'female':
            self.name = 'Mrs.' + values['name']
        else:
            return res
        print("self----", self, "res-----", res, "values-----", values)
        return res

    def unlink(self):
        for rec in self:
            if rec.status == "active":
                raise UserError(_("Active records can't deleted"))
        res = super(RestStaff, self).unlink()
        return res


class RestStaffLines(models.Model):
    _name = 'rest.staff.lines'
    _description = 'This model store line data of staff'

    name = fields.Char(string="Name", size=50, required=True)
    connecting_field = fields.Many2one('rest.staff', string="staff ID")
    product_id = fields.Many2one('product.product', string="Products")
    sequence = fields.Integer(string="Seq.")
