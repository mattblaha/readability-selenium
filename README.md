# readability-selenium
Use readability and Selenium to extract the useful text from a web page.

After trying many options, I found that solutions that try to do this without firing up a real web browser fail on too many sites that use lots of JavaScript to load pages. To work on the real web, I needed to just automate a real web browser.

This will inject **[Readability.js](https://github.com/mozilla/readability)** into browser, execute it and fetch the results. It is essentially identical to visiting the page in Firefox and hitting the reader view button in the URL bar.

To run the example, just clone the repo, place your own copy of Readability.js alongside example.py, and run:

    python example.py https://example.com/some/article/

The simplest way I know of to setup a Selenium server that will work with the example is with docker:

    docker run -d -p 4444:4444 -v /dev/shm:/dev/shm selenium/standalone-firefox:3.141.59-radium