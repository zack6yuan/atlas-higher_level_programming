#!/usr/bin/node
// Updates the text of the <header> element.
// Using the JQuery API (onclick(DIV#update_header)).
$('DIV#update_header').click(function () {
  $('header').text('New Header!!!');
});
