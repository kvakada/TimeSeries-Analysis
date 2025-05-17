# 🧠 Time Series Analysis of Bitcoin Prices Using s3fs

**Author:** Karthik Vakada  
**Email:** kvakada@umd.edu  
**Project Tag:** TutorTask114_Spring2025_Time_Series_Analysis_of_Bitcoin_Prices_Using_s3fs  
**Date:** May 2025

---

## 📁 Project Structure

```

TutorTask114\_Spring2025\_Time\_Series\_Analysis\_of\_Bitcoin\_Prices\_Using\_s3fs/
├── bitcoin\_utils.py                         <- Utility functions to fetch data via CoinGecko API
├── Spring2025\_s3fs.API.ipynb                <- Notebook: s3fs usage and native API interaction
├── Spring2025\_s3fs.API.md                   <- Markdown description of the s3fs API usage
├── Spring2025\_s3fs.API.py                   <- Python script version of the s3fs API notebook ✅
├── Spring2025\_s3fs.example.ipynb            <- Main notebook: analysis, forecasting, and S3 integration
├── Spring2025\_s3fs.example.md               <- Summary of project methodology and results
├── Spring2025\_s3fs.example.py               <- Python script version of the example notebook ✅
├── requirements.txt                         <- Standard pip dependencies
├── pyproject.toml                           <- Poetry-based dependency manager ✅
├── Dockerfile                               <- Docker build configuration
├── start.sh                                 <- Script to build and launch Docker
├── bitcoin\_prices.csv                       <- Sample fetched data
├── bitcoin\_prices\_with\_forecast.csv         <- Forecast output file
├── bitcoin\_prices\_with\_anomalies.csv        <- Anomaly detection output file (if generated)
├── dev\_scripts\_tutorial\_s3fs/               <- Boilerplate folder for tutorial compliance ✅
│   └── README.md                             <- Placeholder explaining purpose

````

---

## ⚙️ Setup and Dependencies

### Core Dependencies
- **Python 3.10+**
- `pandas`, `matplotlib`, `statsmodels`, `scikit-learn`
- `s3fs`, `requests`
- `Jupyter` for notebooks
- `Docker` for environment reproducibility

📌 Install via `requirements.txt` or `pyproject.toml`

---

## 🐳 Docker Setup (Recommended)

```bash
# Build the container
docker build -t bitcoin-s3fs .

# Run with AWS credentials mounted
docker run -it -p 8888:8888 -v $(pwd):/app -v ~/.aws:/root/.aws bitcoin-s3fs
````

Then open: `http://localhost:8888` in your browser.

---

## 🧪 Jupyter Notebooks Overview

### 🔹 Native S3 API (`Spring2025_s3fs.API.*`)

* Mounts and accesses AWS S3 using `s3fs`
* Reads/writes `.csv` files directly from/to S3
* Abstracts `boto3` for simplicity

### 🔹 Main Analysis (`Spring2025_s3fs.example.*`)

* Fetches Bitcoin prices via `bitcoin_utils.py`
* Plots daily price trends and moving averages
* Performs ARIMA forecasting (optional)
* Detects anomalies (Z-score method)
* Uploads cleaned and forecasted data back to S3

---

## 🌐 Local Environment Setup

```bash
# (Optional) Virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

or if using Poetry:

```bash
poetry install
```

---

## 📊 Visual Output

* ✅ Time series plots with 30-day moving average
* 🔮 ARIMA-based price forecasts
* 🚨 Anomaly detection using Z-scores
* ☁️ Real-time S3 uploads (verified using `s3fs`)

---

## 🔐 API Key Configuration

In `bitcoin_utils.py`, the function `fetch_bitcoin_data(api_key, days)` fetches CoinGecko data.
Avoid hardcoding the API key. Use `.env` or environment variables in production setups.

---

## 💡 Suggested Improvements (Stretch Goals)

* Add Facebook Prophet or LSTM models for improved forecasting
* Build a Plotly Dash or Flask UI to serve the outputs
* Monitor Bitcoin price in real-time and push updates to S3

---

## ✅ Final Notes

This project was developed for **DATA605 – Spring 2025** at UMD using Causify AI’s project structure. It combines:

* Time series modeling
* Cloud data management
* Reproducible deployment

📫 For queries, reach out: **[kvakada@umd.edu](mailto:kvakada@umd.edu)**
