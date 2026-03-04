import './LearnMore.css';
import { useNavigate } from "react-router-dom";

function LearnMore()
{
    const navigate = useNavigate();

    return(  
        <div className='LearnMore'>
            <header className='LearnMore-header'>
        <p>This was inspired by something I had the chance to research and prototype during my internship. It wasn't 
        within the scope of what they were doing. I think something like this will work for small businesses hosted
        on social media though!

        A backend API built using python and Flask, hosted on AWS, handles sign in, api usage, and graph generation. Than, hosted on 
        AWS web server stuff, this site is held (with S3 holding the build files).

        I learned how API generation and tracking works, learned how to navigate and host full stack programs on AWS. We did it!
        Look ma! All development!

    </p>
    <button onClick={()=>navigate("../")}>
        Back to Home Page
    </button>
    </header>
    
    </div> 
    )

}
export default LearnMore;