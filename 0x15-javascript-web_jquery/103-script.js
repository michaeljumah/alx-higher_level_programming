$(document).ready(function () {
  // Function to fetch and display the translation
  function fetchTranslation() {
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
  }

  // Event handler for the translate button click
  $('#btn_translate').on('click', function () {
    fetchTranslation();
  });

  // Event handler for pressing ENTER in the language code input
  $('#language_code').on('keypress', function (e) {
    if (e.which === 13) {
      // Check if the pressed key is ENTER (key code 13)
      fetchTranslation();
    }
  });
});
