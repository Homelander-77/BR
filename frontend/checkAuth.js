import { apiFetch } from './api.js';

export async function check(){
    try {
	const res = await apiFetch('/check_auth');
	if (res.status === 200) return true;
	if (res.status === 403) return false;
	throw new Error(`Unexpected status: ${res.status}`);
    } catch(e) {
	alert(`${e}`);
	return false;
    }    
}
