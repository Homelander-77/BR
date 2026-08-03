export async function apiFetch(path, {method = 'GET', body} = {}) {
    return fetch(`/api${path}`, {
	method,
	credentials: 'include',
	headers: {'Content-type': 'application/json'},
	...(body !== undefined ? {body: JSON.stringify(body)} : {})
    });
}
