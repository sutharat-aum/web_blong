      google.charts.load("current", {packages:["corechart"]});
      google.charts.setOnLoadCallback(drawChart1);
      google.charts.setOnLoadCallback(drawChart2);
      google.charts.setOnLoadCallback(drawChart3);


function drawChart1() {
        var data1 = google.visualization.arrayToDataTable([
          ['Emotions', 'Results'],
          ['Happiness',     25],
          ['Sadness',      5],

        ]);

        var options1 = {
          title: 'My Daily Activities1',
          pieHole: 0.5,
        };

        var chart = new google.visualization.PieChart(document.getElementById('donutchart1'));
        chart.draw(data1, options1);
      }
function drawChart2() {
        var data2 = google.visualization.arrayToDataTable([
          ['Emotions', 'Results'],
          ['Love',  2],
          ['Hate', 2]
        ]);

        var options2 = {
          title: 'My Daily Activities2',
          pieHole: 0.5,
        };

        var chart = new google.visualization.PieChart(document.getElementById('donutchart2'));
        chart.draw(data2, options2);
      }
      function drawChart3() {
        var data3 = google.visualization.arrayToDataTable([
          ['Emotions', 'Results'],
          ['Fun',    7],
          ['Worry',    7]
        ]);

        var options3 = {
          title: 'My Daily Activities3',
          pieHole: 0.5,
        };

        var chart = new google.visualization.PieChart(document.getElementById('donutchart3'));
        chart.draw(data3, options3);
      }



