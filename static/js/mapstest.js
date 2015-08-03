var map;
var testaddress = '{{ startup.address }}';
function initialize() {
  map = new google.maps.Map(document.getElementById('map-canvas'), {
    zoom: 8,
    center: {lat: -34.397, lng: 150.644}
  });
  testaddress;
}

google.maps.event.addDomListener(window, 'load', initialize);