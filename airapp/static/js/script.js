/* script */
function initialize() {
  var title = document.title;
  if (title == "Register"){
    var latlng = new google.maps.LatLng(28.5355161,77.39102649999995);
     var map = new google.maps.Map(document.getElementById('map'), {
       center: latlng,
       zoom: 13
     });
     var marker = new google.maps.Marker({
       map: map,
       position: latlng,
       draggable: true,
       anchorPoint: new google.maps.Point(0, -29)
    });
     var input = document.getElementById('searchInput');
     map.controls[google.maps.ControlPosition.TOP_LEFT].push(input);
     var geocoder = new google.maps.Geocoder();
     var autocomplete = new google.maps.places.Autocomplete(input);
     autocomplete.setComponentRestrictions({'country': 'in'});
     autocomplete.bindTo('bounds', map);
     var infowindow = new google.maps.InfoWindow();
     autocomplete.addListener('place_changed', function() {
         infowindow.close();
         marker.setVisible(false);
         var place = autocomplete.getPlace();
         if (!place.geometry) {
             window.alert("Autocomplete's returned place contains no geometry");
             return;
         }

         // If the place has a geometry, then present it on a map.
         if (place.geometry.viewport) {
             map.fitBounds(place.geometry.viewport);
         } else {
             map.setCenter(place.geometry.location);
             map.setZoom(17);
         }

         marker.setPosition(place.geometry.location);
         marker.setVisible(true);

         bindDataToForm(place.formatted_address,place.geometry.location.lat(),place.geometry.location.lng());
         infowindow.setContent(place.formatted_address);
         infowindow.open(map, marker);

     });
     // this function will work on marker move event into map
     google.maps.event.addListener(marker, 'dragend', function() {
         geocoder.geocode({'latLng': marker.getPosition()}, function(results, status) {
         if (status == google.maps.GeocoderStatus.OK) {
           if (results[0]) {
               bindDataToForm(results[0].formatted_address,marker.getPosition().lat(),marker.getPosition().lng());
               infowindow.setContent(results[0].formatted_address);
               infowindow.open(map, marker);
           }
         }
         });
     });
  }
  else{
       var input = document.getElementById('searchInput');
        var autocomplete = new google.maps.places.Autocomplete(input);
        autocomplete.setComponentRestrictions({'country': 'in'});  google.maps.event.addListener(autocomplete, 'place_changed', function() {
          var place = autocomplete.getPlace();
          var lat = place.geometry.location.lat();
          var lng = place.geometry.location.lng();
          var address = place.formatted_address;
          httpGet(lat,lng);

    });

  }


}
function setAll(text) {
    var obj = JSON.parse(text);
    var params = obj.data.aqiParams;
    for (var i = 0; i < params.length; i++) {
        var name = ((params[i].name).toString()).toLowerCase();
        var value = (params[i].value).toString()
        name = name.replace(/[\W_]/g, "")
        if(document.getElementById(name).innerHTML){
          console.log(name);
        }
        document.getElementById(name).innerHTML = value;
    }
    var status = obj.data.text.toString();
    var alert = obj.data.alert.toString();
    var value = obj.data.value.toString();
    var updated = obj.data.updated.toString();
    var source = obj.data.source.name.toString();
    var temp = obj.data.temp.toString();
    var color = obj.data.color.toString();
    document.getElementById("status").innerHTML = status;
    document.getElementById("value").innerHTML = value;
    document.getElementById("details").innerHTML = 'Updated on: '+updated;
                                                    // '\n Temperature: '+temp+
                                                    //   '\nsource: '+source;
    document.getElementById("desc").innerHTML = 'Description: '+alert+
                                                '<br> Source: '+source;
    document.getElementById("desc").style.backgroundColor = color;
}
function httpGet(lat,lng)
{
    var url = 'http://api.airpollutionapi.com/1.0/aqi?'+'lat='+lat+'&lon='+lng+
                  '&APPID=m953d6onf11vvufmc8gmugatqb';
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function(){
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
            setAll(xmlHttp.responseText);
    }
    xmlHttp.open("GET", url, true); // true for asynchronous
    xmlHttp.send(null);
}

function bindDataToForm(address,lat,lng){
   document.getElementById('locationid').value = address;
   document.getElementById('coordinatesid').value = ((lat.toString()).concat(",",lng.toString())).toString();
}

google.maps.event.addDomListener(window, 'load', initialize);
