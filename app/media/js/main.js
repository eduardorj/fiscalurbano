/*
#######################################################################
#
# Author: Eduardo Francellino
#
#######################################################################
*/

$(function(){

	var lat = geoip_latitude();
	var lon = geoip_longitude();

	var url_end = "?nocache=" + (new Date()).valueOf();

	var marker_count = 1;

	$("#map").gmap3(
		{
				action: 'init', 
				options: { 
					center:[lat,lon], zoom: 11
				},
					events:{
						rightclick:function(map, event){
							current = event;
							$(this).gmap3( { 
								action: 'addMarkers', 
								markers:[ {lat:current.latLng.lat(), lng:current.latLng.lng(), data:'<b>Policarpo esteve aqui!</b> Ponto : ' + marker_count++  , options:{ suppressInfoWindows: false }} ],
								marker:{options:{ draggable: true },
								events:{
									mouseover:function(marker, event, data){
										$(this).gmap3({action:'addinfowindow', anchor:marker, options:{content: data}});
									},
									mouseout: function(){
										var infowindow = $(this).gmap3({action:'get', name:'infowindow'});
											if (infowindow){
												infowindow.close();
											}
									}										
								}
								}
								});
						}
					}
			},
			{
				action: 'addKmlLayer',
				url: 'http://www.gmap3.net/kml/rungis.kml',
				options:{ suppressInfoWindows: false },
				tag:'chk1'
			},
			{
				action: 'addKmlLayer',
				url: 'http://www.gmap3.net/kml/sogaris.kml',
				options:{ suppressInfoWindows: false },
				tag:'chk2'
			},
			{
				action: 'addKmlLayer',
				url: 'http://kmlx.herokuapp.com/kml' + url_end,
				options:{ suppressInfoWindows: false },
				tag:'chk3'
			}
		);

/**

	$("select").multiselect({
		click: function(event, ui){
			var map = $('#map').gmap3('get');
			kml = getKML(ui.value);
			enableKML(kml, ui.checked ? map : null)

		},
		checkAll: function(){
			
			var map = $('#map').gmap3('get');
			
			$("select option").each(function(){
					kml = getKML($(this).val())
					enableKML(kml, map)
			});
						
		},
		uncheckAll: function(){
			clearAllOpenlayers();
		}
	});
**/

	clearAllOpenlayers();
		
	$('#btnVai').click(function(){		
		map=$('#map').gmap3({action:'get',name:'map'});
	   center=map.getCenter();
	   lat=center.lat();
	   lng=center.lng();
	   zoom=map.getZoom();
		
		//alert(lat + ' X ' + lng)
		
		var myEvent = {lat: "calEvent.id", lng: "calEvent.start" };
		
		alert(1)

		$.post("/event/save-json", { 
		    name: "Monty",
		    food: "Spam" 
		},
		    function(data) {
		        alert(data);
		    }
		);

		alert(2)		
/**		
		$.ajax({
		        url: '/event/save-json/',
		        type: 'POST',
		        contentType: 'application/json; charset=utf-8',
		        data: $.toJSON(myEvent),
		        dataType: 'text',
		        success: function(result) {
		            alert(result.Result);
		        }
		    });
**/		
	});
	
});

function getKML(tag_id){
	return $('#map').gmap3({
		action: 'get',
		name: 'kmllayer',
		tag: tag_id
	});	
}

function enableKML(kml_obj, map_obj){
	kml_obj.setMap( map_obj );	
}

function clearAllOpenlayers(){
	enableKML(getKML('chk1'), null)
	enableKML(getKML('chk2'), null)
	enableKML(getKML('chk3'), null)

//	$("select option").each(function(){
//			kml = getKML($(this).val())
//			enableKML(kml, null)
//	});

}