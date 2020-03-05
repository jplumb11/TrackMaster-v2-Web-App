var map;
var locations;
var dates;
var mapLat = 52.407633;
var mapLng = -1.496947;
var mapDefaultZoom = 15;
var mapJourneyZoom = 20;

function initialize_map(loc, dat) {
    locations = loc;
    dates = dat;
    map = new ol.Map({
        target: "map",
        layers: [
            new ol.layer.Tile({
                source: new ol.source.OSM
            })
        ],
        view: new ol.View({
            center: ol.proj.fromLonLat([mapLng, mapLat]),
            zoom: mapDefaultZoom
        })
    });
    get_map_all_locations();
}

function reset_map_layers() {
    layers = map.getLayers();
    layers.a = [layers.a[0]];
}

function get_map_all_locations() {
    reset_map_layers();
    for(i = 0; i < locations.length; i++) {
        add_map_point(locations[i]);
    }
    var new_center = get_average(locations);
    map.getView().setCenter(ol.proj.fromLonLat([new_center[0], new_center[1]]));
    map.getView().setZoom(mapDefaultZoom);
}

function get_map_for_date(date) {
    reset_map_layers();
    var this_date_loc = [];
    for(i = 0; i < locations.length; i++) {
        if(locations[i][2] == date) {
            this_date_loc.push(locations[i]);
        }
    }
    for(i = 0; i < this_date_loc.length - 1; i++) {
        add_map_lines(this_date_loc[i], this_date_loc[i + 1]);
    }
    for(i = 0; i < this_date_loc.length; i++) {
        if (i == 0 && this_date_loc.length > 1) {
            add_map_point(this_date_loc[i], '#0000ff');
        } else if (i == this_date_loc.length - 1 && this_date_loc.length > 1) {
            add_map_point(this_date_loc[i], '#00ff00');
        } else {
            add_map_point(this_date_loc[i]);
        }
    }
    var new_center = get_average(this_date_loc);
    map.getView().setCenter(ol.proj.fromLonLat([new_center[0], new_center[1]]));
    map.getView().setZoom(mapJourneyZoom);
}

function get_average(array_in) {
    var center = [0, 0];
    for(i = 0; i < array_in.length; i++) {
        center[0] += array_in[i][0];
        center[1] += array_in[i][1];
    }
    return [center[0] / array_in.length, center[1] / array_in.length]
}

function add_map_point(location, color = '#ff0000') {
    var vectorLayer = new ol.layer.Vector({
        source: new ol.source.Vector({
            features: [new ol.Feature({
                geometry: new ol.geom.Point(ol.proj.fromLonLat([location[0], location[1]])),
            })]
        }),
        style: new ol.style.Style({
            image: new ol.style.Icon({
                crossOrigin: "Anonymous",
                scale: 0.5,
                color: color,
                anchorXUnits: "fraction",
                anchorYUnits: "fraction",
                src: "https://upload.wikimedia.org/wikipedia/commons/7/7b/WhiteDot.svg"
            })
        })
    });
    map.addLayer(vectorLayer);
}

function add_map_lines(loc1, loc2) {
    var pos1 = ol.proj.fromLonLat([loc1[0], loc1[1]]);
    var pos2 = ol.proj.fromLonLat([loc2[0], loc2[1]]);
    var lineStyle = [
        new ol.style.Style({
            stroke: new ol.style.Stroke({
                color: '#ff0000',
                width: 2
            })
        })
    ];
    var myLine = new ol.layer.Vector({
        source: new ol.source.Vector({
            features: [new ol.Feature({
                geometry: new ol.geom.LineString([pos1, pos2]),
                name: 'Line',
            })]
        })
    });
    myLine.setStyle(lineStyle);
    map.addLayer(myLine);
}