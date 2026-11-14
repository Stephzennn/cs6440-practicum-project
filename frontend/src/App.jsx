import { useEffect, useState } from 'react'
import { apiGet, apiPost } from './api.js'


import Header from './components/Header.jsx'
import PatientBanner from './components/PatientBanner.jsx'
import InputsPanel from './components/InputsPanel.jsx'
import CounterfactualPanel from './components/CounterfactualPanel.jsx'
import RiskResults from './components/RiskResults.jsx'
import { patient, inputs, models } from './sampleData.js'


// Start with an empty form: { age: '', sex: '', ... }
const emptyForm = Object.fromEntries(inputs.map((row) => [row.key, '']))


export default function App() {
  const [health, setHealth] = useState(null)
  const [error, setError] = useState(false)

  const [loaded, setLoaded] = useState(inputs)
  const [form, setForm] = useState(emptyForm)
  const [results, setResults] = useState({})
  const [status, setStatus] = useState('idle')

  useEffect(() => {
    apiGet('/health').then(setHealth).catch(() => setError(true))
  }, [])

  const updateField = (key, value) => setForm((f) => ({ ...f, [key]: value }))

  const calculate = async () => {
    // Use the typed value, or keep the loaded value if the input is empty
    const filled = Object.fromEntries(
      loaded.map((row) => [row.key, form[row.key] !== '' ? form[row.key] : row.value ?? ''])
    )
    // Show the values used in the Loaded value column
    setLoaded(loaded.map((row) => ({ ...row, value: filled[row.key] === '' ? null : filled[row.key] })))

    // Empty fields -> null, numbers -> Number, text (sex, family history) stays as is
    const body = Object.fromEntries(
      Object.entries(filled).map(([k, v]) => [k, v === '' ? null : isNaN(v) ? v : Number(v)])
    )
    setStatus('loading')
    try {
      setResults(await apiPost('/risk', body))
      setStatus('done')
    } catch {
      setStatus('error')
    }
  }

  // Backend results (keyed by model id) replace the dummy values on the cards
  const shownModels = models.map((m) => ({ ...m, ...results[m.id] }))

  return (
    <main>

      <Header />
      <PatientBanner patient={patient} />
      <InputsPanel
        inputs={loaded}
        form={form}
        onChange={updateField}
        onCalculate={calculate}
        status={status}
      />
      <CounterfactualPanel />
      <RiskResults models={shownModels} />
    </main>
  )
}
