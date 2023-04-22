
$(document).ready(function () {
    var profilePic = document.querySelector('.profile-pic')
	var switchs = document.querySelector('#agree')
	var nextBtn1 = document.querySelector('#next1')
	var nextBtn4 = document.querySelector('#next4')
	var nextBtn5 = document.querySelector('#next5')
	var nextBtn6 = document.querySelector('#next6')
    
	nextBtn1.addEventListener("click", (e)=>{
		var fullName = $(".full-name").val()
		var username = $(".username").val()
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
		if (!username){
			e.preventDefault();
			Swal.fire({
				title: 'Warning!',
				text: "user name can't be empty",
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
	nextBtn4.addEventListener("click", (e)=>{
		var local_government = $("#local_government").val()
		var district = $("#district").val()
		var school = $("#school").val()
		var level = $("#level").val()
		if (!local_government){
			e.preventDefault();
			Swal.fire({
				title: 'Warning!',
				text: "local government can't be left empty",
				icon: 'warning',
			})
			return false
		}
		if (!district){
			e.preventDefault();
			Swal.fire({
				title: 'Warning!',
				text: "district can't be left empty",
				icon: 'warning',
			})
			return false
		}
		if (!school){
			e.preventDefault();
			Swal.fire({
				title: 'Warning!',
				text: "school can't be left empty",
				icon: 'warning',
			})
			return false
		}
		if (!level){
			e.preventDefault();
			Swal.fire({
				title: 'Warning!',
				text: "school can't be left empty",
				icon: 'warning',
			})
			return false
		}
	})
	nextBtn5.addEventListener("click", (e)=>{
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
		if (!school){
			e.preventDefault();
			Swal.fire({
				title: 'Warning!',
				text: "school can't be left empty",
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
		if (!$('#location').is(':checked')) {
			e.preventDefault();
			Swal.fire({
				title: 'Warning!',
				text: "you must select everything",
				icon: 'warning',
			})
			return false
		}
		if (!$('#camera').is(':checked')) {
			e.preventDefault();
			Swal.fire({
				title: 'Warning!',
				text: "you must select everything",
				icon: 'warning',
			})
			return false
		}
		if (!$('#terms').is(':checked')) {
			e.preventDefault();
			Swal.fire({
				title: 'Warning!',
				text: "you must select everything",
				icon: 'warning',
			})
			return false
		}
	})

	$('#location').change(()=>{
		if (!$(this).prop('checked')) {
			if (navigator.geolocation) {
				navigator.geolocation.getCurrentPosition(function(position) {
				// Success callback
				var latitude = position.coords.latitude;
				var longitude = position.coords.longitude;
				alertify.set("notifier", "position", "top-right");
				alertify.success("location access sucessfully")
				$("#latitude").val(latitude)
				$("#longitude").val(longitude)
			}, function(error) {
				// Error callback
				if (error.code == error.PERMISSION_DENIED) {
					Swal.fire({
						title: 'Denied!',
						text: "you can't continue until you grant access to your location!",
						icon: 'error',
					}).then(function() {
						// Uncheck the checkbox
						$('#location').prop('checked', false);
					});
				}
			});
			} else {
				Swal.fire({
					title: 'Warning!',
					text: 'Geolocation is not supported by this browser!',
					icon: 'warning',
				})
			}		  
		}
	})

    $(function(){
        $.ajax({
            method: "GET",
            url: "/get_local_government/",
            success: function (response) {
                // document.querySelector(".lang_level").innerHTML = ""
				document.querySelector("#local_government").innerHTML = `<option value="">SELECT A LOCAL GOVERNMENT</option>`
                var local_government = document.querySelector("#local_government")
                response.map(data => {
                    let value = `<option>${data.name}</option>`;
                    $("#local_government").append(value)
                })
                // document.querySelector(".lang_level").innerHTML = result
            },
            error: function (e) {
                console.log(e)
                return false;
            }
        })
    })

    $("#local_government").on("change", (e) => {
		var local_government = $("#local_government").val().trim();
		if (local_government) {
			$.ajax({
			method: "GET",
			url: "/get_district/",
			data: {"local_government": local_government},
			success: function (response) {
				document.querySelector("#district").innerHTML = `<option value="">SELECT A DISTRICT</option>`
				var doc = document.querySelector("#district")
				response.map(data => {
					let value = `<option>${data.name}</option>`;
					$("#district").append(value)
				})
				// document.querySelector(".lang_level").innerHTML = result
			},
			error: function (e) {
				console.log(e)
				return false;
			}
		})
		}
	})

    $("#district").on("change", (e) => {
		var local_government = $("#local_government").val().trim();
		var district = $("#district").val().trim();
		if (local_government && district) {
			$.ajax({
			method: "GET",
			url: "/get_school/",
			data: {
				"local_government": local_government,
				"district": district,
			},
			success: function (response) {
				document.querySelector("#school").innerHTML = `<option value="">SELECT A SCHOOL</option>`
				var school = document.querySelector("#school")
				response.map(data => {
					let value = `<option>${data.name}</option>`;
					$("#school").append(value)
				})
				// document.querySelector(".lang_level").innerHTML = result
			},
			error: function (e) {
				console.log(e)
				return false;
			}
		})
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