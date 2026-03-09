import './CreateUser.css'
import { useState, setError } from "react";

function CreateUser()
{
  function passwordCheck(e, password, confirmPassword)
{
    if (password !== confirmPassword)
    {
        setError("AHHHHH");
        return;
    }
    setError("")
    console.log("Account can be created")
}
  function submitCreationForm()
  {
    
  }


  function SignUpForm()
{
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [email, setEmail] = useState("");
    const [confirmPassword, setConfirmPassword] = useState("");
    return(
    <div className='CreateUser'>
        <p>
    <input type="text" placeholder="Username" value={username} onChange={(e) => setUsername(e.target.value)}/> 
    <p></p>       
    <input type="password" placeholder="Password" value={password} onChange={(e) => setPassword(e.target.value)}/> 
    <p></p> 
    <input type="password" placeholder="ReEnter Password" value={confirmPassword} onChange={(e) => setConfirmPassword(e.target.value)}/> 
    <p></p>
    <input type="email" placeholder="Email" value={email} onChange={(e) => setEmail(e.target.value)}/> 
    <p></p>
    <button onClick={(e) => passwordCheck(e, password, confirmPassword)}>Submit</button>
        </p>
    </div>
    )
}
return(<p><SignUpForm/></p>);
}

export default CreateUser;