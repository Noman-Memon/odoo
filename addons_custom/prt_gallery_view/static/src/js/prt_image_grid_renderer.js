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

odoo.define('prt_gallery_view.ImageGridRenderer', function (require) {
"use strict";

var BasicRenderer = require('web.BasicRenderer');

var ImageGridRenderer = BasicRenderer.extend({
  className: 'o_image_grid_view',
  events: {
      'click .oe_image_grid_image': '_onGridItemImage',
      'click .oe_image_grid_caption': '_onGridItemCaption',
  },

  // Override _renderView
  _renderView: function () {
      var self = this;

      this.$el
          .removeClass('o_image_grid_view')
          .empty();

      var $flex_container = $('<div class="o_image_grid_container">');
      this.$el
          .addClass('o_image_grid_view')
          .append($flex_container);
      $flex_container.append(this._renderBody());
      return this._super();
  },

// Render ImageGrid Body
  _renderBody: function () {
    return _.map(this.state.data, this._renderImageGridItem.bind(this));
    },

// Render ImageGrid Item
  _renderImageGridItem: function (record) {
      var self = this;
      var $result = $('<div class="o_image_grid_item"/>');
      // TODO fallback to default size in case nothing in attrs
      var config_height = this.arch.attrs.item_height ? this.arch.attrs.item_height : 150;
      var config_width = this.arch.attrs.item_width ? this.arch.attrs.item_width : 150;

      $result.css("height", config_height);
      $result.css("width", config_width);
      $result.css("max-height", (config_height * 1.50));
      $result.css("max-width", (config_width * 1.50));

      $result.append(_.map(this.arch.children, function (node, index) {
          return self._renderNode(node, record, {mode: 'readonly'})}));

      return $result;
    },

// Render ImageGrid Element
  _renderNode: function (node, record, options) {
    var renderer = this['_renderTag' + _.str.capitalize(node.tag)];
    if (renderer) {
        return renderer.call(this, node, record, options);
    }
    if (_.isString(node)) {
        return node;
    }
    return "oops...)";
  },

  // Render Field
  _renderTagField: function (node, record, options) {
    return this._renderFieldWidget(node, record, {mode: 'readonly'}).$el;
  },

  // Render Image Tag -- div version
  _renderTagImage: function (node, record, options) {
    var self = this;
    var $image_div = $('<div class="oe_image_grid_image"/>');
    // Append all children
    $image_div.append(_.map(node.children, function (node, index) {
        return self._renderNode(node, record, options)}));

    // Store res_id
    $image_div[0].res_id = record.data['id'];

    return $image_div;
  },

  // Render Caption Tag -- div version
  _renderTagCaption: function (node, record, options) {
    var self = this;
    var $caption_div = $('<div class="oe_image_grid_caption"/>');
    // Append all children
    $caption_div.append(_.map(node.children, function (node, index) {
        return self._renderNode(node, record, options)}));

  // Store res_id
    $caption_div[0].res_id = record.data['id'];
    return $caption_div;
  },

// Click caption
  _onGridItemCaption: function (event) {
      if (!$(event.target).prop('special_click')) {
          var id = event.currentTarget.res_id;
          this.trigger_up('switch_view', {
              view_type: 'form',
              res_id: id,
              mode: $(event.currentTarget).data.mode || 'readonly', //fix
              model: this.state.model,
          });
      }
  },

  // Click image
    _onGridItemImage: function (event) {
        if (!$(event.target).prop('special_click')) {
            var id = event.currentTarget.res_id;
            this.trigger_up('switch_view', {
                view_type: 'gallery',
                res_id: id,
                mode: $(event.currentTarget).data.mode || 'readonly', //fix
                model: this.state.model,
            });
        }
    },

// End)
  });

return ImageGridRenderer;

});
