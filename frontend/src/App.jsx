import { useEffect, useState } from 'react'
import { apiGet } from './api.js'

export default function App() {
  const [health, setHealth] = useState(null)
  const [error, setError] = useState(false)

  useEffect(() => {
    apiGet('/health').then(setHealth).catch(() => setError(true))
  }, [])

  return (
    <main>
      <h1>CS 6440 Practicum Project</h1>
      <p>
        Backend: {error ? '❌ not reachable' : health ? '✅ connected' : 'checking…'}
      </p>
      {health && (
        <p>Synthea data: {health.synthea_data_found ? '✅ found' : '⚠️ not downloaded yet'}</p>
      )}
    </main>
  )
}
