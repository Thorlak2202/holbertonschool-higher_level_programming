#!/usr/bin/node
const url = process.argv[2];
require('request').get(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const todos = JSON.parse(body);
    const complete = {};
    for (const i in todos) {
      if (todos[i].completed) {
        if (!(todos[i].userId in complete)) {
          complete[todos[i].userId] = 0;
        }
        complete[todos[i].userId] += 1;
      }
    }
    console.log(complete);
  }
});
