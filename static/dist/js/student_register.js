
$(document).ready(function () {
    var profilePic = document.querySelector('.profile-pic')
	var nextBtn1 = document.querySelector('#next1')
	var nextBtn6 = document.querySelector('#next6')
    
	nextBtn1.addEventListener("click", (e)=>{
		var fullName = $(".full-name").val()
		var email = $(".email").val()
		if (!fullName){
			e.preventDefault();
			Swal.fire({
				title: 'Warning!',
				text: "Full name can't be empty",
				icon: 'warning',
			})
			return false
		}

		if (!email){
			e.preventDefault();
			Swal.fire({
				title: 'Warning!',
				text: "email can't be empty",
				icon: 'warning',
			})
			return false
		}
	})

	nextBtn6.addEventListener("click", (e)=>{
		var profile_pic = $(".profile-pic").val()
		if (!profile_pic){
			e.preventDefault();
			Swal.fire({
				title: 'Warning!',
				text: "upload your profile picture",
				icon: 'warning',
			})
		}
	})
	$('.formResult').on("submit", (e)=>{
		console.log("submit")
		var fullName = $(".full-name").val()
		if (!fullName){
			e.preventDefault();
			Swal.fire({
				title: 'Warning!',
				text: "Full name can't be empty",
				icon: 'warning',
			})
			return false
		}

		if (!profile_pic){
			e.preventDefault();
			Swal.fire({
				title: 'Warning!',
				text: "upload your profile picture",
				icon: 'warning',
			})
			return false
		}
	})

    $(".img").click(function () {
		$(".profile-pic").click();
	});

    profilePic.addEventListener("change", function (){
		let folder = this.files[0];
		if (folder.type == "image/png" | folder.type == "image/jpeg") {
		let fileReader = new FileReader();
		fileReader.onload = ()=>{
		  let fileURL = fileReader.result;
		  pict = document.querySelector(".img")
		  pict.src = fileURL
		};
		fileReader.readAsDataURL(folder);
		}
	})
})