#!/usr/bin/node
// Adds the class "red" to the <header> element.
// Using the JQuery API (onclick(DIV#red_header)).
$('DIV#red_header').click(function () {
  $('header').addClass('red');
});