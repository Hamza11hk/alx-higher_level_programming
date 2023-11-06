$(document).ready(function () {
  $('#add_item').click(function () {
    const newItem = $('<li>').text('Item');
    $('.my_list').append(newItem);
  });

  $('#remove_item').click(function () {
    $('.my_list li:last').remove();
  });
  $('#clear_list').click(function () {
    $('UL.my_list').empty();
  });
});
