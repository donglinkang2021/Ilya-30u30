with open("origin.html", "r", encoding="utf-8") as f:
    html = f.read()

lines = html.split("\n")

hrefs = []
imgs = []
titles = []
for i, line in enumerate(lines):
    if (i+1)%3 == 0:
        titles.append(line)
    elif (i+1)%3 == 1:
        hrefs.append(line)
    else:
        imgs.append(line)

def download_img(url:str, filename:str):
    import requests
    from pathlib import Path
    Path("images/icons").mkdir(parents=True, exist_ok=True)
    r = requests.get(url)
    filename = f"images/icons/{filename}"
    with open(filename, "wb") as f:
        f.write(r.content)
    print(f"Downloaded {filename}")

def getUrl(html_text:str):
    import re
    pattern = r'src="(.+?)"'
    match = re.search(pattern, html_text)
    if match:
        return match.group(1)
    return None

def href2url(html_text:str):
    import re
    pattern = r'href="(.+?)"'
    match = re.search(pattern, html_text)
    if match:
        return match.group(1)
    return None

# download the favicon of img
img_urls = [getUrl(img) for img in imgs]
# img_url_set = set(img_urls)
# for img_url in img_url_set:
#     filename = img_url.replace("&amp;sz=32", "").split("=")[-1] + ".ico"
#     print(f"Downloading {filename}")
#     download_img(img_url, filename)

def url2icon(url:str) -> str:
    filename = url.replace("&amp;sz=32", "").split("=")[-1] + ".ico"
    return f"images/icons/{filename}"

# map the url to the icon
img_icos = [url2icon(url) for url in img_urls]
href_urls = [href2url(href) for href in hrefs]

markdown = "| Type | Name | Downloaded |\n| :--: | ---- | :--------: |\n"
cnt = 0
for title, img_ico, href_url in zip(titles, img_icos, href_urls):
    print(href_url)
    if cnt < 4:
        type = "Blog"
    elif cnt < 23:
        type = "Paper"
    elif cnt < 26:
        type = "Book"
    else:
        type = "Course"
    is_downloaded = "✅" if type == "Paper" or type == "Book" else "❌"
    markdown += f"| {type} | ![icon]({img_ico}) [{title}]({href_url}) | {is_downloaded} |\n"
    cnt += 1
    
with open("table.md", "w", encoding="utf-8") as f:
    f.write(markdown)
print("Markdown has been saved to table.md")
