from odoo import models, fields


# create wizard folder in project
# create __init__.py file
# create wizard.py file or any other name as we want
# to create its view
# define path in manifest.py
# Note : Do all things same as creation of models and its fields, views, actions_ids everything only two fields extra create in
# wizard action_id that is
# <field name="target">new</field>
#         <field name="view_id" ref="tutorial_project.rest_staff_wizard_view_form"/>

# after this create action button where ever we want and define this wizard's xml file action_id with project name '

# by-default its create two buttons save and discard
# we can also create our own buttons for calling any function e.g.
# <button name="update_function" string="Update Info" type="object"
#                                 class="oe_highlight"/>
# <button string="Cancel" special="cancel"--------(special attribute is used in wizard for cancel button defining function not required)
#                                 class="btn_secondary"/>


class RestStaffWizard(models.TransientModel):
    _name = 'rest.staff.wizard'
    _description = 'This wizard will update information of staff'

    name = fields.Char(string='Name', size=50)
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
    staff_line_ids = fields.One2many('rest.staff.wizard.lines', 'connecting_field', string="Staff Line")
    image = fields.Binary(string="Image")
    hand_salary = fields.Float(string="In Hand Salary")
    epf_efi = fields.Float(string="EPF+ESI")
    ctc_salary = fields.Float(string="CTC")

    # how to update record through wizard

    def update_function(self):
        # 1st get id of current form record through context (active_id = self._context.get('active_id'))
        active_id = self._context.get('active_id')
        print("active_id---", active_id)
        # 2nd make this id browsable (upd_var = self.env['rest.staff'].browse(active_id))
        # now we get wizard fields data through self and update record fields through browsable_id that is upd_var.write method
        upd_var = self.env['rest.staff'].browse(active_id)
        print(upd_var)
        # for update many2many fields data
        country_list = []  # in this list we get country ids
        for vals in self.country_ids:
            country_list.append(vals.id)
        # for update one2many fields data
        list2 = []
        for val2 in self.staff_line_ids:
            list2.append((0, 0, {
                'name': val2.name,
                'product_id': val2.product_id.id,
            }))

        # if we want to first empty one2many fields data and then update new data then do this
        upd_var.staff_line_ids = [(5, 0, 0)]
        # 3rd create dictionary and update fields data
        vals = {
            'name': self.name,
            'age': self.age,
            'gender': self.gender,
            'dob': self.dob,
            'mobile': self.mobile,
            'email': self.email,
            'country_id': self.country_id.id,  # for update many2one field
            'country_ids': [(6, 0, country_list)],
            'staff_line_ids': list2,

        }
        upd_var.write(vals)
        # if we want to not close wizard automatically then just return this
        return {
            'type': 'ir.actions.do.nothing'
        }


class RestStaffWizardLines(models.TransientModel):
    _name = 'rest.staff.wizard.lines'
    _description = 'This model store line data of staff'

    name = fields.Char(string="Name", size=50, required=True)
    connecting_field = fields.Many2one('rest.staff.wizard', string="staff ID")
    product_id = fields.Many2one('product.product', string="Products")
    sequence = fields.Integer(string="Seq.")
