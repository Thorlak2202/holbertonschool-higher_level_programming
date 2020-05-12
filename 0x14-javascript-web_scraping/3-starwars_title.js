#!/usr/bin/node
const url = 'https://swapi-api.hbtn.io/api/films/';
require('request').get(url + process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
