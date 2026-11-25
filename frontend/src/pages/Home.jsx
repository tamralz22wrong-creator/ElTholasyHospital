
import { useNavigate } from "react-router-dom";

function Home() {
  const navigate = useNavigate();

  return (
    <div className="home">

      <div className="welcome-section">
        <h1>Welcome to MediCare</h1>
        <p>Your health is our priority.</p>

        <button className="book-btn">
          Book Appointment
        </button>
      </div>

      <div className="services-section">
        <h2>Our Services</h2>

        <div className="services-list">

          <div
            className="service-card"
            onClick={() => navigate("/doctors")}
          >
            <h3>Doctors</h3>
            <p>Find and manage hospital doctors.</p>
          </div>

          <div className="service-card"
          onClick={()=> navigate("/patients")}>
            <h3>Patients</h3>
            <p>View and manage patient information.</p>
          </div>

          <div className="service-card"
          onClick={()=> navigate("/clinics")}>
            <h3>Clinics</h3>
            <p>Explore our available clinics.</p>
          </div>

        </div>
      </div>

    </div>
  );
}

export default Home;

