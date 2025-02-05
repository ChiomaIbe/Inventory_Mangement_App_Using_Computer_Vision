import React, { useEffect, useState } from 'react';
import BoxList from './components/BoxList';
import { fetchBoxData } from './services/api';

const App = () => {
  const [boxes, setBoxes] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const getBoxData = async () => {
      try {
        const data = await fetchBoxData();
        setBoxes(data);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    getBoxData();
  }, []);

  if (loading) {
    return <div>Loading...</div>;
  }

  if (error) {
    return <div>Error: {error}</div>;
  }

  return (
    <div>
      <h1>Box Detection App</h1>
      <BoxList boxes={boxes} />
    </div>
  );
};

export default App;