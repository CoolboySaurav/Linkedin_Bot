# LinkedIn Scraping Bot

## Project Description
The LinkedIn Scraping Bot is a Python script that automates the process of scraping recruiter profile URLs from LinkedIn search results. It uses Selenium to navigate through LinkedIn's search pages, extract recruiter profile URLs, and store them for further analysis or networking purposes.

## Installation
1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/<username>/<repository>.git

cd <repository>

pip install -r requirements.txt

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt

3. Download the appropriate WebDriver for your browser:
    - Chrome: https://sites.google.com/a/chromium.org/chromedriver/downloads
    - Firefox:
        - GeckoDriver:  
        
4. Update the `config.py` file with your LinkedIn credentials and the path to the WebDriver executable.

## Usage
Run the script using the following command:
```bash 
python linkedin_bot.py

The script will prompt you to enter the search query and the number of pages to scrape. It will then navigate through the search results, extract the recruiter profile URLs, and store them in a text file.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Replace `<username>` and `<repository>` with your GitHub username and repository name respectively. You can customize the sections as needed to provide more detailed instructions or information about your project. If you have any specific requirements or need further assistance, feel free to ask!


## Acknowledgements
- [Selenium](https://www.selenium.dev/)
- [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/)
- [LinkedIn](https://www.linkedin.com/)
- [Python](https://www.python.org/)
