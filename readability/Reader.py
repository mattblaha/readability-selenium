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
    return [article.content, article.byline];
    """

  def __del__(self):
    self.driver.quit()

  def get_url_dict(self,url):
    self.driver.get(url)
    sleep(3)
    content = html2text.html2text(self.driver.execute_script(self.script)[0])
    byline  = html2text.html2text(self.driver.execute_script(self.script)[1])
    return {'content': content, 'byline':byline}

  def get_url(self,url):
    return self.get_url_dict(url)['content']

