

//
//var dateFormat = 'MMMM DD YYYY';
//var date = moment(new Date(), dateFormat).subtract(30, 'd');
//console.log(date.valueOf())
//





var ctx = document.getElementById('myChart').getContext('2d');
ctx.canvas.width = 1000;
ctx.canvas.height = 400;

var color = Chart.helpers.color;
var cfg = {
    type: 'bar',
    data: {
        datasets: [{
            label: 'Distances [m]',
            backgroundColor: color(window.chartColors.green).alpha(0.5).rgbString(),
            borderColor: window.chartColors.green,
            data: data_from_db,
            type: 'bar',
            pointRadius: 0,
            fill: false,
            lineTension: 0,
            borderWidth: 2
        }]
    },
    options: {
        legend: {
            display: false
        },
        scales: {
            xAxes: [{
                type: 'time',
                time:{
                    displayFormats:{
                       'millisecond': 'DD MMM',
                       'second': 'DD MMM',
                       'minute': 'DD MMM',
                       'hour': 'DD MMM',
                       'day': 'DD MMM',
                       'week': 'DD MMM',
                       'month': 'DD MMM',
                       'quarter': 'DD MMM',
                       'year': 'DD MMM'
                    }
                },
                distribution: 'series',
                ticks: {
                    source: 'data',
                    autoSkip: true
                }
            }],
            yAxes: [{
                scaleLabel: {
                    display: true,
                    labelString: 'Distance [m]'
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

