#!/usr/bin/node
// Fetches and lists the title for all movies.
// Using the JQuery API.
$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  $('UL#list_movies').append(`<li>${data.title}</li>`);
});
