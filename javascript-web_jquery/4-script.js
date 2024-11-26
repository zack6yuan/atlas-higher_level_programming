#!/usr/bin/node
// Toggles the class of the <header> element
// Using the JQuery API (onclick(DIV#toggle_header)).
$('DIV#toggle_header').click(function () {
  $('header').toggleClass('red green');
})
