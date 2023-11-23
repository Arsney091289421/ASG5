# ASG5
# YouTube Channel Analysis

This repository contains Python scripts for analyzing YouTube channel data. The primary focus is to calculate and explore the distribution of different types of YouTube channels and export the output to a csv file and enter it into the sql database.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

To run the scripts, ensure you have the following Python packages installed:
- pymysql
- pandas
- sqlalchemy

## Installing

To set up your development environment, follow these steps:

1. Clone the repository to your local machine.
2. Install the necessary Python packages using the provided `requirements.txt`.

   ```bash
   pip install -r requirements.txt

3. Modify the `YouTube Channel Analysis.py` script with your database credentials (ensure they are not the actual credentials when you push to GitHub).

4. Run the script to process the data:

   ```bash
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
1.Pandas - Data manipulation and CSV file handling.

2.SQLAlchemy - Database interaction.

3.PyMySQL - A MySQL database client for Python, used for database connections.

## Authors

* **[Arsney091289421]** - *Initial work* - [YourGitHub](https://github.com/Arsney091289421)

## License

This project is licensed under the MIT License - see the LICENSE.md file for details

## Acknowledgments

* Special thanks to the developers of [Pandas](https://pandas.pydata.org/) and [SQLAlchemy](https://www.sqlalchemy.org/) for providing the powerful libraries that support this project.
* Grateful acknowledgment to professor Omar for guidance in conceptualizing and implementing the project.
* Appreciation to all the developers who answered related queries on forums, whose solutions greatly assisted in overcoming programming challenges.

