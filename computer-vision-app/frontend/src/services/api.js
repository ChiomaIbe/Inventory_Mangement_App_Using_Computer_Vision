import axios from 'axios';

const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

export const getBoxCounts = async () => {
    try {
        const response = await axios.get(`${API_URL}/boxes/count`);
        return response.data;
    } catch (error) {
        console.error('Error fetching box counts:', error);
        throw error;
    }
};

export const getDefectedBoxes = async () => {
    try {
        const response = await axios.get(`${API_URL}/boxes/defected`);
        return response.data;
    } catch (error) {
        console.error('Error fetching defected boxes:', error);
        throw error;
    }
};