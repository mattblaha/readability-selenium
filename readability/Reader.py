import time
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

  def get_readable_dict(self,url):
    start = time.perf_counter()
    self.driver.get(url)
    time.sleep(3)
    script_result = self.driver.execute_script(self.script)
    content = html2text.html2text(script_result[0])
    try:
        byline  = html2text.html2text(script_result[1]).rstrip()
    except:
        byline = "Unknown"
    end = time.perf_counter()
    return {'content': content, 'byline':byline,
        'time': end - start}

  def get_readable(self,url):
    return self.get_readable_dict(url)['content']

  get_url = get_readable
