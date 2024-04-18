# Setup

1. Head over to the [Google API Console](https://console.cloud.google.com/apis/dashboard).
2. Create a new project by selecting My Project -> + button
3. Search for 'Google Drive API', enable it.
4. Head over to 'Credentials' (sidebar), click 'Create Credentials' -> 'Service Account Key'
   ![image](https://github.com/dimverrr/spendbase_test/assets/118119126/6881cfff-2da6-42a7-8238-e55f4eb016dc)
5. Click on created credentials, click 'Keys' button, then 'Add Key' button, choose 'JSON' and save it
   ![image](https://github.com/dimverrr/spendbase_test/assets/118119126/7b92b6de-a6a3-45bf-837e-cc432d2e6d0e)
8. Create new Google Sheet.
9. Open up the JSON file, copy your spreadsheet with the "XXX-compute@developer.gserviceaccount.com", open your spreadshhet and add this email as editor.
10. Save the JSON file where you're hosting project.
11. Create .env file with variables as in .env.example file. Paste there your spreadsheet name and path to your JSON file.
   
# How script works

Run this command to write data to your spreadsheet

```python 
  scrapy crawl people_spider -o your_name_for_json.json -o your_name_for_csv.csv
```

## Get JSON and CSV files

To additionally obtain json and csv files you should run the following command:

```python
  scrapy crawl people_spider -o your_name_for_json.json -o your_name_for_csv.csv
```

# Tools used

Scrapy (for retriving data from the website), pygsheets (for interacting with spreadsheets), pandas (for creating DataFrame).

