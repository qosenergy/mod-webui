/* Copyright (C) 2009-2015:
   Gabes Jean, naparuba@gmail.com
   Gerhard Lausser, Gerhard.Lausser@consol.de
   Gregory Starck, g.starck@gmail.com
   Hartmut Goebel, h.goebel@goebel-consult.de
   Andreas Karfusehr, andreas@karfusehr.de
   Frederic Mohier, frederic.mohier@gmail.com

   This file is part of Shinken.

   Shinken is free software: you can redistribute it and/or modify
   it under the terms of the GNU Affero General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.

   Shinken is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU Affero General Public License for more details.

   You should have received a copy of the GNU Affero General Public License
   along with Shinken.  If not, see <http://www.gnu.org/licenses/>.
*/

var _already_loaded = {};

// when we show a custom view tab, we lazy load it :D
function show_custom_view(p){
   var hname = p.data('element');
   var cvname = p.data('name');
   console.debug('Request for loading custom view: ', cvname, ' for ', hname);

   if (cvname in _already_loaded){
      return;
   }

   var _t = new Date().getTime();
   $("#cv"+cvname+" .panel-body").load('/cv/'+cvname+'/'+hname+"?_="+_t, function(response, status, xhr) {
      if (status == "error") {
         var msg = "Sorry but there was an error: ";
         $('#cv'+cvname).html(msg + xhr.status + " " + xhr.statusText);
      } else {
         // Panel container height is updated with the custom view height ...
         $("#cv"+cvname+" .panel-body").each(function() {
            $(this).css('height', $('#cv_'+cvname).height() + "px");
         });
         console.debug('Loaded custom view: ', cvname);
      }
   });

   _already_loaded[cvname] = true;
}

function reload_custom_view(name){
   // Be sure to remove the panel from already loaded panels, else it won't load
   delete _already_loaded[name];
   show_custom_view($('#tab-cv-'+name));
}