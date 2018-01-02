$(document).ready(function(){
  var ctx = document.getElementById("myChart").getContext('2d');
var myChart = new Chart(ctx, {
    type: 'pie',
    data: {
        labels: ["Mee-eters", "Niet mee-eters"],
        datasets: [{
            label: '# of Votes',
            data: [2,8],
            backgroundColor: [
                'rgba(255, 99, 132,1)',
                'rgba(54, 162, 235,1)',
                'rgba(255, 206, 86,1)',
                'rgba(75, 192, 192,1)',
                'rgba(153, 102, 255,1)',
                'rgba(255, 159, 64,1)'
            ],
            borderColor: [
                'rgba(255,99,132,1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
      responsive:true,
      legend:false,
    }
});
});

// if data[0]==8{
//   print "Hulde"
// }
