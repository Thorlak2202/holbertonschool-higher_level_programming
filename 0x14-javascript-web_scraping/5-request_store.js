#!/usr/bin/node
const url = process.argv[2];
require('request').get(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const fs = require('fs');
    fs.writeFile(process.argv[3], body, 'utf-8', (err) => {
      if (err) {
        throw (err);
      }
    });
  }
});
