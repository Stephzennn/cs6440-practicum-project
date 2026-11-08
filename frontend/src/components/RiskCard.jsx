import RiskBadge from './RiskBadge.jsx'

export default function RiskCard({ model }) {
  return (
    <div>
      <h3>{model.name}</h3>
      <p>{model.value}</p>
      <p>{model.unit}</p>
      <RiskBadge level={model.level} />
      <p>Top drivers: {model.drivers}</p>
    </div>
  )
}
