import { Link, NavLink } from "react-router-dom";
import "../App.css";

function Navbar() {
return ( <header className="navbar">
<Link to="/" className="nav-logo">
MediCare </Link>

  <nav className="nav-links">
    <NavLink to="/" end>
      Home
    </NavLink>

    <NavLink to="/doctors">
      Doctors
    </NavLink>

    <NavLink to="/services">
      Services
    </NavLink>

    <NavLink to="/patients">
      Patients
    </NavLink>

    <NavLink to="/clinics">
      Clinics
    </NavLink>
  </nav>
  <Link to="/appointments" className="book-btn">
    احجز موعد
  </Link>
</header>
);
}

export default Navbar;

