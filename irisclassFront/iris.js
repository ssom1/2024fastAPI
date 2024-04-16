google.charts.load("current", {packages:["corechart"]});
//  google.charts.setOnLoadCallback(drawChart);

function drawChart(p) {

  var data = google.visualization.arrayToDataTable([
    ['iris', 'species'],
    ['setosa',     p[0]],
    ['versicolor',    p[1]],
    ['virginica',  p[2]],

  ]);

  var options = {
    title: '붓꽃 종류 확률',
    is3D: true,
  };

  var chart = new google.visualization.PieChart(document.getElementById('piechart'));
  chart.draw(data, options);
}

function Send(){

    sl = document.getElementById("sl")
    sw = document.getElementById("sw")
    pl = document.getElementById("pl")
    pw = document.getElementById("pw")
    
      var data = {
        'sepal_length': sl.value,
        'sepal_width': sw.value,
        'petal_length': pl.value,
        'petal_width': pw.value,
      }  
    
      $.ajax({
      
        type: "POST",
        url: 'http://localhost:8000/predict',
        headers:{
            "Accept" : "application/json",
            "Content-Type": "application/json", 
            },
        data: JSON.stringify(data),
    
      }).done(function(response) {
    
            txtOut.value = response.predict + "  " + response.probability
    

            console.log(response)

            rp = response.probability

            p = [rp[0][0], rp[0][1], rp[0][2]]
           
            google.charts.setOnLoadCallback(drawChart(p));      
    
      }).fail(function(error) {
        alert("!/js/user.js에서 에러발생: " + error.statusText);
        console.log(error)
      }).always(function(r){
        console.log("always" + r)
      });
    
    
    }