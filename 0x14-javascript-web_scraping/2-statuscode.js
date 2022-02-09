#!/usr/bin/node

const request = require('request');
const args = process.argv.slice(2);

request(args[0], function (err, response) {
  if (err) {
    console.log(err);
  }
  console.log('code:', response.statusCode);
});
