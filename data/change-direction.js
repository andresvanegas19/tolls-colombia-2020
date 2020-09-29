#!/usr/bin/env node
const service = require('./service.json').data.tolls;
const axios = require('axios');
const newDirections = {};

data = service.forEach((data) => {
  newDirections[data._id] = data.direction;

  if (/(^$|^ $|ambos|bidi|^((^|nor )oriente|occidente|sur|norte)$)/gmi.test(data.direction)) {
    newDirections[data._id] = 0;
  } else if (/(norte|sur|occidente|oriente).{0,3}(oriente|occidente|sur|norte).{0,5}(norte|sur|occidente|oriente).{0,3}(oriente|occidente|sur|norte)/gmi.test(data.direction)) {
    newDirections[data._id] = 0;
  } else if (/norte.{0,3}sur($|.)/gmi.test(data.direction)) {
    newDirections[data._id] = 1;
  } else if (/sur.{0,3}norte$/gmi.test(data.direction)) {
    newDirections[data._id] = 2;
  } else if (/occidente.{0,3}oriente$/gmi.test(data.direction)) {
    newDirections[data._id] = 3;
  } else if (/oriente.{0,3}occidente$/gmi.test(data.direction)) {
    newDirections[data._id] = 4;
  }
})



Object.entries(newDirections).forEach(direction =>
  axios.patch(`https://api-tolls.herokuapp.com/tolls/${direction[0]}`,
	{
		direction: direction[1],
	})
  .then((response) => {
    console.log(response.res.complete);
  })
  .catch(err => {throw err})
)
