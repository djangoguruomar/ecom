var BtnUpdate = document.getElementsByClassName("update-cart")

for (i=0; i<BtnUpdate.length; i++)
{	BtnUpdate[i].addEventListener('click', function()

{
    var productId=this.dataset.product
    var action=this.dataset.action
    console.log('productId:', productId, 'Action:', action)
		console.log('USER:', user)

	update_cart(productId, action)})}
	function update_cart(productId, action){
		console.log('User is authenticated, sending data...')
		$.ajax({
            type: 'POST',
            url: '/update_cart/',
			headers:{
						'Content-Type':'application/json',
						'X-CSRFToken':csrftoken,
					}, 
            data: JSON.stringify({'productId':productId, 'action':action}),

			success: function(data) {
			
				$( "#up-cart" ).html(data)
				
			},

		})}





			// var url = '/update_cart/'
	
			// fetch(url, {
			// 	method:'POST',
			// 	headers:{
			// 		'Content-Type':'application/json',
			// 		'X-CSRFToken':csrftoken,
			// 	}, 
			// 	body:JSON.stringify({'productId':productId, 'action':action})
			// })
			// .then((response) => {
			//    return response.json();
			// })
			// .then((data) => {
			// 	location.reload()
			// });}