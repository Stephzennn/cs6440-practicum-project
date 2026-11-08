export default function PatientBanner({ patient }) {
  return (
    <section>
      Patient Name: <strong>{patient.name}</strong> {patient.age} y · {patient.sex} DOB {patient.dob} MRN {patient.mrn}
    </section>
  )
}
