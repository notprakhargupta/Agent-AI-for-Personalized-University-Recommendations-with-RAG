
import React, { useState } from "react";
import axios from "axios";

function App() {
  const [query, setQuery] = useState("");
  const [recommendations, setRecommendations] = useState("");

  const handleQuerySubmit = async () => {
    try {
      const response = await axios.post("/recommendations/", { query });
      setRecommendations(response.data.recommendations);
    } catch (error) {
      console.error("Error fetching recommendations:", error);
    }
  };

  return (
    <div>
      <h1>University Recommendations</h1>
      <input
        type="text"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="Enter your preferences..."
      />
      <button onClick={handleQuerySubmit}>Get Recommendations</button>
      <div>
        <h2>Recommendations:</h2>
        <p>{recommendations}</p>
      </div>
    </div>
  );
}

export default App;
