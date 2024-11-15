function enter(){
	localStorage.clear();
	let username = document.getElementById("user").value;
	localStorage.setItem('setUser', username);
	let password = document.getElementById("pass").value;
	localStorage.setItem('setPass', password);
}