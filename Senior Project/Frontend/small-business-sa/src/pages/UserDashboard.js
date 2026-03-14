import { useState } from "react";

function UserDashboard()
{
const [data, setData] = useState(null);

// Handles The Drag and Drop and original processing of the Instagram json object
function InputDms()
{
    async function HandleDragAndDrop(event)
    {
        event.preventDefault();
        const file = event.dataTransfer.files[0];
        const reader = new FileReader();
        reader.onload = function(e) {
            const text = e.target.result;
            const json = JSON.parse(text);
            console.log(json);
            setData(json);
        }
        reader.readAsText(file);
    }
    function handleDragOver(event) {
    event.preventDefault();
  }
  return (
    <div
      onDrop={HandleDragAndDrop}
      onDragOver={handleDragOver}
      style={{
        border: "2px dashed gray",
        padding: "50px",
        textAlign: "center"
      }}>
      Drop your Instagram JSON file here
      {data && <p>{data.messages.length} messages loaded</p>}
    </div>
  );
}

// This takes the json object, and cuts out the crud we don't need
function MapJson({data})
   {
  return (
    <div>
      {data.messages.map((msg, index) => (
        <div key={index}>
          <p><b>{msg.sender_name}</b></p>
          <p>{msg.content}</p>
          <p>{new Date(msg.timestamp_ms).toLocaleString()}</p>
          <hr />
        </div>
      ))}
    </div>
        );
    }

// This sends the Json object to the backend, and names the images

// This is the actual page, showing the images that are loaded after this data is sent
    return(
    <div className="container">
     <p>
      <img src="/img1.png" className="top-left" />
      <img src="/img2.png" className="top-right" />
      <img src="/img3.png" className="bottom-left" />
      <img src="/img4.png" className="bottom-right" />
      You made it to the dashboard
      <InputDms />
    {data && <MapJson data={data} />}     </p>
    </div>
    )
}

export default UserDashboard;