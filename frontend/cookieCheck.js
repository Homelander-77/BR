export function check(){
    fetch('/api/cookie', {
	method: 'GET',
	credentials: 'include',
	headers: { 'Content-Type': 'application/json' }
    })
    .then(res => {
	if (res.status === 200){
	    return true;
	} else if (res.status === 403){
	    return false;
	} else {
	    alert(res.status);
	}
    })
    .catch(e =>{
	alert(e);
    });
}
