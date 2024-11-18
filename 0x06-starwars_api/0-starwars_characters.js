#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

if (!movieId) {
	console.error('Usage: ./0-starwars_characters.js <Movie ID>');
	process.exit(1);
}

// URL for starwars API
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, (error, response, body) => {
	if (error) {
		console.error('Error:', error);
		return;
	}

	if (response.statusCode !== 200) {
		console.error('Failed to fetch data. Status code', response.statusCode);
		return;
	}

	const filmData = JSON.parse(body);
	const characters = filmData.characters;

	printCharacters(characters, 0);
});

function printCharacters(characters, index) {
	if (index >= characters.length) {
		return;
	}

	request(characters[index], (error, response, body) => {
		if (error) {
			console.error('Error', error);
			return;
		}
		if (response.statusCode === 200) {
			const characterData = JSON.parse(body);
			console.log(characterData.name);
		} else {
			console.error('Failed to fetch character data. Status code:', response.statusCode);
		}

		printCharacters(characters, index + 1);
	});
}
