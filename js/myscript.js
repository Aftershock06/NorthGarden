
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