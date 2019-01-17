var request = require('request');
 
var Service, Characteristic;

module.exports = function (homebridge) {
  Service = homebridge.hap.Service;
  Characteristic = homebridge.hap.Characteristic;
  homebridge.registerAccessory("homebridge-tristan-lights-plugin", "Tristan Lights", mySwitch);
};

function mySwitch(log, config) {
  this.log = log;
  this.getUrl = config['getUrl'];
  this.postUrl = config['postUrl'];
  this.displayName = config['name'];
}
  
mySwitch.prototype = {
  getServices: function () {
    let informationService = new Service.AccessoryInformation();
    informationService
      .setCharacteristic(Characteristic.Manufacturer, "Tristan Inc")
      .setCharacteristic(Characteristic.Model, "Model 0")
      .setCharacteristic(Characteristic.SerialNumber, "554-54-58");
    let switchService = new Service.Switch("Lights");
    switchService
      .getCharacteristic(Characteristic.On)
        .on('get', this.getSwitchOnCharacteristic.bind(this))
        .on('set', this.setSwitchOnCharacteristic.bind(this));
 
    this.informationService = informationService;
    this.switchService = switchService;
    return [informationService, switchService];
  },
  getSwitchOnCharacteristic: function (next) {
    request({
        url: this.getUrl,
        method: 'GET'
    }, 
    function (error, response, body) {
      if (error) {
        this.log('STATUS: ' + response.statusCode);
        this.log(error.message);
        return next(error);
      }
      return next(null, body.currentState);
    });
  },
  setSwitchOnCharacteristic: function (on, next) {
    request({
      url: this.postUrl,
      method: 'POST',
      body: {'targetState': on},
      headers: {'Content-type': 'application/json'}
    },
    function (error, response) {
      if (error) {
        this.log('STATUS: ' + response.statusCode);
        this.log(error.message);
        return next(error);
      }
      return next();
    });
  }
};
