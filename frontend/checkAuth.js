export async function check(){
    return fetch('/api/check_auth', {
	method: 'GET',
	credentials: 'include',
	headers: { 'Content-Type': 'application/json' }
    })
    .then(res => {
	if (res.status === 200) return true;
	if (res.status === 403) return false;
	throw new Error(`Unexpected status: ${res.status}`);
    })
    .catch(e =>{
	alert(`${e}`);
	return false;
    });
}
