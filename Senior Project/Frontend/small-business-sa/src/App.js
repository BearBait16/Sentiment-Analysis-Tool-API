import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <p>
          Welcome to My Senior Project
        </p>
        <p>
          Sentiment Analysis for Small Business
          Using Social Media
        </p>
        <button onClick={handleDashboardButton()}>Dashboard</button>
        <button>Create User</button>
      </header>
    </div>
  );
}

function handleDashboardButton()
{
      alert('You clicked me!');
}

export default App;
