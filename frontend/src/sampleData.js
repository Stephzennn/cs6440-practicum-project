// Hard-coded sample values (replace with apiGet calls later)
export const patient = { name: 'Rick Sanchez', age: 54, sex: 'Male', dob: '03/14/1972', mrn: '4827193' }

// "value" is the loaded value (stand-in for FHIR). Keys match backend/data/sample_patient.json
export const inputs = [
  { key: 'age', label: 'Age', value: '54' },
  { key: 'sex', label: 'Sex', value: 'Male' },
  { key: 'bmi', label: 'BMI', value: '31.2' },
  { key: 'systolic_bp', label: 'Systolic BP (mmHg)', value: '138' },
  { key: 'diastolic_bp', label: 'Diastolic BP (mmHg)', value: '86' },
  { key: 'fasting_glucose', label: 'Fasting glucose (mg/dL)', value: '108' },
  { key: 'hdl', label: 'HDL (mg/dL)', value: '42' },
  { key: 'triglycerides', label: 'Triglycerides (mg/dL)', value: '168' },
  { key: 'family_history', label: 'Family history of diabetes', value: 'Yes' },
  { key: 'hba1c', label: 'HbA1c (%, optional)', value: null },
  { key: 'waist_cm', label: 'Waist (cm, optional)', value: null },
]

export const models = [
  { id: 'qdiabetes_b', name: 'QDiabetes-2018 (Model B)', value: '14%', unit: '10-year risk', level: 'High', drivers: 'BMI, fasting glucose' },
  { id: 'framingham', name: 'Framingham Offspring (2007)', value: '11%', unit: '8-year risk', level: 'Moderate', drivers: 'fasting glucose, low HDL' },
  { id: 'ada', name: 'ADA / CDC Risk Test', value: '6 / 10', unit: 'Score (5+ = increased risk)', level: 'Increased', drivers: 'age, BMI, family history' },
  { id: 'findrisc', name: 'FINDRISC', needs: 'waist size' },
  { id: 'qdiabetes_c', name: 'QDiabetes-2018 (Model C)', needs: 'HbA1c' },
]
