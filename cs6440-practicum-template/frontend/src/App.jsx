import { useEffect, useState } from 'react'
import { api } from './api.js'
import PatientList from './components/PatientList.jsx'
import PatientDetail from './components/PatientDetail.jsx'

export default function App() {
  const [health, setHealth] = useState(null)
  const [selectedId, setSelectedId] = useState(null)

  useEffect(() => {
    api.health().then(setHealth).catch(() => setHealth({ status: 'down' }))
  }, [])

  return (
    <div className="app">
      <header className="topbar">
        <h1>Practicum App</h1>
        {/* TODO(team): rename the app and describe what it does */}
        <span className={`status ${health?.status === 'ok' ? 'ok' : 'down'}`}>
          {health?.status === 'ok'
            ? `API connected · ${health.patients} patients (${health.source} data)`
            : health
              ? 'API not reachable'
              : 'Connecting…'}
        </span>
      </header>

      <main className="layout">
        <aside>
          <PatientList selectedId={selectedId} onSelect={setSelectedId} />
        </aside>
        <section>
          {selectedId ? (
            <PatientDetail patientId={selectedId} />
          ) : (
            <p className="empty">Select a patient to see their record.</p>
          )}
        </section>
      </main>
    </div>
  )
}
