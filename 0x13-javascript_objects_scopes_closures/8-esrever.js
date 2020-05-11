#!/usr/bin/node
exports.esrever = function (list) {
  var rList = [];
  var i = 0;
  for (i; i in list; ++i) {
    rList.unshift(list[i]);
  }
  return (rList);
};
