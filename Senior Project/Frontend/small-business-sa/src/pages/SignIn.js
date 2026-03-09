import './SignIn.css';
import { useNavigate } from "react-router-dom";
import { useState } from 'react';

function SignIn() {
  const navigate = useNavigate();
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
        <button onClick={() => SignInSubmission(username, password)}>Submit</button>
          </p>
        </div>
      )
    }
    // Handles Sign In call to the API
async function SignInSubmission(username, password) {
  try{const response = await fetch("http://localhost:5000/sign_in", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      name: username,
      password: password
    })
  });

  const data = await response.json();
  if (data.isGood === true)
  {
    navigate("/UserDashboard")
  }
  else
  {
    alert("BAD! YOU ENTERED YOUR USERNAME AND PASSWORD BAD")
  }}
  catch (error) {
  console.error(error);
  alert("Technically Sent, but needs to be fixed");
}}

  return (
    <div className="App">
      <header className="App-header">
        <p>Sign in!</p>
        <SignInForm />
        <button onClick={() => navigate("/CreateUser")}>
          No account? Create a New User Here
        </button>
      </header>
    </div>
  );
}

export default SignIn;
