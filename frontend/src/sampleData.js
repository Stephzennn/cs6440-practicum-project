// Hard-coded sample values (replace with apiGet calls later)
export const patient = { name: 'Rick Sanchez', age: 54, sex: 'Male', dob: '03/14/1972', mrn: '4827193' }

export const inputs = [
  { label: 'Age', value: '54' },
  { label: 'Sex', value: 'Male' },
  { label: 'BMI', value: '31.2' },
  { label: 'Blood pressure', value: '138/86' },
  { label: 'Fasting glucose', value: '108 mg/dL' },
  { label: 'HDL', value: '42 mg/dL' },
  { label: 'Triglycerides', value: '168 mg/dL' },
  { label: 'Family history', value: 'Yes' },
  { label: 'HbA1c', value: null },
]

export const models = [
  { id: 'qdiabetes_b', name: 'QDiabetes-2018 (Model B)', value: '14%', unit: '10-year risk', level: 'High', drivers: 'BMI, fasting glucose' },
  { id: 'framingham', name: 'Framingham Offspring (2007)', value: '11%', unit: '8-year risk', level: 'Moderate', drivers: 'fasting glucose, low HDL' },
  { id: 'ada', name: 'ADA / CDC Risk Test', value: '6 / 10', unit: 'Score (5+ = increased risk)', level: 'Increased', drivers: 'age, BMI, family history' },
  { id: 'findrisc', name: 'FINDRISC', needs: 'waist size' },
  { id: 'qdiabetes_c', name: 'QDiabetes-2018 (Model C)', needs: 'HbA1c' },
]
