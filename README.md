# ETL Pipeline (AWS Ready)

This project demonstrates a basic ETL (Extract, Transform, Load) pipeline using Python and pandas. It reads raw CSV files, transforms the data by cleaning and merging, and loads the final dataset into a local or cloud-based PostgreSQL database.

## Features

- Modular scripts: `extract.py`, `transform.py`, and `load.py`
- Designed for large CSV ingestion
- Clean and reusable code structure
- Easily extendable to AWS using:
  - Amazon S3 for storage
  - Amazon EC2 for compute
  - Amazon RDS for database

## Tech Stack

- Python 3
- Pandas
- SQLAlchemy
- PostgreSQL (optional, for loading stage)

## Project Structure

```bash
data/
  ├── raw/          # Input CSVs
  └── processed/    # Cleaned output
scripts/
  ├── extract.py
  ├── transform.py
  └── load.py
