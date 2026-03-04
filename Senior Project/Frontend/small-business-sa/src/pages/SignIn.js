import './SignIn.css';
import { useNavigate } from "react-router-dom";
import { useState } from 'react';



function SignIn() {
  function SignInForm()
    {
      const [username, setUsername] = useState("");
      const [password, setPassword] = useState("");
      return(
        <div>
          <p>
        <input type="text" placeholder="Username" value={username} onChange={(e) => setUsername(e.target.value)}/> 
        <p></p>       
        <input type="password" placeholder="Password" value={password} onChange={(e) => setPassword(e.target.value)}/> 
        <p></p> 
        <button onClick={() => handleDashboardButton(false)}>Submit</button>
          </p>
        </div>
      )
    }
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
        <SignInForm />
        <button onClick={() => navigate("/create-user")}>
          No account? Create a New User Here
        </button>
      </header>
    </div>
  );
}

export default SignIn;
