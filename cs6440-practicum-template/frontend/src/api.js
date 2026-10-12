// All calls to the Python backend go through here. Paths are relative, so the same code
// works with the Vite dev proxy locally and with vercel.json routing in production.

async function get(path, params = {}) {
  const query = new URLSearchParams(params).toString()
  const res = await fetch(`/api${path}${query ? `?${query}` : ''}`)
  if (!res.ok) throw new Error(`${res.status} ${res.statusText}`)
  return res.json()
}

export const api = {
  health: () => get('/health'),
  searchPatients: (q) => get('/patients', { q }),
  getPatient: (id) => get(`/patients/${encodeURIComponent(id)}`),
}
