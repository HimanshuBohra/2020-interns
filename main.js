function chart(dates,eur_exchange){
    const ctx = document.getElementById('chart');
    const myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: dates,
            datasets: [{
                label: '# of Votes',
                data: eur_exchange,
                borderWidth: 1
            }]
        },
    });
}
var currency;
functiongetCurrency(){
    currency = document.getElementById('currency').value;
}
function main(data){
    var d = data.rates;
    var dates=[];
    for(x in d){
        dates.push(x);
    }
        var specified_date = [];
        for (var i = 0; i < dates.length; i++){
            var arr = dates[i].split("-");
            var month_index =  parseInt(arr[1],10);
            if(month_index == 1){
                specified_date.push(dates[i]);
            }
        }
        specified_date.sort();
        var eur_exchange = []
        for (var i = 0; i < specified_date.length; i++){
            eur_exchange.push(data.rates[dates[i]][currency]);
        }  
        chart(dates,eur_exchange);
    }

    
window.onload = function() {
    function readTextFile(file, callback) {
    var rawFile = new XMLHttpRequest();
    rawFile.overrideMimeType("application/json");
    rawFile.open("GET", file, true);
    rawFile.onreadystatechange = function() {
        if (rawFile.readyState === 4 && rawFile.status == "200") {
            callback(rawFile.responseText);
        }
    }
    rawFile.send(null);
    }
    var data = [];
    readTextFile("./data.json", function(text){
      data = JSON.parse(text);
      alert(data)
    });
    
    main(data);
}