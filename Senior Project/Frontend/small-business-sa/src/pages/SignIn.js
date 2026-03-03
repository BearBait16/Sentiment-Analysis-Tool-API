import './SignIn.css';
import { useNavigate } from "react-router-dom";

function SignIn() {

  const navigate = useNavigate();

  function handleDashboardButton(signedIn) {
    let page = "";

    if (signedIn === true) {
      page = "/UserDashboard";
    } else {
      page = "/SignIn";
    }

    navigate(page);
  }

  return (
    <div className="App">
      <header className="App-header">
        <p>Sign in!</p>
        <p>
          <entry></entry>
        </p>

        <button onClick={() => handleDashboardButton(false)}>
          Submit
        </button>

        <button onClick={() => navigate("/create-user")}>
          No account? Create a New User Here
        </button>

      </header>
    </div>
  );
}

export default SignIn;
