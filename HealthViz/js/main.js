
base_url = 'http://192.168.43.3:8000';


$(document).ready(function(){
    $(".login-submit").click(function(){
       
        username=$(".username").val();
        password=$(".pass").val();
        
        $.ajax({
            type : "POST",
            url: base_url+'/api/v1/login',
            data: {
                "username" : username,
                "password" : password
            },
            dataType: 'json',
            success: function(data) {
                localStorage.setItem('username',username);
                $('.profile-wraper').show('slide', {direction: 'right'}, 500);
            }
       });
    });
});




var retailerCircle;
var circles = [];
var circle_two = [];


function removeAllcircles() {
    for(var i in circles) {
        circles[i].setMap(null);
    }
    circles = []; 
    console.log(circles);
}

function geoLoc(place, callLatLong) {
    alert(place);
    $.ajax({
        type : "GET",
        url: ' http://maps.googleapis.com/maps/api/geocode/json?address='+place+'&sensor=true',
        dataType: 'json',
        success: function(data) {
            var LatLongValue = data.results[0].geometry.location;
            return callLatLong(LatLongValue);
        }
    });
} 

$(document).ready(function(){

    $(".des").keypress(function (e) {
        var token = $(".locat").val();
        console.log(token);
        
            var key = e.which; 
            if(key === 13) {

                if(token === '') {
                    var dis = $(".des").val();
                    geoLoc(location, function(output){
                    console.log(output);
                        $.ajax({
                            type : "POST",
                            url: base_url+'/api/v1/geo_distribution',
                            data: {
                                "disease_name" : dis
                            },
                            dataType: 'json',
                            success: function(data) {
                                console.log(data);

                                removeAllcircles();
                                initMap(data, 1);
                            }
                        });
                    });
                }
                else {
                    var dis = $(".des").val();
                    var location = $(".locat").val();
                    geoLoc(location, function(output){
                    console.log(output);
                        $.ajax({
                            type : "POST",
                            url: base_url+'/api/v1/custom_plot',
                            data: {
                                "username" : "test",
                                "password" : "test",
                                "disease" : dis,
                                "lat" : output.lat,
                                "lng" : output.lng,
                                "place" : location
                            },
                            dataType: 'json',
                            success: function(data) {
                                console.log(data);

                                removeAllcircles();
                                initMap(data, 2);
                            }
                        });
                    });
                }
            }
    });

    $(".button_map").click(function(){
        $("map").css("left", "0px").show('slide', {direction: 'right'}, 500);
        $('.place input').slideDown();
    });

    $(".fa-plus-circle").click(function(){
        $("add").fadeIn();
    });

    
    $(".button_add").click(function(){
        $("plot").show('slide', {direction: 'right'}, 500);
    });

    

    var retailermap = {

        chicago: {
            center: {lat: 41.878, lng: -87.629},
            population: 2714856
        },
        newyork: {
            center: {lat: 40.714, lng: -74.005},
            population: 8405837
        },
        losangeles: {
            center: {lat: 34.052, lng: -118.243},
            population: 3857799
        },
        vancouver: {
            center: {lat: 49.25, lng: -123.1},
            population: 603502
        }
    };

    initMap(retailermap, 1);
    $("#close").click(function(){ 
        $('add').fadeOut();
    });
    $("#add_submit").click(function(){
        var location = $('#add_loc').val();
        var dis = $('#add_dis').val();
        console.log(location);
        geoLoc(location, function(output){
            console.log(output);

            $.ajax({
                type : "POST",
                url: base_url+'/api/v1/register_disease',
                data: {
                    "username" : "test",
                    "password" : "test",
                    "disease_name" : dis,
                    "lat" : output.lat,
                    "lon" : output.lng,
                    "place" : location
                },
                dataType: 'json',
                success: function(data) {
                    $("add").fadeOut();
                }
            });

        });
    });

    $.ajax({
        type : "POST",
        url: base_url+'/api/v1/geo_distribution',
        data: {
            "disease_name" : "parkinson"
        },
        dataType: 'json',
        success: function(data) {
            console.log(data);
            removeAllcircles();
            initMap(data, 1);
        }
    });
});

function getData(sendData) {
    $.ajax({
        type : "POST",
        url: base_url+'/api/v1/geo_distribution',
        data: {
            "disease_name" : "parkinson"
        },
        dataType: 'json',
        success: function(data) {
            var circle_datas;
            for(i = 0; i < data.length; i++) {
                geoLoc(data[i].place, function(output){
                    var circle_data = {
                        center: {
                            lat: output.lat,
                            long: output.long
                        },
                        population: data.total
                    };
                    circle_datas.push(circle_data);
                });
            }
            return sendData(circle_datas);
        }
    });
}    



function initMap(retailermap, typ) {
// Create the map.
    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 11,
        center: {
        lat: 28.6618976,
        lng: 77.22739580000007
        },
        styles: [
                {
                    "featureType": "administrative",
                    "elementType": "geometry.fill",
                    "stylers": [
                        {
                            "color": "#d6e2e6"
                        }
                    ]
                },
                {
                    "featureType": "administrative",
                    "elementType": "geometry.stroke",
                    "stylers": [
                        {
                            "color": "#cfd4d5"
                        }
                    ]
                },
                {
                    "featureType": "administrative",
                    "elementType": "labels.text.fill",
                    "stylers": [
                        {
                            "color": "#7492a8"
                        }
                    ]
                },
                {
                    "featureType": "administrative.neighborhood",
                    "elementType": "labels.text.fill",
                    "stylers": [
                        {
                            "lightness": 25
                        }
                    ]
                },
                {
                    "featureType": "landscape.man_made",
                    "elementType": "geometry.fill",
                    "stylers": [
                        {
                            "color": "#dde2e3"
                        }
                    ]
                },
                {
                    "featureType": "landscape.man_made",
                    "elementType": "geometry.stroke",
                    "stylers": [
                        {
                            "color": "#cfd4d5"
                        }
                    ]
                },
                {
                    "featureType": "landscape.natural",
                    "elementType": "geometry.fill",
                    "stylers": [
                        {
                            "color": "#dde2e3"
                        }
                    ]
                },
                {
                    "featureType": "landscape.natural",
                    "elementType": "labels.text.fill",
                    "stylers": [
                        {
                            "color": "#7492a8"
                        }
                    ]
                },
                {
                    "featureType": "landscape.natural.terrain",
                    "elementType": "all",
                    "stylers": [
                        {
                            "visibility": "off"
                        }
                    ]
                },
                {
                    "featureType": "poi",
                    "elementType": "geometry.fill",
                    "stylers": [
                        {
                            "color": "#dde2e3"
                        }
                    ]
                },
                {
                    "featureType": "poi",
                    "elementType": "labels.text.fill",
                    "stylers": [
                        {
                            "color": "#588ca4"
                        }
                    ]
                },
                {
                    "featureType": "poi",
                    "elementType": "labels.icon",
                    "stylers": [
                        {
                            "saturation": -100
                        }
                    ]
                },
                {
                    "featureType": "poi.park",
                    "elementType": "geometry.fill",
                    "stylers": [
                        {
                            "color": "#a9de83"
                        }
                    ]
                },
                {
                    "featureType": "poi.park",
                    "elementType": "geometry.stroke",
                    "stylers": [
                        {
                            "color": "#bae6a1"
                        }
                    ]
                },
                {
                    "featureType": "poi.sports_complex",
                    "elementType": "geometry.fill",
                    "stylers": [
                        {
                            "color": "#c6e8b3"
                        }
                    ]
                },
                {
                    "featureType": "poi.sports_complex",
                    "elementType": "geometry.stroke",
                    "stylers": [
                        {
                            "color": "#bae6a1"
                        }
                    ]
                },
                {
                    "featureType": "road",
                    "elementType": "labels.text.fill",
                    "stylers": [
                        {
                            "color": "#41626b"
                        }
                    ]
                },
                {
                    "featureType": "road",
                    "elementType": "labels.icon",
                    "stylers": [
                        {
                            "saturation": -45
                        },
                        {
                            "lightness": 10
                        },
                        {
                            "visibility": "on"
                        }
                    ]
                },
                {
                    "featureType": "road.highway",
                    "elementType": "geometry.fill",
                    "stylers": [
                        {
                            "color": "#c1d1d6"
                        }
                    ]
                },
                {
                    "featureType": "road.highway",
                    "elementType": "geometry.stroke",
                    "stylers": [
                        {
                            "color": "#a6b5bb"
                        }
                    ]
                },
                {
                    "featureType": "road.highway",
                    "elementType": "labels.icon",
                    "stylers": [
                        {
                            "visibility": "on"
                        }
                    ]
                },
                {
                    "featureType": "road.highway.controlled_access",
                    "elementType": "geometry.fill",
                    "stylers": [
                        {
                            "color": "#9fb6bd"
                        }
                    ]
                },
                {
                    "featureType": "road.arterial",
                    "elementType": "geometry.fill",
                    "stylers": [
                        {
                            "color": "#ffffff"
                        }
                    ]
                },
                {
                    "featureType": "road.local",
                    "elementType": "geometry.fill",
                    "stylers": [
                        {
                            "color": "#ffffff"
                        }
                    ]
                },
                {
                    "featureType": "transit",
                    "elementType": "labels.icon",
                    "stylers": [
                        {
                            "saturation": -70
                        }
                    ]
                },
                {
                    "featureType": "transit.line",
                    "elementType": "geometry.fill",
                    "stylers": [
                        {
                            "color": "#b4cbd4"
                        }
                    ]
                },
                {
                    "featureType": "transit.line",
                    "elementType": "labels.text.fill",
                    "stylers": [
                        {
                            "color": "#588ca4"
                        }
                    ]
                },
                {
                    "featureType": "transit.station",
                    "elementType": "all",
                    "stylers": [
                        {
                            "visibility": "off"
                        }
                    ]
                },
                {
                    "featureType": "transit.station",
                    "elementType": "labels.text.fill",
                    "stylers": [
                        {
                            "color": "#008cb5"
                        },
                        {
                            "visibility": "on"
                        }
                    ]
                },
                {
                    "featureType": "transit.station.airport",
                    "elementType": "geometry.fill",
                    "stylers": [
                        {
                            "saturation": -100
                        },
                        {
                            "lightness": -5
                        }
                    ]
                },
                {
                    "featureType": "water",
                    "elementType": "geometry.fill",
                    "stylers": [
                        {
                            "color": "#a6cbe3"
                        }
                    ]
                }
            ],
        mapTypeId: 'terrain'
    });

    if (typ === 1) {
        for (var retailer in retailermap) {
                console.log(retailermap[retailer].center);
                var retailerCircle = new google.maps.Circle({
                strokeColor: '#FF0000',
                strokeOpacity: 0.8,
                strokeWeight: 2,
                fillColor: '#FF0000',
                fillOpacity: 0.35,
                map: map,
                center: retailermap[retailer].center,
                radius: Math.sqrt(retailermap[retailer].population) * 100
            });
            circles.push(retailerCircle);
        }
    }
    else {
        for (var retailer in retailermap) {
                console.log(retailermap.center);
                var retailerCircle = new google.maps.Circle({
                strokeColor: '#FF0000',
                strokeOpacity: 0.8,
                strokeWeight: 2,
                fillColor: '#FF0000',
                fillOpacity: 0.35,
                map: map,
                center: retailermap.center,
                radius: Math.sqrt(retailermap.population) * 100
            });
            circles.push(retailerCircle);
        }
    }
}
