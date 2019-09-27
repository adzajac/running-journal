var NUM_DAYS_DISPLAYED = 60;
var run_data = []
var injury_data = []


for(i=0; i<NUM_DAYS_DISPLAYED; i++) { 
    var date = moment().subtract(i,'d').format("YYYY-MM-DD");
    if (typeof from_db_runs !== 'undefined') {
        index = from_db_runs.date.findIndex(x => x.slice(0,-9) === date);
        if(index>=0) {
            run_data.push({t:date, y:from_db_runs.distance[index]});
        }
        else {
            run_data.push({t:date, y:null});
        }
    }
    if (typeof from_db_injuries !== 'undefined') {
        index = from_db_injuries.date.findIndex(x => x.slice(0,-9) === date);
        if(index>=0) {
            injury_data.push({t:date, y:0});
        }
        else {
            injury_data.push({t:date, y:null});
        }
    }  
}

var ctx = document.getElementById('myChart').getContext('2d');
ctx.canvas.width = 1000;
ctx.canvas.height = 400;

var color = Chart.helpers.color;
var cfg = {
    type: 'bar',
    data: {
        datasets: [{
            label: 'Runs',
            backgroundColor: color(window.chartColors.green).alpha(0.5).rgbString(),
            borderColor: window.chartColors.green,
            data: run_data,
            type: 'bar',
            pointRadius: 0,
            fill: false,
            lineTension: 0,
            borderWidth: 2,
            spanGaps: true
        },
           {
            label: 'Injuries',
            backgroundColor: color(window.chartColors.red).alpha(0.5).rgbString(),
            borderColor: window.chartColors.red,
            data: injury_data,
            type: 'bubble',
            pointRadius: 0,
            radius:10,
            fill: false,
            lineTension: 0,
            borderWidth: 2,
            spanGaps: true
        }      
                  
      ]
    },
    options: {
        legend: {
            display: true
        },
        animation: {
            duration: 0
        },
        scales: {
            xAxes: [{
                type: 'time',
                time:{
                    unit:'day',
                    displayFormats: {
                        day: 'DD MMM'
                    }
                },
                distribution: 'linear',
                ticks: {
                    source: 'data',
                    autoSkip: true
                }
            }],
            yAxes: [{
                scaleLabel: {
                    display: true,
                    labelString: 'Distance [km]'
                },
                ticks: {
                    suggestedMin: 0
                }
            }]
        },
        tooltips: {
            intersect: false,
            mode: 'index',
            callbacks: {
                label: function(tooltipItem, myData) {
                    var label = myData.datasets[tooltipItem.datasetIndex].label || '';
                    if (label) {
                        label += ': ';
                    }
                    label += parseFloat(tooltipItem.value).toFixed(2);
                    return label;
                }
            }
        }
    }
};

var chart = new Chart(ctx, cfg);

