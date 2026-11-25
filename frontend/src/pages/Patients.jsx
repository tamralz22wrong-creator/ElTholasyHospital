
import { useState, useEffect } from "react";

function Patients() {
  const [patient, setPatient] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(false);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/patients/")
      .then((response) => {
        if (!response.ok) {
          throw new Error("Something went wrong");
        }

        return response.json();
      })
      .then((data) => {
        setPatient(data);
      })
      .catch((error) => {
        console.error(error);
        setError(true);
      })
      .finally(() => {
        setLoading(false);
      });
  }, []);

  if (loading) {
    return <h2>Loading...</h2>;
  }

  if (error) {
    return <h2>Something went wrong</h2>;
  }

  if (patient.length === 0) {
    return <h2>No patients found</h2>;
  }

  return (
    <div>
      <h1>Our Patients</h1>

      {patient.map((item) => (
        <div key={item.id}>
          <h2>{item.name}</h2>
          <p>Age: {item.age}</p>
          <p>Phone: {item.phone}</p>
        </div>
      ))}
    </div>
  );
}

export default Patients;

