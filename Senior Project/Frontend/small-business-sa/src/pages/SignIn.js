import './App.css';
import { useNavigate } from "react-router-dom";

function App() {

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
        <p>Welcome to My Senior Project</p>
        <p>
          Sentiment Analysis for Small Business
          Using Social Media
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

export default App;
