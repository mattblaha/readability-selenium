import time

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
    return [article.textContent, article.byline];
    """

  def get_readable_dict(self,url):
    start = time.perf_counter()
    self.driver.get(url)
    time.sleep(3)
    script_result = self.driver.execute_script(self.script)
    content = script_result[0]
    byline  = script_result[1] if script_result[1] else "Unknown"
    end = time.perf_counter()
    return {'content': content, 'byline':byline,
        'time': end - start}

  def get_readable(self,url):
    return self.get_readable_dict(url)['content']

  # just an alias for compatibility, accidental change broke tests
  get_url = get_readable
