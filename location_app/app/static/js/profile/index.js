// USER
var locations;
var weight;
var dates;
// DATA
var distance = 0;
var calories = 0;
var tdistance = 0;
var tcalories = 0;
var tspeed = 0;

/** 
 * Runs the calculations for dates and displays the calculated data 
 * after the page loads
 */
function setup(_locations, _weight, _dates) {
    locations = _locations;
    weight = _weight;
    dates = _dates;
    window.onload = function() {
        cycle_through_dates();
        document.getElementById("type").innerHTML = get_type();
        document.getElementById("speed").innerHTML = format_speed(tspeed);
        document.getElementById("tdist").innerHTML = format_distance(tdistance);
        document.getElementById("tcal").innerHTML = format_calories(tcalories);
        document.getElementById("cal").innerHTML = format_calories(calories);
        document.getElementById("dist").innerHTML = format_distance(distance);
    };
}

/** 
 * Goes through all the dates and does the calculations 
 * for each date individually
 */
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
            var dis = get_distance(this_date_loc[j],
                                   this_date_loc[j + 1]);
            this_date_dist += dis;
            this_date_cal += get_calories(this_date_loc[j],
                                          this_date_loc[j + 1]);
            var speed = get_speed(this_date_loc[j],
                                  this_date_loc[j + 1]);
            var time = get_time(this_date_loc[j],
                                this_date_loc[j + 1]);
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

/** 
 * Returns a type based on your top distance in a day
 */
function get_type() {
    if(tdistance < 1000) {
        return "Couch Potato"
    } else if(tdistance < 3000) {
        return "Couch Potato"
    } else if(tdistance < 5000) {
        return "Minimalist"
    } else if(tdistance < 8000) {
        return "Average Joe"
    } else if(tdistance < 11000) {
        return "Enjoyer"
    } else if(tdistance < 14000) {
        return "Adventurer"
    } else if(tdistance < 17000) {
        return "Long Legs"
    } else if(tdistance < 21000) {
        return "Extreme"
    } else {
        return "Top Dog"
    }
}