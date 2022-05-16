#!/usr/bin/node
// prints all characters of a Star Wars movie
const film_id = process.argv[2];
const film_url = 'https://swapi-api.hbtn.io/api/films/' + film_id;
const request = require('request');

function get_char(charUrl) {
    return new Promise(function(resolve, reject) {
	request(charUrl, function(err1, response1, body1) {
	    if(err1) {
		reject(err1);
	    } else {
		resolve(JSON.parse(body1).name);
	    }
	});
    });
}

async function charlist(chars) {
    for(const charUrl of chars) {
	const character = await get_char(charUrl);
	console.log(character);
    }
}

request(film_url, function my_chars(err, response, body) {
    if(err) {
	throw err;
    } else {
	const chars = JSON.parse(body).characters;
	charlist(chars);
    }
});
