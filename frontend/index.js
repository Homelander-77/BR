window.addEventListener('load', check);

function check(){
    const hello = document.getElementById('hello');
    const forbidden = document.getElementById('403');
    fetch('/api/cookie', {
	method: 'GET',
	credentials: 'include',
	headers: {
	    'Content-Type': 'application/json'
	}
    })
    .then(res => {
	if (res.status === 200){
	    hello.style.display = 'block';
	} else if (res.status === 403){
	    forbidden.style.display = 'block';
	} else {
	    alert(res.status);
	}
    })
    .catch(e =>{
	alert(e);
    });
}
