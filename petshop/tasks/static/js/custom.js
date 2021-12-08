$(document).ready(function(){
	// Add to cart
	$(document).on('click',".add-to-cart",function(){
		var _vm=$(this);
		var _index=_vm.attr('data-index');
		var _qty=$(".product-qty-"+_index).val();
		var _productId=$(".product-id-"+_index).val();
		var _productTitle=$(".product-title-"+_index).val();
		var _productPrice=$(".product-price-"+_index).text();
		// Ajax
		$.ajax({
			url:'/add-to-cart',
			data:{
				'id':_productId,
				'qty':_qty,
				'title':_productTitle,
				'price':_productPrice
			},
			dataType:'json',
			beforeSend:function(){
				_vm.attr('disabled',true);
			},
			success:function(res){
				$(".cart-list").text(res.totalitems);
				_vm.attr('disabled',false);
			}
		});
		// End
	});
	// End

	// Delete item from cart
	$(document).on('click','.delete-item',function(){
		var _pId=$(this).attr('data-item');
		var _vm=$(this);
		// Ajax
		$.ajax({
			url:'/delete-from-cart',
			data:{
				'id':_pId,
			},
			dataType:'json',
			beforeSend:function(){
				_vm.attr('disabled',true);
			},
			success:function(res){
				$(".cart-list").text(res.totalitems);
				_vm.attr('disabled',false);
				$("#cartList").html(res.data);
			}
		});
		// End
	});

	// Update item from cart
	$(document).on('click','.update-item',function(){
		var _pId=$(this).attr('data-item');
		var _pQty=$(".product-qty-"+_pId).val();
		var _vm=$(this);
		// Ajax
		$.ajax({
			url:'/update-cart',
			data:{
				'id':_pId,
				'qty':_pQty
			},
			dataType:'json',
			beforeSend:function(){
				_vm.attr('disabled',true);
			},
			success:function(res){
				// $(".cart-list").text(res.totalitems);
				_vm.attr('disabled',false);
				$("#cartList").html(res.data);
			}
		});
		// End
	});

	// Add wishlist
	$(document).on('click',".add-wishlist",function(){
		var _pid=$(this).attr('data-product');
		var _vm=$(this);
		// Ajax
		$.ajax({
			url:"/add-wishlist",
			data:{
				product:_pid
			},
			dataType:'json',
			success:function(res){
				if(res.bool==true){
					_vm.addClass('disabled').removeClass('add-wishlist');
				}
			}
		});
		// EndAjax
	});
	// End

	// Activate selected address
	$(document).on('click','.activate-address',function(){
		var _aId=$(this).attr('data-address');
		var _vm=$(this);
		// Ajax
		$.ajax({
			url:'/activate-address',
			data:{
				'id':_aId,
			},
			dataType:'json',
			success:function(res){
				if(res.bool==true){
					$(".address").removeClass('shadow border-secondary');
					$(".address"+_aId).addClass('shadow border-secondary');

					$(".check").hide();
					$(".actbtn").show();
					
					$(".check"+_aId).show();
					$(".btn"+_aId).hide();
				}
			}
		});
		// End
	});

});
// End Document.Ready

// Product Review Save
$("#addForm").submit(function(e){
	$.ajax({
		data:$(this).serialize(),
		method:$(this).attr('method'),
		url:$(this).attr('action'),
		dataType:'json',
		success:function(res){
			if(res.bool==true){
				$(".ajaxRes").html('Data has been added.');
				$("#reset").trigger('click');
				// Hide Button
				$(".reviewBtn").hide();
				// End

				// create data for review
				var _html='<blockquote class="blockquote text-right">';
				_html+='<small>'+res.data.review_text+'</small>';
				_html+='<footer class="blockquote-footer">'+res.data.user;
				_html+='<cite title="Source Title">';
				for(var i=1; i<=res.data.review_rating; i++){
					_html+='<i class="fa fa-star text-warning"></i>';
				}
				_html+='</cite>';
				_html+='</footer>';
				_html+='</blockquote>';
				_html+='</hr>';

				$(".no-data").hide();

				// Prepend Data
				$(".review-list").prepend(_html);

				// Hide Modal
				$("#productReview").modal('hide');

				// AVg Rating
				$(".avg-rating").text(res.avg_reviews.avg_rating.toFixed(1))
			}
		}
	});
	e.preventDefault();
});
// End