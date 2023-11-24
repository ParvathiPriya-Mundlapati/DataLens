# DataLens
DataLens is a simple, yet effective web application designed for performing basic data quality checks on CSV files. Users can upload a file, and the application will analyze it for common data issues such as missing values, duplicates, and provide a basic statistical overview.

## Features

- **File Upload**: Users can upload CSV files for analysis.
- **Data Quality Checks**: Automated checks for missing values, duplicates, and basic statistical summaries.
- **User-friendly Results Display**: Results are displayed on a web page in an easy-to-read format.

## Technologies

- **Python**: The core programming language used.
- **Flask**: A lightweight WSGI web application framework.
- **Pandas**: A Python library used for data manipulation and analysis.
- **HTML/CSS**: Used for designing the user interface.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Before you begin, ensure you have the following installed:
- Python (Version 3.x)
- Flask
- Pandas

You can install Flask and Pandas using pip:
```
pip install Flask
pip install pandas
```

### Installation

1. **Clone the repository:**
   ```
   git clone [repository-url]
   ```
   Replace `[repository-url]` with the URL of this repository.

2. **Navigate to the project directory:**
   ```
   cd DataLens
   ```

3. **Start the Flask server:**
   ```
   python app.py
   ```

4. **Access the application:**
   - Open your web browser and visit `http://127.0.0.1:5000/`.

### Usage

1. **Upload a CSV File:**
   - On the home page, click 'Choose File' and select a CSV file from your computer.
   - Click 'Upload' to submit the file for analysis.

2. **View Results:**
   - After uploading the file, the results of the data quality checks will be displayed on a new page.
   - The results include counts of missing values, duplicates, and a basic statistical summary.

## Contributing

Please read [CONTRIBUTING.md] for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

- **Parvathi Priya** - *Initial work*

## License

This project is licensed under the MIT License - see the [LICENSE.md] file for details.
