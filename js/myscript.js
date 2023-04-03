
$(document).ready(function(){
    $.ajax({
        type: "GET",
        url: "data.csv",
        dataType: "text",
        success: function(data) {processData(data)}
    });

    function processData(data){
        var lines = data.trim().split('\n');
        var lastLine = lines[lines.length-1].split(',')

        console.log(lastLine)
        
        var time = lastLine[0];
        var soil = lastLine[1];
        var temp = lastLine[2];
        const date = document.lastModified;
       
        document.getElementById('time').innerHTML=time;
        document.getElementById('temp').innerHTML=temp;
        document.getElementById('soil').innerHTML=soil;
        document.getElementById('update').innerHTML=date;
   }  
     
})


function differenceInWeeks(d1, d2) {
    var t2 = d2.getTime();
    var t1 = d1.getTime();

    return parseInt((t2-t1)/(24*3600*1000*7));
  }

{
  "nickname": "weather-test", 
  "model": "grow",
  "uid": "e6614c775b8c4035", 
  "timestamp": "2022-09-04T10:40:24Z", 
  "readings": {
    "temperature": 27.57,   // will change depending on board model
    "humidity": 49.33, 
    "pressure": 996.22, 
    "light": 0.41, 
    "moisture_1": 0.0, 
    "moisture_2": 0.0, 
    "moisture_3": 0.0, 
    "voltage": 4.954
  }
}
