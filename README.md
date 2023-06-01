# vlr-user-posts-scraper

Simple python script to scrape user names and their respective number of posts on vlr.gg.
In documentation, samples refers to the number of forum pages searched starting from the
first after being sorted by "top" "all-time" on the vlr.gg forums page.

Usage: 
1. Load notebook into google colab - https://colab.research.google.com/ - or run locally if your 
device is fast enough.

2. Run the first block of code to initialize functions etc. If you are running locally, you may
need to install python packages "lxml", "beatifulsoup4", and "requests". You can do so with the 
following commands: 

"pip3 install bs4"
"pip3 install requests"
"pip3 install lxml"

3. Run the second block of code, enter a sample count - 10 samples took 1500 seconds to run on 
colab - and wait!

4. Results will be printed to the terminal.
