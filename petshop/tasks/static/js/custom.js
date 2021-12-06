$(document).ready(function(){
	$("#loadMore").on('click',function(){
		var _currentProducts=$(".product-box").length;
		var _limit=$(this).attr('data-limit');
		var _total=$(this).attr('data-total');

		// Run Ajax
		$.ajax({
			url:'/load-more-data',
			data:{
				limit:_limit,
				offset:_currentProducts,
			}
			dataType:'json',
			beforeSend:function(){
				$("#loadMore").attr('disabled', true);
				$(".icon-line2-refresh").addClass('fa-spin');
			},
			success:function(res){
				$("#loadMore").attr('disabled', false);
				$(".icon-line2-refresh").removeClass('fa-spin');
			}

		});
		// End

		
	});

});	