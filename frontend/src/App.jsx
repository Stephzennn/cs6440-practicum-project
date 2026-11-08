import { useEffect, useState } from 'react'
import { apiGet } from './api.js'


import Header from './components/Header.jsx'
import PatientBanner from './components/PatientBanner.jsx'
import InputsPanel from './components/InputsPanel.jsx'
import CounterfactualPanel from './components/CounterfactualPanel.jsx'
import RiskResults from './components/RiskResults.jsx'
import { patient, inputs, models } from './sampleData.js'




export default function App() {
  const [health, setHealth] = useState(null)
  const [error, setError] = useState(false)

  useEffect(() => {
    apiGet('/health').then(setHealth).catch(() => setError(true))
  }, [])

  return (
    <main>
      
      <Header />
      <PatientBanner patient={patient} />
      <InputsPanel inputs={inputs} />
      <CounterfactualPanel />
      <RiskResults models={models} />
    </main>
  )
}
