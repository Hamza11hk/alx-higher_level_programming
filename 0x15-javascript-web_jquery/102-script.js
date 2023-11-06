dy(() => {
  $('#btn_translate').click(() => {
    const cc = $('#language_code').val();
    $.get('https://hellosalut.stefanbohacek.dev/?lang=' + cc, (data) => {
      $('#hello').html(data.hello);
    });
  });
});
