# Computer Vision App Backend

This README file provides an overview of the backend component of the Computer Vision App, which is designed to identify densely packed boxes in real-time and detect any defects.

## Project Structure

The backend is structured as follows:

```
backend/
├── app/
│   ├── main.py                # Entry point of the FastAPI application
│   ├── api/
│   │   └── endpoints/
│   │       └── boxes.py       # API endpoints for box detection
│   ├── core/
│   │   └── config.py          # Configuration settings
│   ├── models/
│   │   └── box.py             # Box data model
│   ├── schemas/
│   │   └── box.py             # Pydantic schemas for validation
│   └── services/
│       └── box_detection.py    # Logic for detecting boxes
├── Dockerfile                  # Docker instructions for the backend
├── requirements.txt            # Python dependencies
└── README.md                   # Documentation for the backend
```

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd computer-vision-app/backend
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**
   ```bash
   uvicorn app.main:app --reload
   ```

   The application will be running at `http://127.0.0.1:8000`.

## API Usage

### Endpoints

- **GET /boxes/count**
  - Description: Returns the count of detected boxes.
  
- **GET /boxes/defected**
  - Description: Returns a list of defected boxes.

## Docker

To build and run the Docker container, use the following commands:

```bash
docker build -t computer-vision-app-backend .
docker run -p 8000:8000 computer-vision-app-backend
```

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

- Dataset: SKU110K_CVPR19
- Framework: FastAPI
- Machine Learning: Edge Impulse

For any questions or contributions, please feel free to reach out!