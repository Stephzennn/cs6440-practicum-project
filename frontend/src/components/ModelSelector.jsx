export default function ModelSelector({ models, selected, onToggle }) {
  return (
    <div>
      {models.map((m) => (
        <label key={m.id}>
          <input
            type="checkbox"
            checked={selected.includes(m.id)}
            disabled={Boolean(m.needs)}
            onChange={() => onToggle(m.id)}
          />
          {m.name} {m.needs && `(Needs ${m.needs})`}
        </label>
      ))}
    </div>
  )
}
