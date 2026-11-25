import { useState, useEffect } from "react";
import { useParams } from "react-router-dom"; // استدعاء useParams لجلب الـ ID من الرابط تلقائياً

function DoctorDetails() {
  const { id } = useParams(); // التقاط المتغير :id من مسار الصفحة الفعلي
  const [doctor, setDoctor] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(false);

  useEffect(() => {
    // استخدام الـ id الديناميكي في دالة الـ fetch بدلاً من الرقم الثابت 1
    fetch(`http://127.0.0{id}/`)
      .then((response) => {
        if (!response.ok) {
          throw new Error("Something went wrong");
        }
        return response.json();
      })
      .then((data) => {
        setDoctor(data);
      })
      .catch((error) => {
        console.error(error);
        setError(true);
      })
      .finally(() => {
        setLoading(false);
      });
  }, [id]); // إعادة تشغيل الـ Effect إذا تغير الـ id في الرابط

  // تطبيق كلاسات التنسيق المجهزة في ملف الـ CSS الخاص بك للتحميل والخطأ
  if (loading) {
    return <div className="loading">جاري تحميل تفاصيل الطبيب...</div>;
  }

  if (error) {
    return <div className="error-message">حدث خطأ أثناء تحميل البيانات. يرجى المحاولة مرة أخرى.</div>;
  }

  if (!doctor) {
    return <div className="empty-message">لم يتم العثور على هذا الطبيب في النظام.</div>;
  }

  return (
    // استخدام كلاس التنسيق الاحترافي المجهز مسبقاً في ملف الـ CSS لديك (المطوّر لـ Doctor Details)
    <div className="doctor-details">
      <h1>تفاصيل الطبيب</h1>

      {/* استخدام الحقل الصحيح full_name ليطابق Django المحدث */}
      <h2>{doctor.full_name}</h2>

      {/* سحب واستعراض كافة التفاصيل العميقة من الـ API بالتنسيق المناسب */}
      <p><strong>التخصص:</strong> {doctor.specialization}</p>
      <p><strong>رقم الهاتف:</strong> {doctor.phone}</p>
      <p><strong>البريد الإلكتروني:</strong> {doctor.email}</p>
      <p><strong>رقم ترخيص المزاولة:</strong> {doctor.license_number}</p>
      <p><strong>سنوات الخبرة:</strong> {doctor.years_of_experience} سنوات</p>
      {doctor.clinic_address && <p><strong>عنوان العيادة:</strong> {doctor.clinic_address}</p>}
      <p><strong>حالة المواعيد:</strong> {doctor.is_available ? "🟢 متاح لاستقبال الحجوزات" : "🔴 غير متاح حالياً"}</p>
    </div>
  );
}

export default DoctorDetails;

