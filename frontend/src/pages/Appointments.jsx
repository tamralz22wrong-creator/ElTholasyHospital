
import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";

function Appointments() {
  const navigate = useNavigate();

  // بيانات الأطباء والعيادات
  const [doctors, setDoctors] = useState([]);
  const [clinics, setClinics] = useState([]);

  // بيانات الحجز
  const [formData, setFormData] = useState({
    doctor: "",
    clinic: "",
    patient_name: "",
    appointment_date: "",
    notes: "",
  });

  // حالات الصفحة
  const [loading, setLoading] = useState(false);
  const [fetching, setFetching] = useState(true);
  const [error, setError] = useState("");
  const [success, setSuccess] = useState(false);

  // عنوان Django
  const API_URL = "http://127.0.0.1:8000";

  // جلب الأطباء والعيادات
  useEffect(() => {
    const fetchData = async () => {
      try {
        setFetching(true);
        setError("");

        const [doctorsResponse, clinicsResponse] = await Promise.all([
          fetch(`${API_URL}/doctors/`),
          fetch(`${API_URL}/clinics/`),
        ]);

        if (!doctorsResponse.ok || !clinicsResponse.ok) {
          throw new Error("فشل تحميل بيانات الأطباء أو العيادات");
        }

        const doctorsData = await doctorsResponse.json();
        const clinicsData = await clinicsResponse.json();

        // دعم البيانات العادية وبيانات Django REST Framework Pagination
        setDoctors(
          Array.isArray(doctorsData)
            ? doctorsData
            : doctorsData.results || []
        );

        setClinics(
          Array.isArray(clinicsData)
            ? clinicsData
            : clinicsData.results || []
        );

      } catch (err) {
        console.error(err);
        setError("حدث خطأ أثناء تحميل بيانات الأطباء والعيادات");
      } finally {
        setFetching(false);
      }
    };

    fetchData();
  }, []);

  // تغيير قيم الحقول
  const handleChange = (e) => {
    const { name, value } = e.target;

    setFormData((prev) => ({
      ...prev,
      [name]: value,
    }));
  };

  // إرسال الحجز
  const handleSubmit = async (e) => {
    e.preventDefault();

    setLoading(true);
    setError("");

    try {
      const response = await fetch(`${API_URL}/appointments/`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(formData),
      });

      const data = await response.json();

      if (!response.ok) {
        console.error("Server error:", data);
        throw new Error(
          data.detail ||
          data.message ||
          "فشل تسجيل الحجز، تأكد من صحة البيانات"
        );
      }

      setSuccess(true);

      setFormData({
        doctor: "",
        clinic: "",
        patient_name: "",
        appointment_date: "",
        notes: "",
      });

      setTimeout(() => {
        navigate("/");
      }, 2000);

    } catch (err) {
      console.error(err);
      setError(err.message || "حدث خطأ أثناء تسجيل الحجز");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="form-container">

      <h2>حجز موعد طبي جديد</h2>

      {/* رسالة الخطأ */}
      {error && (
        <div className="error-message">
          {error}
        </div>
      )}

      {/* رسالة النجاح */}
      {success && (
        <div className="loading" style={{ color: "green" }}>
          🟢 تم تسجيل حجزك بنجاح! جاري تحويلك...
        </div>
      )}

      {/* تحميل البيانات */}
      {fetching ? (
        <p>جاري تحميل بيانات الأطباء والعيادات...</p>
      ) : (
        <form onSubmit={handleSubmit}>

          {/* اسم المريض */}
          <input
            type="text"
            name="patient_name"
            placeholder="اسم المريض بالكامل"
            value={formData.patient_name}
            onChange={handleChange}
            required
          />

          {/* اختيار العيادة */}
          <select
            name="clinic"
            value={formData.clinic}
            onChange={handleChange}
            required
          >
            <option value="">اختر العيادة المطلوبة</option>

            {clinics.map((clinic) => (
              <option key={clinic.id} value={clinic.id}>
                {clinic.name}
              </option>
            ))}
          </select>

          {/* اختيار الطبيب */}
          <select
            name="doctor"
            value={formData.doctor}
            onChange={handleChange}
            required
          >
            <option value="">اختر الطبيب المعالج</option>

            {doctors.map((doctor) => (
              <option key={doctor.id} value={doctor.id}>
                {doctor.full_name} - {doctor.specialization}
              </option>
            ))}
          </select>

          {/* تاريخ الموعد */}
          <input
            type="datetime-local"
            name="appointment_date"
            value={formData.appointment_date}
            onChange={handleChange}
            required
          />

          {/* الملاحظات */}
          <textarea
            name="notes"
            placeholder="ملاحظات طبية أو أعراض (اختياري)"
            value={formData.notes}
            onChange={handleChange}
            rows="4"
          />

          {/* زر الحجز */}
          <button
            type="submit"
            className="btn"
            disabled={loading || success}
          >
            {loading
              ? "جاري تسجيل الحجز..."
              : "تأكيد الحجز"}
          </button>

        </form>
      )}

    </div>
  );
}

export default Appointments;

