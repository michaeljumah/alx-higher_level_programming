$(document).ready(function () {
  // Event handler for adding a new item
  $('#add_item').on('click', function () {
    var newItem = $('<li>Item</li>');
    $('.my_list').append(newItem);
  });

  // Event handler for removing the last item
  $('#remove_item').on('click', function () {
    $('.my_list li:last-child').remove();
  });

  // Event handler for clearing the entire list
  $('#clear_list').on('click', function () {
    $('.my_list').empty();
  });
});
