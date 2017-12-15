// Для отправки вормы использовать jQuery ajax forms (http://jquery.malsup.com/form/)
// Показывает ошибки формы
function show_form_errors(form, error_json)
{
    clear_form_errors(form);
    for (name in error_json) {
        var elem = form.find('input[name=' + name + '], textarea[name=' + name + ']');
        elem.closest('.control-group').addClass('error');
        elem.parent().prepend($('<span class="help-inline">*' + error_json[name] + '</span>'));
    }
}

// Очистка формы от ошибок
function clear_form_errors(form)
{
    form.find("span.help-inline").remove();
    form.find('.control-group').removeClass('error');
}


// AJAX подгрузка модальных формы
($("a[data-toggle=modal]")).click(function() {
    if ($(this).hasClass('js_ajax')) {
        var target, url;
        target = ($(this)).attr('data-target');
        // очищаем контейнер модального окна при закрытии
        $(target).on('hidden', function() {
            $(this).html('');
        });

        url = ($(this)).attr('data-href');
        $('body').activity();

        return $(target).load(url, function() {
            $('body').activity(false);
        });
    }
});