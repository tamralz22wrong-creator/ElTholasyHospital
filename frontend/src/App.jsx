import { BrowserRouter, Routes, Route } from "react-router-dom";

import Navbar from "./components/Navbar";
import Appointments from "./pages/Appointments"
import Home from "./pages/Home";
import Patients from "./pages/Patients";
import Doctors from "./pages/Doctors";
import DoctorDetails from "./pages/DoctorDetails";
import Clinics from "./pages/Clinics"; // 1. تم إضافة الاستيراد الصحيح هنا

import "./App.css";

function App() {
  return (
    <BrowserRouter>
      <Navbar />

      <Routes>
        <Route path="/" element={<Home />} />
        
        {/* 2. تم تصحيح الخطأ الإملائي من Clincs إلى Clinics */}
        <Route path="/clinics" element={<Clinics />} />

        <Route path="/patients" element={<Patients />} />

        <Route path="/doctors" element={<Doctors />} />
        <Route path="/appointments" element={<Appointments/>}/>

        <Route
          path="/doctors/:id"
          element={<DoctorDetails />}
        />
      </Routes>
    </BrowserRouter>
  );
}

export default App;










