# Exploring API Integration with Python: Building a Custom Application

## Overview
This project involves creating a Python application that interacts with a free API of choice, processes the retrieved data, and is containerized using Docker. The application demonstrates skills in API integration, data processing, and deployment using modern tools like Docker and Python.

---

## API Information
- **API Provider**: AbstractAPI (Holidays API)
- **API Endpoint**: `https://holidays.abstractapi.com/v1/`
- **Purpose**: Retrieve holiday details for specific dates and countries.

---

## Technologies Used
- **Python**: Core programming language for API interaction and data processing.
- **Libraries**: `requests`, `argparse`, `os`, `sys` for handling API calls, command-line arguments, and environment variables.
- **Docker**: Containerization for easy deployment and execution.

---

## Application Features
- Fetches holiday details for a specified country and date.
- Processes and outputs information like holiday name, type, and date.
- Configurable using command-line arguments for flexibility.

---

## Project Structure
```
Exploring_API_Integration/
├── Dockerfile                     # Defines environment for containerization
├── main.py                        # Python script for API interaction and data processing
├── README.md                      # Documentation
```

---

## Setup Instructions
### 1. Obtain an API Key
1. Sign up at AbstractAPI to get your unique API key.
2. Note down the API key for use during application execution.

### 2. Build the Docker Image
1. Navigate to the project directory containing the `Dockerfile` and `main.py`.
2. Build the Docker image:
   ```bash
   docker build -t holidays_api:1.0 .
   ```

### 3. Run the Docker Container
1. Use the following command to run the container with appropriate arguments:
   ```bash
   docker run -e API_KEY=your_api_key holidays_api:1.0 --country US --year 2024 --month 12 --day 25
   ```

---

## Command-Line Arguments
- `--country`: The country code (e.g., `US`, `CO`).
- `--year`: The year for which holiday information is required.
- `--month`: (Optional) The month for the holiday.
- `--day`: (Optional) The day for the holiday.

### Example Commands
1. Retrieve holidays in the US on December 25, 2024:
   ```bash
   docker run -e API_KEY=your_api_key holidays_api:1.0 --country US --year 2024 --month 12 --day 25
   ```

2. Retrieve holidays in Colombia on December 7, 2024:
   ```bash
   docker run -e API_KEY=your_api_key holidays_api:1.0 --country CO --year 2024 --month 12 --day 7
   ```

---

## Example Output
**Command**:
```bash
docker run -e API_KEY=your_api_key holidays_api:1.0 --country CO --year 2024 --month 12 --day 7
```

**Output**:
```
Holiday Details:
Name: Eve of the Feast of the Immaculate Conception
Country: CO
Type: Observance
Date: 12/07/2024
Year: 2024
Month: 12
Day: 7
Weekday: Saturday
```

---

## Notes
- Ensure the API key is set as an environment variable before running the container.
- Multiple holiday entries for the same date may appear if applicable to different regions.

---

## Submission Artifacts
1. `Dockerfile`: Environment setup for containerization.
2. `main.py`: Python script for API interaction and data processing.
3. `README.md`: Project description and usage instructions.

---

## Acknowledgment
This project was completed as part of the CIS 9760 – Big Data Technologies class at Baruch College, demonstrating API integration and containerization with Docker.
