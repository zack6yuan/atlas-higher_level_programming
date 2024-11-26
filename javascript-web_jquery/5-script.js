#!/usr/bin/node
// Adds a <li> element to a list
// Using the JQuery API (onclick(DIV#add_item)).
$('DIV#add_item').click(function () {
  $('UL.my_list').append('<li>Item</li>');
});
