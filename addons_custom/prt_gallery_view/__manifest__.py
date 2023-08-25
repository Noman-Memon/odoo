###################################################################################
# 
#    Copyright (C) Cetmix OÜ
#
#   Odoo Proprietary License v1.0
# 
#   This software and associated files (the "Software") may only be used (executed,
#   modified, executed after modifications) if you have purchased a valid license
#   from the authors, typically via Odoo Apps, or if you have received a written
#   agreement from the authors of the Software (see the COPYRIGHT file).
# 
#   You may develop Odoo modules that use the Software as a library (typically
#   by depending on it, importing it and using its resources), but without copying
#   any source code or material from the Software. You may distribute those
#   modules under the license of your choice, provided that this license is
#   compatible with the terms of the Odoo Proprietary License (For example:
#   LGPL, MIT, or proprietary licenses similar to this one).
# 
#   It is forbidden to publish, distribute, sublicense, or sell copies of the Software
#   or modified copies of the Software.
# 
#   The above copyright notice and this permission notice must be included in all
#   copies or substantial portions of the Software.
# 
#   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#   IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#   FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
#   IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
#   DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
#   ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#   DEALINGS IN THE SOFTWARE.
#
###################################################################################

# -*- coding: utf-8 -*-
{
    'name': 'Image Grid View and Gallery View. Display images as grid, preview images, open images full screen,'
            ' swipe images on mobile or tablet',
    'version': '1.2',
    'summary': """Image Grid and Gallery Views""",
    'author': 'Ivan Sokolov, Cetmix',
    'license': 'OPL-1',
    'price': 750.00,
    'currency': 'EUR',
    'category': 'Productivity',
    'support': 'odooapps@cetmix.com',
    'website': 'https://cetmix.com',
    'live_test_url': 'https://demo.cetmix.com',
    'description': """
Gallery View
""",
    'depends': ['base', 'product', 'web'],
    'data': [
        'security/groups.xml',
        'data/prt_gallery_template.xml',
        'views/prt_gallery_template.xml',
        'views/prt_gallery_sample.xml',
    ],

    'images': ['static/description/banner_gallery.png'],

    'qweb': [
        'static/src/xml/prt_gallery_qweb.xml',
        'static/src/xml/prt_gallery_image_widget.xml',
    ],
    'assets': {
        'web.assets_backend': [
            '/prt_gallery_view/static/src/css/gallery_view.css',
            '/prt_gallery_view/static/src/js/prt_gallery_renderer.js',
            '/prt_gallery_view/static/src/js/prt_gallery_view.js',
            '/prt_gallery_view/static/src/js/prt_gallery_widgets.js',
            '/prt_gallery_view/static/src/js/prt_gallery_grid_renderer.js',
            '/prt_gallery_view/static/src/js/prt_gallery_grid_view.js',
        ],
    },

    'installable': True,
    'application': True,
    'auto_install': False
}
