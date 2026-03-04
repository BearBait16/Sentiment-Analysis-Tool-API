import { useState } from "react";

function UserDashboard()
{
  function SignUpForm()
{
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [email, setEmail] = useState("");
    return(
    <div>
        <p>
    <input type="text" placeholder="Username" value={username} onChange={(e) => setUsername(e.target.value)}/> 
    <p></p>       
    <input type="password" placeholder="Password" value={password} onChange={(e) => setPassword(e.target.value)}/> 
    <p></p> 
    <input type="email" placeholder="Email" value={email} onChange={(e) => setEmail(e.target.value)}/> 
    <button onClick={() => alert("You Pushed")}>Submit</button>
        </p>
    </div>
    )
}
return(<p><SignUpForm/></p>);
}

export default UserDashboard;