(function( $ ){

	$(function() {

		$('.rf').each(function(){
			var form = $(this),
				btn = form.find('#btn_submit');
			
			form.find('.rfield').addClass('empty_field');
			
			// Функция проверки полей формы
			function checkInput(){
				form.find('.rfield').each(function(){
					if($(this).val() != ''){
						$(this).removeClass('empty_field');
					} else {
						$(this).addClass('empty_field');
					}
				});
			}
			

			btn.click(function(){
				if($(this).hasClass('disabled')){
					form.submit();
				}
			});
			
		});
		
	});

})( jQuery );