// Fields with a fixed set of choices use a dropdown, everything else is a number
const CHOICES = { sex: ['Male', 'Female'], family_history: ['Yes', 'No'] }

export default function InputsPanel({ inputs, form, onChange, onCalculate, status }) {
  return (
    <section>
      <h2>Inputs</h2>
      <button disabled>Load from FHIR</button>

      <table>
        <thead>
          <tr>
            <th>Field</th>
            <th>Loaded value</th>
            <th>Manual Input</th>
          </tr>
        </thead>
        <tbody>
          {inputs.map((row) => (
            <tr key={row.key}>
              <td><label htmlFor={row.key}>{row.label}</label></td>
              <td>{row.value ?? 'Not available'}</td>
              <td>
                {CHOICES[row.key] ? (
                  <select id={row.key} value={form[row.key]} onChange={(e) => onChange(row.key, e.target.value)}>
                    <option value="">--</option>
                    {CHOICES[row.key].map((c) => <option key={c}>{c}</option>)}
                  </select>
                ) : (
                  <input
                    id={row.key}
                    type="number"
                    step="any"
                    value={form[row.key]}
                    onChange={(e) => onChange(row.key, e.target.value)}
                  />
                )}
              </td>
            </tr>
          ))}
        </tbody>
      </table>

      <button onClick={onCalculate} disabled={status === 'loading'}>
        {status === 'loading' ? 'Calculating...' : 'Calculate'}
      </button>
      {status === 'error' && <p>Could not calculate. Is the backend running?</p>}
    </section>
  )
}
