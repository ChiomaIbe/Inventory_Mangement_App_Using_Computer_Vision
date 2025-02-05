# frontend/README.md

# Computer Vision App - Frontend

This is the frontend part of the Computer Vision App, built using React. The application interfaces with a FastAPI backend to provide real-time counts of densely packed boxes and identify defected boxes.

## Getting Started

### Prerequisites

- Node.js (version 14 or higher)
- npm (Node Package Manager)

### Installation

1. Clone the repository:

   git clone <repository-url>

2. Navigate to the frontend directory:

   cd computer-vision-app/frontend

3. Install the dependencies:

   npm install

### Running the Application

To start the development server, run:

npm start

The application will be available at `http://localhost:3000`.

### Folder Structure

- **public/**: Contains static files like `index.html`.
- **src/**: Contains the source code for the React application.
  - **App.js**: Main component that sets up routing and layout.
  - **components/**: Contains React components, including `BoxList.js` for displaying box information.
  - **services/**: Contains API service functions for making requests to the backend.
  - **index.js**: Entry point for the React application.

### Environment Variables

You can configure environment variables in the `.env` file. Make sure to set the backend API URL:

REACT_APP_API_URL=http://localhost:8000

### Usage

Once the application is running, you can interact with the UI to view the counts of boxes and their defect statuses. The frontend communicates with the backend API to fetch and display the relevant data.

### Contributing

Feel free to submit issues or pull requests for any improvements or bug fixes.

### License

This project is licensed under the MIT License. See the LICENSE file for details.