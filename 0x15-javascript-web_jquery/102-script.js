$(document).ready(function () {
  $('#btn_translate').on('click', function () {
    var languageCode = $('#language_code').val();

    if (languageCode) {
      // Make a GET request to the API with the language code
      $.get(`https://www.fourtonfish.com/hellosalut/hello/${languageCode}`, function (data) {
        // Display the translation in the #hello div
        $('#hello').text(data.hello);
      }).fail(function () {
        // Handle any errors that may occur during the request
        $('#hello').text('Translation not available for the entered language code.');
      });
    } else {
      // Display a message if the user didn't enter a language code
      $('#hello').text('Please enter a language code.');
    }
  });
});
