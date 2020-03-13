var locations;
var weight;
var dates;
var distance = 0;
var calories = 0;
var tdistance = 0;
var tcalories = 0;
var tspeed = 0;
var color;

function setup(_locations, _weight, _dates, _color) {
    locations = _locations;
    weight = _weight;
    dates = _dates;
    color = _color;
    
    window.onload = function(){
        cycle_through_dates();
        console.log(document.getElementById("qw").textContent);
        document.getElementById("type").innerHTML = '<p class="info">' + "Adventurer" + '</p>';
        document.getElementById("speed").innerHTML = '<p class="info">' + format_speed(tspeed) + '</p>';
        document.getElementById("color").style.backgroundColor = color;
        document.getElementById("tdist").innerHTML = '<p class="info">' + format_distance(tdistance) + '</p>';
        document.getElementById("tcal").innerHTML = '<p class="info">' + format_calories(tcalories) + '</p>';
        document.getElementById("cal").innerHTML = '<p class="info">' + format_calories(calories) + '</p>';
        document.getElementById("dist").innerHTML = '<p class="info">' + format_distance(distance) + '</p>';
    };
}

function cycle_through_dates() {
    for(i = 0; i < dates.length; i++) {
        var this_date_loc = [];
        var this_date_dist = 0;
        var this_date_cal = 0;
        for(j = 0; j < locations.length; j++) {
            if(locations[j][2] == dates[i]) {
                this_date_loc.push(locations[j]);
            }
        }
        for(j = 0; j < this_date_loc.length - 1; j++) {
            var dis = get_distance(this_date_loc[j], this_date_loc[j + 1]);
            this_date_dist += dis;
            this_date_cal += get_calories(this_date_loc[j], this_date_loc[j + 1]);
            var speed = get_speed(this_date_loc[j], this_date_loc[j + 1]);
            var time = get_time(this_date_loc[j], this_date_loc[j + 1]);
            if(speed > tspeed && dis < 100 && time > 2) {
                tspeed = speed;
            } else if(speed > tspeed && time > 10) {
                tspeed = speed;
            }
        }
        distance += this_date_dist;
        calories += this_date_cal;
        if(this_date_dist > tdistance) {
            tdistance = this_date_dist;
        }
        if(this_date_cal > tcalories) {
            tcalories = this_date_cal;
        }
    }
}
