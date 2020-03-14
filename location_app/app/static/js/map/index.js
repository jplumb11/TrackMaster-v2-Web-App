//MAP
var map;
var locations;
var state;
var weight;

// IMAGES FOR MAP OBJECTS
var normalMarker = "/static/img/map/dot.svg";
var startMarker = "/static/img/map/start.svg";
var endMarker = "/static/img/map/end.svg";

// SCALES FOR MAP OBJECTS
var startScale = 2;
var endScale = 0.7;
var fScale = 0.6;
var hScale = 1;
var lineW = 5;

// COLORS FOR MAP OBJECTS
var normalColor = "#ff0000";
var highStartMarker = "#ffffff";
var highEndMarker = "#000000";
var highLine = "#000000";

// TIMERS FOR MAP OBJECTS
var timers = {};
var l_timers = {};

// MAP

/** 
 * Makes the map from the passed in data, sets click listeners
 * and calls all map locations
 */
function initialize_map(_locations, _weight, _color) {
    locations = _locations;
    weight = _weight;
    normalColor = _color;
    set_other_colors();
    
    map = new ol.Map({
        target: "map",
        layers: [
            new ol.layer.Tile({
                source: new ol.source.OSM
            })
        ],
        view: new ol.View()
    });
    set_click_listener();
    get_map_all_locations();
}

/** 
 * Sets other colors depending on the favourite color
 */
function set_other_colors() {
    console.log(normalColor);
}

/** 
 * Deletes everything on the map
 */
function reset_map_layers() {
    layers = map.getLayers();
    layers.a = [layers.a[0]];
}

/** 
 * Centers the map so it shows all the dots on the map
 * or if the argument are two dots then it centers the map
 * on them 
 */
function center_map(points = 0) {
    if(points == 0) {
        var dot_layers = [];
        map.getLayers().forEach(function(layer) {
            if(!(layer instanceof ol.layer.Group)) {
                if(layer.get('type') == "dot") {
                    dot_layers.push(layer.getSource().getExtent());
                }
            }
        });
        var area = dot_layers[0];
        for(i = 0; i < dot_layers.length; i++) {
            ol.extent.extend(area, dot_layers[i]);
        }
        map.getView().fit(area, {
            size: map.getSize(),
            maxZoom: 20
        });
    } else {
        var area = points[0].getSource().getExtent();
        ol.extent.extend(area, points[1].getSource().getExtent());
        map.getView().fit(area, {
            size: map.getSize(),
            maxZoom: 20
        });
    }
}

// SELECTION

/** 
 * Decides if all locations should be showed or just 
 * a specific date based on the value in the select form
 */
function get_map_for_selection() {
    var div = document.getElementById("date");
    var date = div.options[div.selectedIndex].value;
    if(date == "all") {
        get_map_all_locations();
    } else {
        get_map_for_date(date);
    }
}

// ALL LOCATIONS

/** 
 * Draws a marker for each location entry and stores the
 * date and time in the marker
 */
function get_map_all_locations() {
    state = 1;
    reset_map_layers();
    for(i = 0; i < locations.length; i++) {
        var location = locations[i];
        var marker_properties = {
            'type': "dot",
            'date': location[2],
            'time': location[3]
        };
        draw_marker(location[0], location[1], marker_properties);
    }
    center_map();
}

// FOR DATE

/** 
 * Draws marker for each location entry on a specified date
 * and connects them with lines also stores data that can be
 * later read by clicking on the marker or the line
 */
function get_map_for_date(date) {
    state = 2;
    reset_map_layers();
    var this_date_loc = [];
    var total_distance = 0;
    var total_calories = 0;
    var last_distance = 0;
    var last_calories = 0;
    for(i = 0; i < locations.length; i++) {
        if(locations[i][2] == date) {
            this_date_loc.push(locations[i]);
        }
    }
    for(i = 0; i < this_date_loc.length - 1; i++) {
        connect_two_locations(this_date_loc[i], this_date_loc[i + 1], i);
        total_distance += get_distance(this_date_loc[i], this_date_loc[i + 1]);
        total_calories += get_calories(this_date_loc[i], this_date_loc[i + 1]);
    }
    this_date_loc = this_date_loc.reverse();
    for(i = 0; i < this_date_loc.length; i++) {
        var location = this_date_loc[i];
        if(i > 0) {
            last_distance += get_distance(this_date_loc[i - 1], this_date_loc[i]);
            last_calories += get_calories(this_date_loc[i - 1], this_date_loc[i]);
        }
        var marker_properties = {
            'type': "dot",
            'special': "",
            'number': i,
            'x': location[0],
            'y': location[1],
            'date': location[2],
            'time': location[3],
            'total_distance': format_distance(total_distance),
            'total_calories': format_calories(total_calories),
            'last_distance': format_distance(last_distance),
            'last_calories': format_calories(last_calories)
        }
        if(i == 0 && this_date_loc.length > 1) {
            var marker = draw_marker(location[0], location[1], marker_properties);
            marker.set('special', "start");
            marker.setZIndex(1000);
            marker.setStyle(get_marker_style(normalColor, startScale, startMarker));
        } else if(i == this_date_loc.length - 1 && this_date_loc.length > 1) {
            var marker = draw_marker(location[0], location[1], marker_properties);
            marker.set('special', "end");
            marker.setZIndex(1000);
            marker.setStyle(get_marker_style(normalColor, endScale, endMarker, [0.37, 0.97]));
        } else {
            draw_marker(location[0], location[1], marker_properties);
        }
    }
    center_map();
}

// MARKER

/** 
 * Draws the marker with set properties and 
 * returns a reference to that marker
 */
function draw_marker(pos1, pos2, _properties) {
    var marker = new ol.layer.Vector({
        source: new ol.source.Vector({
            features: [new ol.Feature({
                geometry: new ol.geom.Point(ol.proj.fromLonLat([pos1, pos2])),
            })]
        }),
        style: get_marker_style(normalColor, fScale, normalMarker)
    });
    marker.setProperties(_properties);
    map.addLayer(marker);
    return marker;
}

/** 
 * Returns a marker style with specified values
 */
function get_marker_style(color, scale, img, anchor = [0.5, 0.5]) {
    return new ol.style.Style({
        image: new ol.style.Icon({
            crossOrigin: "Anonymous",
            scale: scale,
            color: color,
            anchorXUnits: "fraction",
            anchorYUnits: "fraction",
            anchor: anchor,
            src: img
        })
    });
}

// LINE

/** 
 * Connects 2 locations, does the distance, 
 * calories, speed and time calculations and stores 
 * them in line properties
 */
function connect_two_locations(loc1, loc2, num) {
    var pos1 = ol.proj.fromLonLat([loc1[0], loc1[1]]);
    var pos2 = ol.proj.fromLonLat([loc2[0], loc2[1]]);
    var line_properties = {
        'type': "line",
        'number': num,
        'start1': loc2[0],
        'start2': loc2[1],
        'end1': loc1[0],
        'end2': loc1[1],
        'length': format_distance(get_distance(loc1, loc2)),
        'time': format_time(get_time(loc1, loc2)),
        'speed': format_speed(get_speed(loc1, loc2)),
        'calories': format_calories(get_calories(loc1, loc2))
    }
    draw_line(pos1, pos2, line_properties)
}

/** 
 * Draws the line in between 2 positions and applies the 
 * properties to the line
 */
function draw_line(pos1, pos2, _properties) {
    var line = new ol.layer.Vector({
        source: new ol.source.Vector({
            features: [new ol.Feature({
                geometry: new ol.geom.LineString([pos1, pos2])
            })]
        }),
        style: get_line_style(normalColor)
    });
    line.setProperties(_properties);
    map.addLayer(line);
}

/** 
 * Returns a line style with specified color
 */
function get_line_style(color) {
    return new ol.style.Style({
        stroke: new ol.style.Stroke({
            color: color,
            width: lineW
        })
    });
}

// CLICK LISTENER

/** 
 * Sets a click listener on the map which will monitor if a line 
 * or marker are clicked and in which state and based of that 
 * will show alerts displaying all the data that was stored 
 * in the properties of the clicked object
 */
function set_click_listener() {
    map.getViewport().addEventListener("click", function(event) {
        var layer = map.forEachFeatureAtPixel(map.getEventPixel(event),
                                              function(feature, layer) {
            return layer;
        });
        if(layer) {
            if(layer.get('type') == "dot") {
                get_dot_data(layer);
            } else if(layer.get('type') == "line") {
                get_line_data(layer);
                highlight_line(layer);
                var dots = get_start_end(layer);
                center_map(dots);
            }
        }
    });
}

/** 
 * Takes in an array of strings and makes an alert out of that
 */
function show_alert(info) {
    var text = "";
    for(i = 0; i < info.length; i++) {
        text += info[i] + "\n";
    }
    alert(text);
}

/** 
 * Shows marker data depending on which state it is and if
 * it is a special marker
 */
function get_dot_data(layer) {
    if(state == 1) {
        show_alert(["You were here on", 
                    "Date: " + layer.get('date'),
                    "Time: " + layer.get('time')]);
    } else {
        if(layer.get('special') == "start") {
            show_alert(["Your journey started here!", 
                        "Time: " + layer.get('time'), 
                        "Your total distance is: " + layer.get('total_distance'), 
                        "Your total calories are: " + layer.get('total_calories')]);
        } else if(layer.get('special') == "end") {
            show_alert(["Your journey ended here!",
                        "Time: " + layer.get('time'), 
                        "Your total distance is: " + layer.get('total_distance'), 
                        "Your total calories are: " + layer.get('total_calories')]);
        } else {
            show_alert(["Time: " + layer.get('time'), 
                        "Distance from start: " + layer.get('last_distance'), 
                        "Calories from start: " + layer.get('last_calories'), 
                        "Your total distance is: " + layer.get('total_distance'), 
                        "Your total calories are: " + layer.get('total_calories')]);
        }
    }
}

/** 
 * Shows line data - only accesible in state 2
 */
function get_line_data(layer) {
    show_alert(["Distance: " + layer.get('length'),
                "Time: " + layer.get('time'), 
                "Speed: " + layer.get('speed'),
                "Calories: " + layer.get('calories')]);
}

/** 
 * Highlights the line for 4 seconds and updates it's timer
 * in the dictionary based on its number
 */
function highlight_line(line) {
    line.setStyle(get_line_style(highLine));
    clearTimeout(l_timers[line.get('number')]);
    l_timers[line.get('number')] = setTimeout(function() {
        line.setStyle(get_line_style(normalColor));
    }, 4000);
}

/** 
 * Highlights the marker for 4 seconds and updates it's timer
 * in the dictionary based on its number
 */
function highlight_marker(marker, color) {
    marker.setStyle(get_marker_style(color, hScale, normalMarker));
    marker.setZIndex(100);
    clearTimeout(timers[marker.get('number')]);
    timers[marker.get('number')] = setTimeout(function() {
        marker.setStyle(get_marker_style(normalColor, fScale, normalMarker));
    }, 4000);
}

/** 
 * Finds the start and the end of a line and if they aren't 
 * special markers it highlights them
 */
function get_start_end(layer) {
    var start;
    var end;
    map.getLayers().forEach(function(_layer) {
        if(!(_layer instanceof ol.layer.Group)) {
            if(_layer.get('type') == "dot") {
                if(_layer.get('x') == layer.get('start1') && _layer.get('y') == layer.get('start2')) {
                    start = _layer;
                } else if(_layer.get('x') == layer.get('end1') && _layer.get('y') == layer.get('end2')) {
                    end = _layer;
                }
            }
        }
    });
    if(start.get('special') == "") {
        highlight_marker(start, highStartMarker)
    }
    if(end.get('special') == "") {
        highlight_marker(end, highEndMarker)
    }
    return [start, end];
}