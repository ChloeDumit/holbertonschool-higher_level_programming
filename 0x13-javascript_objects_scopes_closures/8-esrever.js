#!/usr/bin/node
exports.esrever = function (list) {
    var i = 0;
    while (i < list.length - 1) {
    list.splice(i, 0, list.pop());
    i++;
  }
  return list;
}