(function(){
	$(window).scroll(function(){
		if( $(this).scrollTop() > 50 ){
			$(".top-bar").addClass("fixed");
		} else {
			$(".fixed").removeClass("fixed");
		}
	});
})();


