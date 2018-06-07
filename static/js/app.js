// /* data route */
var url = "/population_urban";

function buildPlot() {
    Plotly.d3.json(url, function(error, response) {

        var trace1 = {
            type: "scatter",
            mode: "markers",
            name: response.map(data => data.region),
            x: response.map(data => data.Yr_2017),
            y: response.map(data => data.pop_density),
            line: {
                color: "#17BECF"
            }
        };
        console.log(data);
        var data = [trace1];
        console.log(data);
        var layout = {
            title: "Urban Population",
            showlegend: false,
            height: 500,
            width: 500
          
            // // xaxis: {
            // //     type: "date"
            // },
            // yaxis: {
            //     autorange: true,
            //     type: "linear"    
        };
        Plotly.newPlot("urbanPop", data, layout);
    });
}

buildPlot();
