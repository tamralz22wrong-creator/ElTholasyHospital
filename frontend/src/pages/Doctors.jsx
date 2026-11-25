import { useState, useEffect } from "react";

function Doctors() {
  const [doctors, setDoctors] = useState([]); // تعديل الاسم إلى الجمع للتنظيم
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(false);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/doctors/")
      .then((response) => {
        if (!response.ok) {
          throw new Error("Failed to fetch doctors");
        }
        return response.json();
      })
      .then((data) => {
        setDoctors(data);
        setLoading(false);
      })
      .catch((error) => {
        console.error(error);
        setError(true);
        setLoading(false);
      });
  }, []);

  // استخدام كلاس التنسيق الخاص بك للتحميل والخطأ
  if (loading) {
    return <div className="loading">جاري تحميل الأطباء...</div>;
  }

  if (error) {
    return <div className="error-message">حدث خطأ أثناء جلب البيانات. يرجى المحاولة مرة أخرى.</div>;
  }

  if (doctors.length === 0) {
    return <div className="empty-message">لم يتم العثور على أطباء مسجلين حالياً.</div>;
  }

  return (
    <div className="services-section">
      <h1>Our Doctors</h1>
      <p>Find the best doctors in our hospital</p>

      {/* استخدام حاوية الـ Grid الاحترافية من ملف الـ CSS الخاص بك */}
      <div className="doctors-container">
        {doctors.map((item) => (
          <div key={item.id} className="doctor-card">
            {/* 1. تعديل الحقل إلى full_name ليطابق دجانجو */}
            <h2>{item.full_name}</h2>
            
            {/* 2. تعديل الحقل إلى specialization ليطابق دجانجو */}
            <p><strong>التخصص:</strong> {item.specialization}</p>
            
            {/* 3. سحب بقية الحقول الجديدة الفاخرة المتاحة في الـ API */}
            <p><strong>الهاتف:</strong> {item.phone}</p>
            <p><strong>الخبرة:</strong> {item.years_of_experience} سنوات</p>
            <p><strong>الحالة:</strong> {item.is_available ? "🟢 متاح حالياً" : "🔴 غير متاح"}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Doctors;



