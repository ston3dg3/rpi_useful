var Blynk = require('blynk-library');
var sensorLib = require('node-dht-sensor');
var AUTH = 'qRSoA0PM0N1Nw_Fn3gtCgCV09fHemT4U';
var blynk = new Blynk.Blynk(AUTH, options = {
	connector : new Blynk.TcpClient()
});

var updateTime = 2000;
var sensorType = 11; // 11 for DHT11, 22 for DHT22 and AM2302
// var v4 = new blynk.VirtualPin(4);
var sensorPin = 17;

if (!sensorLib.initialize(sensorType, sensorPin)) {
	console.warn('Failed to initialize sensor!');
	process.exit(1);
}

// Automatically update sensor value every {updateTime} seconds
setInterval(function() {
	var readout = sensorLib.read();
	blynk.virtualWrite(3, readout.temperature.toFixed(1));
	blynk.virtualWrite(4, readout.humidity.toFixed(1));

	console.log('Temperature:', readout.temperature.toFixed(1) + 'C');
    	console.log('Humidity:   ', readout.humidity.toFixed(1)    + '%');
}, updateTime);
