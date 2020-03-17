// TIME

/** 
 * Returns a difference between 2 dates in seconds
 */
function get_time(loc1, loc2) {
    var miliseconds = Math.abs(new Date('1998/01/01 ' + loc1[3]) -
                               new Date('1998/01/01 ' + loc2[3]));
    return (miliseconds / 1000);
}

/** 
 * Formats time given in seconds
 */
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

/** 
 * Transfers an angle from degrees to radians
 */
function toRad(x) {
   return x * Math.PI / 180;
}

/** 
 * Calculates distance in meters between 2 points
 * using Haversine formula
 */
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

/** 
 * Formats distance given in meters
 */
function format_distance(distance) {
    if (distance > 1000) {
        return (Math.round((distance / 1000) * 100) / 100) + " kilometers";
    } else {
        return (Math.round(distance * 100) / 100) + " meters";
    }
}

// SPEED

/** 
 * Returns speed in km/h between 2 points
 */
function get_speed(loc1, loc2) {
    var distance = get_distance(loc1, loc2);
    var time = get_time(loc1, loc2);
    var speed = distance / time;
    
    return (speed * 3.6);
}

/** 
 * Formats speed given in km/h
 */
function format_speed(speed) {
    return (Math.round(speed * 100) / 100) + " km/h";
}

// CALORIES

/** 
 * Returns MET based of users speed
 * 
 * METS were taken from 
 * https://sites.google.com/site/compendiumofphysicalactivities/home
 */
function get_MET(speed) {
    if ( 1 <= speed && speed < 3) {
        return 2;
    } else if ( 3 <= speed && speed < 4.1) {
        return 2.5;
    } else if ( 4.1 <= speed && speed < 5.1) {
        return 3.2;
    } else if ( 5.2 <= speed && speed < 6.4) {
        return 4.4;
    } else if ( 6.5 <= speed && speed < 7.2) {
        return 5.2;
    } else if ( 7.3 <= speed && speed < 8) {
        return 7;
    } else if ( 8.1 <= speed && speed < 9.6) {
        return 9;
    } else if ( 9.7 <= speed && speed < 10.7) {
        return 10.5;
    } else if ( 10.8 <= speed && speed < 11.2){
        return 11;
    } else if ( 11.3 <= speed && speed < 12.8){
        return 11.6;
    } else if ( 12.9 <= speed && speed < 13.8){
        return 12.3;    
    } else if ( 13.9 <= speed && speed < 14.4){
        return 12.8; 
    } else if ( 14.5 <= speed && speed < 16){
        return 14.5; 
    } else if ( 16.1 <= speed && speed < 17.7){
        return 16; 
    } else if ( 17.8 <= speed && speed < 19.3){
        return 19;
    } else if ( 19.4 <= speed && speed < 20.9){
        return 19.8; 
    } else if ( 21 <= speed && speed < 22.5){
        return 23;  
     } else {
        return 1;
    }
}

/** 
 * Returns calories burned between 2 points
 */
function get_calories(loc1, loc2) {
    var speed = get_speed(loc1, loc2);
    var time = get_time(loc1, loc2);
    var met = get_MET(speed);
    
    return (((met * 3.5 * weight) / 200) * (time/60));
}

/** 
 * Formats calories given in cal
 */
function format_calories(calories) {
    if (calories > 1000) {
        return (Math.round(calories / 10) / 100) + " kcal";
    } else {
        return (Math.round(calories * 100) / 100) + " cal";
    }
}