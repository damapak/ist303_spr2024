# Illustrate multi-threaded execution using concurrent.futures library
# Visit 3 wikipedia pages using requests lib, dl content and save as .txt files

import requests
from concurrent.futures import ThreadPoolExecutor

urls = ["https://en.wikipedia.org/wiki/Solar_System",
        "https://en.wikipedia.org/wiki/Sun",
        "https://en.wikipedia.org/wiki/Plasma_(physics)"]

def multithread():
  
  def url_download(url):
    page = requests.get(url)
    html_content = page.text
    html_content.encode('utf-8')
    out_filename = url.split("wiki/")[1] + ".txt"
    print(f'output filename: {out_filename}')
    with open(out_filename, 'wt', encoding='utf-8') as fileobj:
      fileobj.write(html_content)

  # configure the TPE to loop through urls concurrently
  with ThreadPoolExecutor() as executor:
    executor.map(url_download, urls)

# use name == main idiom to execute the following when run directly (not imported)
if __name__ == "__main__":
  multithread()