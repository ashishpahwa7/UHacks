
base_url = 'http://192.168.43.3:8000';

$(document).ready(function(){

			var date = $('#time_ser').find(':selected').text();
	
			$('#myChart2Trigger').html('');
	
			$.ajax({
				type: 'POST',
				url: base_url+'/api/v1/time_series_plot',
				//crossDomain: true,
				data: {
					'from_date': '2017-10-14' ,
					'to_date': '2017-10-15' ,
					'disease_name': date ,

				},
				dataType: 'json',
				success: function (data) {
					x_Val2 = data.X;
					y_Val2 = data.Y;
				setTimeout(function(){
					trigger_val2(x_Val2, y_Val2)
				}, 500);
	
				function trigger_val2(xv, yv) {
					$('#myChart2Trigger').html('<canvas id="myChart" style="width: 100%;height: 500px;"></canvas>');
					setTimeout(function(){
						product_val(xv, yv)
					}, 500);
				}
				}
			});
	
		/* api to get time series graph data (x, y) */
		$('#product').change(function(){
			var item = $('#product').find(':selected').text();
			
			$('xt').html('');
			$.ajax({
				type: 'POST',
				url: base_url+'/api/v1/time_series_plot',
				//crossDomain: true,
				data: {
					'item': item
				},
				dataType: 'json',
				success: function (data) {
					x_Val = data.X;
					y_Val = data.Y;
	
					setTimeout(function(){
						trigger_val(x_Val, y_Val)
					}, 500);
	
					function trigger_val(x, y) {
						$('xt').html('<canvas id="myChart" style="width: 100%;height: 500px;"></canvas>');
						setTimeout(function(){
							product_val(x, y)
						}, 500);
					}
				}
			});
		});
		/* api to get time series graph data (x, y) ends */


	
		/* api to get todays market graph data (x, y) */
		$('#time_ser').change(function(){
			var date = $('#time_ser').find(':selected').text();
			console.log(date);
			$('#myChart2Trigger').html('');
	
			$.ajax({
				type: 'POST',
				url: base_url+'/api/v1/time_series_plot',
				//crossDomain: true,
				data: {
					'from_date': '2017-10-14' ,
					'to_date': '2017-10-15' ,
					'disease_name': date ,

				},
				dataType: 'json',
				success: function (data) {
					console.log(data);
					x_Val2 = data.X;
					y_Val2 = data.Y;

				setTimeout(function(){
					trigger_val2(x_Val2, y_Val2)
				}, 500);
	
				function trigger_val2(xv, yv) {
					$('xt').html('<canvas id="myChart" style="width: 100%;height: 500px;"></canvas>');
					setTimeout(function(){
						product_val(xv, yv)
					}, 500);
				}
				}
			});
		});
		/* api to get time series graph data (x, y) ends*/
	});
	
	xVal = [];
	yVal = [];
	product_val(xVal, yVal); //call graph for first use
	
	/* chart.js graph for time series */
	function product_val(x, y) {
		var ctx = document.getElementById("myChart");
	
		var myBarChart = new Chart(ctx, {
			type: 'line',
			data: {
			labels: x,
			datasets: [
				{
					label: "No . of disease registered",
					backgroundColor: 'rgba(11, 144, 131, 0.8)',
					borderColor: 'rgba(11, 144, 131, 1)',
					hoverBackgroundColor: 'rgba(11, 144, 131, 1)',
					barThickness: "40px",
					borderWidth: 1,
					data: y,
				}
			],
			},
			options: {
				labels:{fontColor:"black", fontSize: 18},
				responsive: true,
				tooltips: {
				  mode: 'label',
				},
				hover: {
				  mode: 'nearest',
				  intersect: true
				},
				scales: {
				  xAxes: [{
					display: true,
					gridLines: {
					  display: true,
					  color: "rgba(11, 144, 131, 0.1)"
					},
					ticks: { fontColor: 'black' },
					scaleLabel: {
					  display: true,
					  labelString: 'Date',
					  fontColor:"black"
					}
				  }],
				  yAxes: [{
					display: true,
					gridLines: {
					  display: true,
					  color: "rgba(11, 144, 131, 0.1)"
					},
					ticks: { fontColor: 'black' },
					scaleLabel: {
					  display: true,
					  labelString: 'No . of disease registered',
					  fontColor:"black"
					}
				  }]
				}
		}
		});
	}
	/* chart.js graph for time series ends */
