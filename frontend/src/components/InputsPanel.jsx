export default function InputsPanel({ inputs }) {
  return (
    <section>
      <h2>Inputs</h2>
      {inputs.map((row) => (
        <div key={row.label}>
          {row.label}: {row.value ?? 'Not available'}
        </div>
      ))}
    </section>
  )
}
