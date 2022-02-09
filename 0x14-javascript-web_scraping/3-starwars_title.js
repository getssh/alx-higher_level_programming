#!/usr/bin/node
const request = require('request');
const args = process.argv.slice(2);
const url = 'https://swapi-api.hbtn.io/api/films/';
const movieId = args[0];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).results[movieId - 1].title);
  }
});
