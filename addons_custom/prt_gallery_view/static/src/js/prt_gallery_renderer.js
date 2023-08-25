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

odoo.define('prt_gallery_view.GalleryRenderer', function (require) {
"use strict";

var BasicRenderer = require('web.BasicRenderer');

var GalleryRenderer = BasicRenderer.extend({
  className: "o_gallery_view",


// Override autofocus
//  autofocus: function(){},

// Override _renderView
  _renderView: function () {
    // render the gallery and evaluate the modifiers
    var self = this;
    var defs = [];
    this.defs = defs;
    var $gallery = this._renderGallery(this.arch).addClass(this.className);
    delete this.defs;
    return $.when.apply($, defs).then(function () {
            self._updateView($gallery.contents());
        }, function () {
            $gallery.remove();
        });
      },

// Update View
    _updateView: function ($newContent) {
        var self = this;
        // Set the new content of the form view, and toggle classnames
        this.$el.html($newContent);
      },

// Render Gallery
    _renderGallery: function (node) {
      var $result = $('<div/>');
      if (node.attrs.class) {
          $result.addClass(node.attrs.class);
      }
      $result.append(_.map(node.children, this._renderNode.bind(this)));
      return $result;
    },

// Render Node
_renderNode: function (node) {
    var renderer = this['_renderTag' + _.str.capitalize(node.tag)];
    if (renderer) {
        return renderer.call(this, node);
    }
    if (_.isString(node)) {
        return node;
    }
    return "oops...)";
  },

  // Render Field
  _renderTagField: function (node) {
    return this._renderFieldWidget(node, this.state).$el;
  },


  // Render Image Tag
  _renderTagImage: function (node) {
    var $image_div = $('<div class="oe_gallery_image_container"/>');

    // Append all children
    $image_div.append(_.map(node.children, this._renderNode.bind(this)));

    // Buttons
    var $image_side_back = $('<div class="oe_gallery_button_prev"/>');
    var $image_side_next = $('<div class="oe_gallery_button_next"/>');

    // Table to hold image
    var $image_td = $('<td/>').append($image_div).append($image_side_back).append($image_side_next);
    var $image_tr = $('<tr/>').append($image_td)

    var $result = $('<table class="oe_image_table"/>').append($image_tr);

//    Swipe

      $result[0].addEventListener("touchstart",function(event){
       if(event.touches.length === 1){
          //just one finger touched
          swipe_start = event.touches.item(0).clientX;
        }else{
        swipe_start = null;
        }
      });

      $result[0].addEventListener("touchend",function(event){
          event.stopPropagation();
          var offset = 80;//minimum offset considered as swipe are a swipe
          if(swipe_start){
            //just one finger touched
            var end = event.changedTouches.item(0).clientX;

            if(end > swipe_start + offset){
             //a left -> right swipe
            $(".o_pager_previous").click();
            }
            if(end < swipe_start - offset ){
             //a right -> left swipe
             $(".o_pager_next").click();
            }
          // Reset swipe start
          swipe_start = null;
          }
        });

    // Click pager <-
    $image_side_back.click(function(event) {
      event.stopPropagation();
      $(".o_pager_previous").click();
    });
    // ->
    $image_side_next.click(function(event) {
      event.stopPropagation();
      $(".o_pager_next").click();
    });

    // Click image
    $image_div.click(function () {
      var modal = $("#myModal");
      modal.css("display", "block");
    });

    return $result;
  },

  // Render Caption Tag
  _renderTagCaption: function (node) {
    var $caption_div = $('<div class="oe_gallery_caption"/>');
    $caption_div.append(_.map(node.children, this._renderNode.bind(this)));
    var $result = $('<table class="oe_caption_container"/>').append($caption_div);
    return $result;
  },

// Init
  init: function (parent, state, params) {
      this._super.apply(this, arguments);

// Add modal container

      // Content
      var $modal_content = $('<img class="gallery-modal-content"/>');
      var $image_div = $('<div class="oe_gallery_image_container" style="cursor:zoom-out; height: 99%;"/>');

      // Buttons
      var $image_side_back = $('<div class="oe_gallery_button_prev"/>');
      var $image_side_next = $('<div class="oe_gallery_button_next"/>');

      // Assemble
      $image_div.append($modal_content)
          .append($image_side_back)
          .append($image_side_next);
      var $result = $('<div class="gallery-modal" id="myModal"/>').append($image_div)


//    Swipe

      $image_div[0].addEventListener("touchstart",function(event){
       if(event.touches.length === 1){
          //just one finger touched
          swipe_start = event.touches.item(0).clientX;
        }else{
        swipe_start = null;
        }
      });

      $image_div[0].addEventListener("touchend",function(event){
          event.stopPropagation();
          var offset = 80;//minimum offset considered as swipe are a swipe
          if(swipe_start){
            //just one finger touched
            var end = event.changedTouches.item(0).clientX;

            if(end > swipe_start + offset){
             //a left -> right swipe
            $(".o_pager_previous").click();
            }
            if(end < swipe_start - offset ){
             //a right -> left swipe
             $(".o_pager_next").click();
            }
          // Reset swipe start
          swipe_start = null;
          }
        });

      // Click pager <-
      $image_side_back.click(function(event) {
        event.stopPropagation()
        $(".o_pager_previous").click();
      });
      // ->
      $image_side_next.click(function(event) {
        event.stopPropagation()
        $(".o_pager_next").click();
      });

      // Click modal image
      $image_div.click(function(event) {
          event.stopPropagation()
          var modal = $("#myModal");
          modal.css("display", "none");
        });

  // Handle key press
    $(".o_gallery_view").keydown(function(event) {
    switch(event.which) {
        case 37: // left
        event.stopPropagation();
        $(".o_pager_previous").click();
        break;

        case 39: // right
        event.stopPropagation();
        $(".o_pager_next").click();
        break;

        default: return; // exit this handler for other keys
    }
    event.preventDefault(); // prevent the default action (scroll / move caret)
  });

  // Add to navbar
      $("header[role='banner']").removeClass('gallery-modal').append($result);
    },


// End)
  });

return GalleryRenderer;

});
