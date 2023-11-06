$(document).ready(() => {
  function translateFn () {
    const url = 'https://hellosalut.stefanbohacek.dev/?lang=';
    const cc = $('#language_code').val();
    $.get(url + cc, function (data) {
      $('#hello').html(data.hello);
    });
  }
  $('#btn_translate').click(() => { translateFn(); });
  $('#language_code').keypress((event) => {
    if (event.which === 13) { translateFn(); }
  });
  $('INPUT#language_code').focus(() => { translateFn(); });
});
