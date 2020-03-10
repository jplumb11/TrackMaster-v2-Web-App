// TIME
function get_time(loc1, loc2) {
    var miliseconds = Math.abs(new Date('1998/01/01 ' + loc1[3]) -
                               new Date('1998/01/01 ' + loc2[3]));
    return (miliseconds / 1000);
}

function format_time(seconds) {
    var miliseconds = seconds * 1000;
    if(seconds > 60) {
        return new Date(miliseconds).getMinutes() + " minutes and " +
               new Date(miliseconds).getSeconds() + " seconds";
    } else {
        return new Date(miliseconds).getSeconds() + " seconds";
    }
}

// DISTANCE
function toRad(x) {
   return x * Math.PI / 180;
}

function get_distance(loc1, loc2) {
    var x1 = loc2[1] - loc1[1];
    var dLat = toRad(x1);
    var x2 = loc2[0] - loc1[0];
    var dLon = toRad(x2);
    var a = Math.sin(dLat / 2) * Math.sin(dLat / 2) +
            Math.cos(toRad(loc1[1])) * Math.cos(toRad(loc2[1])) *
            Math.sin(dLon / 2) * Math.sin(dLon / 2);
    var c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
    var distance = 6371 * c;
    return (distance * 1000);
}

function format_distance(distance) {
    if (distance > 1000) {
        return (Math.round((distance / 1000) * 100) / 100) + " kilometers";
    } else {
        return (Math.round(distance * 100) / 100) + " meters";
    }
}

// SPEED
function get_speed(loc1, loc2) {
    var distance = get_distance(loc1, loc2);
    var time = get_time(loc1, loc2);
    var speed = distance / time;
    
    return (speed * 3.6);
}

function format_speed(speed) {
    return (Math.round(speed * 100) / 100) + " km/h";
}

// CALORIES
function get_MET(speed) {
    if ( 1 <= speed && speed < 3) {
        return 2;
    } else if ( 3 <= speed && speed < 5) {
        return 2.5;
    } else if ( 5 <= speed && speed < 8) {
        return 5;
    } else if ( 8 <= speed && speed < 10) {
        return 8;
    } else if ( 10 <= speed && speed < 13) {
        return 11;
    } else if ( 13 <= speed && speed < 16) {
        return 13.5;
    } else if ( 16 <= speed && speed < 35){
        return 16;
    } else {
        return 1;
    }
}

function get_calories(loc1, loc2) {
    var speed = get_speed(loc1, loc2);
    var time = get_time(loc1, loc2);
    var met = get_MET(speed);
    
    return (((met * 3.5 * weight) / 200) * (time/60));
}

function format_calories(calories) {
    return (Math.round(calories * 100) / 100) + " calories";
}