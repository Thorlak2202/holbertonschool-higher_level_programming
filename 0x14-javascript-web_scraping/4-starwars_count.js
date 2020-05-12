#!/usr/bin/node
const url = process.argv[2];
require('request').get(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const info = JSON.parse(body).results;
    let appearances = 0;
    for (const i in info) {
      const chars = info[i].characters;
      for (const ppl in chars) {
        if (chars[ppl].includes('18')) {
          appearances += 1;
        }
      }
    }
    console.log(appearances);
  }
});
