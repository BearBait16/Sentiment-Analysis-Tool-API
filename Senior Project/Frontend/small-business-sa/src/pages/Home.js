import './Home.css';
import { useNavigate } from "react-router-dom";


function Home() {

  const navigate = useNavigate();

  function handleDashboardButton(signedIn) {
    if (signedIn) {
      navigate("/UserDashboard");
    } else {
      navigate("/SignIn");
    }
  }

  return (
        <div className="App">
      <header className="App-header">
        <p>Welcome to My Senior Project!</p>
        <button onClick={() => navigate("/LearnMore")}>Learn More Here!</button>
        <p>
          Sentiment Analysis for Small Business
          Using Social Media
        </p>

        <button onClick={() => handleDashboardButton(false)}>
          Dashboard
        </button>

        <button onClick={() => navigate("/CreateUser")}>
          No account? Create a New User Here
        </button>

      </header>
    </div>
  );
}

export default Home;