var map;
var mapLat = 52.407633; 
var mapLng = -1.496947; 
var mapDefaultZoom = 12;

function initialize_map() {
    map = new ol.Map({
        target: "map",
        layers: [
                new ol.layer.Tile({
                                source: new ol.source.OSM({
                                    url: "https://a.tile.openstreetmap.org/{z}/{x}/{y}.png"
                                    })
                                  })
                ],
        view: new ol.View({
            center: ol.proj.fromLonLat([mapLng, mapLat]),
            zoom: mapDefaultZoom
           
           })
       });
    }
    
function add_map_point() {
    for (i=0; i<lat.length; i++) 
    {
        var vectorLayer = new ol.layer.Vector({
            source:new ol.source.Vector({
                features: [new ol.Feature({
                geometry: new ol.geom.Point(ol.proj.transform([parseFloat(lng[i]), parseFloat(lat[i])], 'EPSG:4326', 'EPSG:3857')),
                })]
             }),
            style: new ol.style.Style({
                image: new ol.style.Icon({
                    anchor: [0.5, 0.5],
                    anchorXUnits: "fraction",
                    anchorYUnits: "fraction",
                    src: "https://upload.wikimedia.org/wikipedia/commons/e/ec/RedDot.svg" //get an image for our red dot
                    })
                })
            });
    
        map.addLayer(vectorLayer);
    }
}