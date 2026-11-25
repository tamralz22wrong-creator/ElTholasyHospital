
import { useState, useEffect } from "react";

function Clinics() {
  const [clinics, setClinics] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchClinics = async () => {
      try {
        const response = await fetch(
          "http://127.0.0.1:8000/clinics/"
        );

        if (!response.ok) {
          throw new Error("Failed to fetch clinics");
        }

        const data = await response.json();

        setClinics(Array.isArray(data) ? data : data.results || []);

      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    fetchClinics();
  }, []);

  if (loading) {
    return <div className="loading">جاري تحميل العيادات...</div>;
  }

  if (error) {
    return <div className="error-message">حدث خطأ: {error}</div>;
  }

  if (clinics.length === 0) {
    return <div className="empty-message">
      لا توجد عيادات متاحة حالياً.
    </div>;
  }

  return (
    <div className="services-section">

      <h2>العيادات الطبية المتاحة</h2>

      <div className="doctors-container">

        {clinics.map((clinic) => (

          <div key={clinic.id} className="doctor-card">

            <h2>{clinic.name}</h2>

            <p>
              <strong>التخصص:</strong> {clinic.specialty}
            </p>

            <p>
              <strong>الموقع:</strong> {clinic.location}
            </p>

            {clinic.phone && (
              <p>
                <strong>رقم التواصل:</strong> {clinic.phone}
              </p>
            )}

          </div>

        ))}

      </div>

    </div>
  );
}

export default Clinics;

