import { useEffect, useState } from 'react'
import { api } from '../api.js'

export default function PatientList({ selectedId, onSelect }) {
  const [query, setQuery] = useState('')
  const [patients, setPatients] = useState([])
  const [error, setError] = useState(null)

  useEffect(() => {
    const timer = setTimeout(() => {
      api.searchPatients(query).then(setPatients).catch((e) => setError(e.message))
    }, 250) // small debounce while typing
    return () => clearTimeout(timer)
  }, [query])

  return (
    <div className="card">
      <input
        type="search"
        placeholder="Search patients…"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
      />
      {error && <p className="error">{error}</p>}
      <ul className="patient-list">
        {patients.map((p) => (
          <li key={p.id}>
            <button
              className={p.id === selectedId ? 'selected' : ''}
              onClick={() => onSelect(p.id)}
            >
              <strong>{p.name}</strong>
              <span>
                {p.gender} · {p.age ?? '?'} yrs
              </span>
            </button>
          </li>
        ))}
      </ul>
    </div>
  )
}
