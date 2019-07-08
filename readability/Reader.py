from time import sleep
import html2text


class Reader:

  def __init__(self,driver,readability_js=None):
    self.driver = driver


    if (readability_js):
      self.script = readability_js
    else:
      self.script = open("Readability.js").read()

    self.script += """
    var documentClone = document.cloneNode(true);
    var article = new Readability(documentClone).parse();
    return article.content;
    """

  def __del__(self):
    self.driver.quit()

  def get_url(self,url):
    self.driver.get(url)
    sleep(3)
    content = self.driver.execute_script(self.script)
    return html2text.html2text(content)

