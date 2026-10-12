import { useEffect, useState } from 'react'
import { api } from '../api.js'

export default function PatientDetail({ patientId }) {
  const [patient, setPatient] = useState(null)
  const [error, setError] = useState(null)

  useEffect(() => {
    setPatient(null)
    setError(null)
    api.getPatient(patientId).then(setPatient).catch((e) => setError(e.message))
  }, [patientId])

  if (error) return <p className="error">{error}</p>
  if (!patient) return <p className="empty">Loading…</p>

  return (
    <div className="card">
      <h2>{patient.name}</h2>
      <p className="muted">
        {patient.gender} · {patient.age} yrs · born {patient.birthdate} · {patient.city},{' '}
        {patient.state}
      </p>

      <h3>Conditions</h3>
      {patient.conditions.length === 0 ? (
        <p className="muted">None recorded.</p>
      ) : (
        <table>
          <thead>
            <tr>
              <th>Condition</th>
              <th>Onset</th>
              <th>Status</th>
            </tr>
          </thead>
          <tbody>
            {patient.conditions.map((c, i) => (
              <tr key={`${c.code}-${i}`}>
                <td>{c.description}</td>
                <td>{c.start}</td>
                <td>{c.stop ? `Resolved ${c.stop}` : 'Active'}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}

      {/* TODO(team): add your project's views here — e.g. a lab trend chart, risk score, etc. */}
    </div>
  )
}
