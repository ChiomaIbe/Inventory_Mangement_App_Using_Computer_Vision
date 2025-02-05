import React, { useEffect, useState } from 'react';
import { fetchBoxes } from '../services/api';

const BoxList = () => {
    const [boxes, setBoxes] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const getBoxes = async () => {
            try {
                const data = await fetchBoxes();
                setBoxes(data);
            } catch (err) {
                setError(err.message);
            } finally {
                setLoading(false);
            }
        };

        getBoxes();
    }, []);

    if (loading) {
        return <div>Loading...</div>;
    }

    if (error) {
        return <div>Error: {error}</div>;
    }

    return (
        <div>
            <h2>Detected Boxes</h2>
            <ul>
                {boxes.map(box => (
                    <li key={box.id}>
                        Box ID: {box.id}, Status: {box.defected ? 'Defected' : 'Normal'}
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default BoxList;