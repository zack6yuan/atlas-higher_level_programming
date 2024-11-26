#!/usr/bin/node
// Fetches and displays the value from that fetch.
// In the HTML tag (DIV#hello).
// Using the JQuery API.
$.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (data) {
  $('DIV#hello').text(data.hello);
})