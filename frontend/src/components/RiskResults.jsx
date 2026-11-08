import { useState } from 'react'
import RiskCard from './RiskCard.jsx'
import ModelSelector from './ModelSelector.jsx'
import CombinedEstimate from './CombinedEstimate.jsx'

export default function RiskResults({ models }) {
  const [selected, setSelected] = useState(['qdiabetes_b', 'framingham', 'ada'])

  const toggle = (id) =>
    setSelected((s) => (s.includes(id) ? s.filter((x) => x !== id) : [...s, id]))

  return (
    <section>
      <h2>Risk results</h2>
      {models.filter((m) => selected.includes(m.id)).map((m) => (
        <RiskCard key={m.id} model={m} />
      ))}
      <ModelSelector models={models} selected={selected} onToggle={toggle} />
      <CombinedEstimate />
    </section>
  )
}
