#!/usr/bin/node
// Reading file

const args = process.argv.slice(2);
const fs = require('fs');

fs.readFile(args[0], 'utf-8', function (err, data) {
  if (err) throw err;
  console.log(data);
});
