// Call the backend: apiGet('/health') -> GET /api/health
export async function apiGet(path) {
  const res = await fetch(`/api${path}`)
  if (!res.ok) throw new Error(`${res.status} ${res.statusText}`)
  return res.json()
}
