#!/usr/bin/node

const request = require('request');
const starWarsUri = 'https://swapi-api.hbtn.io/api/films/'.concat(process.argv[2]);

request(starWarsUri, function (_error, _res, body) {
  const characters = JSON.parse(body).characters;

  for (let i = 0; i < characters.length; ++i) {
    request(characters[i], function (_cError, _cRes, cBody) {
      console.log(JSON.parse(cBody).name);
    });
  }
});

