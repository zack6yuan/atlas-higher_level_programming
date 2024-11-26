#!/usr/bin/node
// Updates the text color of the <header> element to red.
// Using the JQuery API (onclick(DIV#red_header)).
$('DIV#red_header').click(function () {
  $('header').css('color', '#FF0000');
});