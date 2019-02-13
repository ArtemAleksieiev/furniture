		$(document).ready(function(){
		$('.gal_img').click(function(){
			$('.overlay, .galery').animate({'opacity':'.60'}, 300,'linear');
			$('.galery').animate({'opacity':'1.00'}, 300,'linear');
			$(".overlay, .galery").css('display', 'block');
		});
		$('.closePopap').click(function(){
			close_box();
		});
		$('.overlay').click(function(){
			close_box();
		});
	});
		$('.submit').click(function(){	
			$(".error-text").css('display', 'block');
			});
		function close_box()
		{
$('.overlay, .galery').animate({'opacity':'0'}, 300,'linear', function(){
				$(".overlay, .galery").css('display', 'none');

			})};

	