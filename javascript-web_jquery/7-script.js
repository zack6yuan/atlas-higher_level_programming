#!/usr/bin/node
// Fetches the character "name" from URL
// Using the JQuery API.
$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function (data) {
  $('DIV#character').text(data.name);
});
