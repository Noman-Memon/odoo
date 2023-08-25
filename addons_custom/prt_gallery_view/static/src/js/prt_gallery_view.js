/**********************************************************************************
* 
*    Copyright (C) Cetmix OÜ
*
*   Odoo Proprietary License v1.0
* 
*   This software and associated files (the "Software") may only be used (executed,
*   modified, executed after modifications) if you have purchased a valid license
*   from the authors, typically via Odoo Apps, or if you have received a written
*   agreement from the authors of the Software (see the COPYRIGHT file).
* 
*   You may develop Odoo modules that use the Software as a library (typically
*   by depending on it, importing it and using its resources), but without copying
*   any source code or material from the Software. You may distribute those
*   modules under the license of your choice, provided that this license is
*   compatible with the terms of the Odoo Proprietary License (For example:
*   LGPL, MIT, or proprietary licenses similar to this one).
* 
*   It is forbidden to publish, distribute, sublicense, or sell copies of the Software
*   or modified copies of the Software.
* 
*   The above copyright notice and this permission notice must be included in all
*   copies or substantial portions of the Software.
* 
*   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
*   IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
*   FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
*   IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
*   DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
*   ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
*   DEALINGS IN THE SOFTWARE.
*
**********************************************************************************/

odoo.define('prt_gallery_view.GalleryView', function (require) {
"use strict";

var BasicController = require('web.BasicController');
var BasicModel = require('web.BasicModel');
var BasicView = require('web.BasicView');

var GalleryController = BasicController.extend({

    _update: function () {
        var title = this.model.getName(this.handle);
        this.set('title', title);
        return this._super.apply(this, arguments);
    }
  });

var GalleryModel = BasicModel.extend({});
var GalleryRenderer = require('prt_gallery_view.GalleryRenderer');
var core = require('web.core');

var _lt = core._lt;

var GalleryView = BasicView.extend({
  config: {
        Model: GalleryModel,
        Controller: GalleryController,
        Renderer: GalleryRenderer,
    },
    display_name: _lt('Gallery'),
    icon: 'fa-image',
    multi_record: false,
    searchable: false,
    viewType: 'gallery',

    init: function (viewInfo, params) {
        this._super.apply(this, arguments);
        this.loadParams.type = 'record';
        params.mode = 'readonly';
        this.controllerParams.hasSidebar = params.sidebar;
      },
  });

return GalleryView;

});

odoo.define('registerGallery', function (require) {
"use strict";

var GalleryView = require('prt_gallery_view.GalleryView');
var view_registry = require('web.view_registry');

view_registry.add('gallery', GalleryView);

});
