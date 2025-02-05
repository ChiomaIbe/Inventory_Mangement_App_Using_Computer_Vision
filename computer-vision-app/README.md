# Computer Vision App

This project is a computer vision application designed to identify densely packed boxes in real-time, providing counts of both total boxes and defected boxes. The application utilizes the SKU110K_CVPR19 dataset for training and evaluation.

## Project Structure

The project is divided into two main parts: the backend and the frontend.

### Backend

The backend is built using FastAPI and is responsible for handling API requests related to box detection.

- **main.py**: Entry point of the FastAPI application.
- **api/endpoints/boxes.py**: Defines API endpoints for counting boxes and identifying defected boxes.
- **core/config.py**: Contains configuration settings for the application.
- **models/box.py**: Defines the Box model structure.
- **schemas/box.py**: Pydantic schemas for validating and serializing box data.
- **services/box_detection.py**: Logic for detecting boxes using the Edge Impulse model.
- **Dockerfile**: Instructions for building a Docker image for the backend.
- **requirements.txt**: Lists Python dependencies required for the backend.

### Frontend

The frontend is built using React and provides a user interface for interacting with the backend.

- **public/index.html**: Main HTML file for the React application.
- **src/App.js**: Main component that sets up routing and layout.
- **src/components/BoxList.js**: Component that displays a list of detected boxes and their statuses.
- **src/services/api.js**: Functions for making API calls to the backend.
- **src/index.js**: Entry point for the React application.
- **package.json**: Configuration file for npm, listing dependencies and scripts.
- **.env**: Contains environment variables for the frontend application.

## Setup Instructions

### Backend

1. Navigate to the `backend` directory.
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the FastAPI application:
   ```
   uvicorn app.main:app --reload
   ```

### Frontend

1. Navigate to the `frontend` directory.
2. Install the required dependencies:
   ```
   npm install
   ```
3. Start the React application:
   ```
   npm start
   ```

## Usage

Once both the backend and frontend are running, you can access the application in your web browser. The frontend will communicate with the backend to provide real-time counts of boxes and defected boxes.

## License

This project is licensed under the MIT License.