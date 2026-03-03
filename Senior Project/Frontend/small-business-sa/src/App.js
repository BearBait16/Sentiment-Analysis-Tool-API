import { Routes, Route } from "react-router-dom";

import Home from "./pages/Home";
import LearnMore from "./pages/LearnMore";
import UserDashboard from "./pages/UserDashboard";
import SignIn from "./pages/SignIn";
import CreateUser from "./pages/CreateUser";

function App() {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/LearnMore" element={<LearnMore />} />
      <Route path="/UserDashboard" element={<UserDashboard />} />
      <Route path="/SignIn" element={<SignIn />} />
      <Route path="/CreateUser" element={<CreateUser />} />
    </Routes>
  );
}

export default App;