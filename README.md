# ASG5
# YouTube Channel Analysis

This repository contains Python scripts for analyzing YouTube channel data. The primary focus is to calculate and explore the distribution of different types of YouTube channels.

## Getting Started

These instructions will guide you in setting up the project locally for development and testing.

### Prerequisites

To run the scripts, ensure you have the following Python packages installed:
- pymysql
- pandas
- sqlalchemy

## Installing
To set up your development environment, follow these steps:

Clone the repository to your local machine.
Install the necessary Python packages using the provided requirements.txt.
Modify the YouTube Channel Analysis.py script with your database credentials (ensure they are not the actual credentials when you push to GitHub).
Run the script to process the data:
python "YouTube Channel Analysis.py"

## Running the Scripts

The main script performs the following tasks:
1. Loads a dataset from a CSV file (`youtube_dataset.csv`).
2. Calculates the distribution of channel types within the dataset.
3. Selects and processes the top 1000 records.
4. Saves the processed data to a new CSV file (`top_1000_channels.csv`).
5. Connects to a MySQL database and uploads the data.

### Important Notes

- The script contains database connection details. Ensure to replace these with your actual database credentials.
- The dataset `youtube_dataset.csv` should be present in the same directory as the script.

## Deployment

The script is designed for a local development environment. For deployment, additional configuration may be required depending on your setup.

## Built With
Pandas - Data manipulation and CSV file handling.
SQLAlchemy - Database interaction.

## Authors

* **[Arsney091289421]** - *Initial work* - [YourGitHub](https://github.com/Arsney091289421)

## License

This project is licensed under the MIT License - see the LICENSE.md file for details

## Acknowledgments

* Hat tip to Durham College and professor Omar

