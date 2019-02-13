jQuery(document).ready(function() {
    
    $('#countdown_dashboard').countDown({
					targetDate: {
						'day': 		29,
						'month': 	03,
						'year': 	2014,
						'hour': 	23,
						'min': 		59,
						'sec': 		59,	
						'utc':      true,
						},
					omitWeeks: true					
				});               
                             
});