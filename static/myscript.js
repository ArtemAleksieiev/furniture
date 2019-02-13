		$(document).ready(function(){
		$('.lightbox1').click(function(){
			$('.backdrop, .box').animate({'opacity':'.50'}, 300,'linear');
			$('.box').animate({'opacity':'1.00'}, 300,'linear');
			$(".backdrop, .box").css('display', 'block');
		});
		$('.close').click(function(){
			close_box();
		});
		$('.backdrop').click(function(){
			close_box();
		});
	});
		$('.submit').click(function(){	
			$(".error-text").css('display', 'block');
			});
		function close_box()
		{
$('.backdrop, .box').animate({'opacity':'0'}, 300,'linear', function(){
				$(".backdrop, .box").css('display', 'none');

			})};

	