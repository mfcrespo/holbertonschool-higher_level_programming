#!/usr/bin/node
// Write a function that returns the reversed version of a list:
// Prototype: exports.esrever = function (list)
// You are not allow to use the built-in method reverse

exports.esrever = function (list) {
  let left = 0;
  let right = list.length - 1;
  while (left <= right) {
    const temp = list[right];
    list[right] = list[left];
    list[left] = temp;
    left++;
    right--;
  }
  return (list);
};
