// General Imports
import { Routes, Route, useNavigate } from "react-router-dom";
import React from "react";
import { useEffect, useState } from "react";
import axios from "axios";
import SRPage from "../SRPage/SRPage";
import { hardData } from "../SRPage/hardData";
import SearchField from "../../components/SearchField/SearchField";
import VideoPage from "../VideoPage/VideoPage";
import { YOUTUBE_API } from "../../localKey";

function HomePage() {
  const [videoResults, setVideoResults] = useState(hardData);
  const navigate = useNavigate();

  if (process.env.NODE_ENV !== "production") {
    console.log("It's working!");
  }

  const fetchResults = async (searchTerm) => {
    try {
      let response = await axios.get(
        `https://www.googleapis.com/youtube/v3/search`,
        {
          params: {
            q: searchTerm,
            key: YOUTUBE_API,
            part: "snippet",
            type: "video",
            maxResults: 5,
          },
        }
      );
      setVideoResults(response.data.items);
      navigate("/");
    } catch (error) {
      console.log(error.message);
    }
  };

  useEffect(() => {
    fetchResults("xrp");
  }, []);

  

  return (
    <div className="container">
      <SearchField handleSearch={fetchResults} />
      <Routes>
        <Route
          path="/"
          element={<SRPage results={videoResults} />}
        />
        <Route path="/:videoId" element={<VideoPage />} />
      </Routes>
    </div>
  );
}

export default HomePage;