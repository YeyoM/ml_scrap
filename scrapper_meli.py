import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver


def get_html(url):
    browser = webdriver.Firefox()
    browser.get(url)

    browser.implicitly_wait(10)

    scroll_amount = 2000
    current_height = browser.execute_script("return document.body.scrollHeight")

    max_counter = 0

    while True:
        browser.execute_script(f"window.scrollTo(0, {current_height});")
        browser.execute_script(f"window.scrollTo(0, {current_height - scroll_amount});")
        new_height = browser.execute_script("return document.body.scrollHeight")
        if new_height >= 20000:
            break
        current_height = new_height
        max_counter += 1
        if max_counter >= 5000:
            break
    html = browser.page_source
    browser.quit()
    return html


def get_comments(html):
    soup = BeautifulSoup(html, "html.parser")
    articles = soup.find_all("article", class_="ui-review-capability-comments__comment")

    data = []

    for article in articles:
        rating_div = article.find(
            "div", class_="ui-review-capability-comments__comment__rating"
        )
        rating = rating_div.find("p", class_="andes-visually-hidden")
        rating_info = rating.text.strip()

        comment = article.find(
            "p", class_="ui-review-capability-comments__comment__content"
        ).text.strip()

        rating_info = rating_info.split(" ")[1]

        if int(rating_info) < 3:
            rating_info = 0
        else:
            rating_info = 1

        data.append((rating_info, comment))

    return data


if __name__ == "__main__":
    urls = [
        "https://www.mercadolibre.com.mx/noindex/catalog/reviews/MLM19671372?noIndex=true&access=view_all&modal=true&controlled=true",
        "https://articulo.mercadolibre.com.mx/noindex/catalog/reviews/MLM1385142136?noIndex=true&access=view_all&modal=true",
        "https://articulo.mercadolibre.com.mx/noindex/catalog/reviews/MLM1453562130?noIndex=true&access=view_all&modal=true",
        "https://articulo.mercadolibre.com.mx/noindex/catalog/reviews/MLM1310553268?noIndex=true&access=view_all&modal=true",
        "https://articulo.mercadolibre.com.mx/noindex/catalog/reviews/MLM1529227728?noIndex=true&access=view_all&modal=true",
        "https://articulo.mercadolibre.com.mx/noindex/catalog/reviews/MLM2413812916?noIndex=true&access=view_all&modal=true",
        "https://articulo.mercadolibre.com.mx/noindex/catalog/reviews/MLM1483602610?noIndex=true&access=view_all&modal=true",
        "https://www.mercadolibre.com.mx/noindex/catalog/reviews/MLM26374823?noIndex=true&access=view_all&modal=true&controlled=true",
        "https://articulo.mercadolibre.com.mx/noindex/catalog/reviews/MLM1595869350?noIndex=true&access=view_all&modal=true",
        "https://articulo.mercadolibre.com.mx/noindex/catalog/reviews/MLM1436939565?noIndex=true&access=view_all&modal=true",
        "https://articulo.mercadolibre.com.mx/noindex/catalog/reviews/MLM1918786987?noIndex=true&access=view_all&modal=true",
        "https://www.mercadolibre.com.mx/noindex/catalog/reviews/MLM23718286?noIndex=true&access=view_all&modal=true&controlled=true",
        "https://www.mercadolibre.com.mx/noindex/catalog/reviews/MLM27953242?noIndex=true&access=view_all&modal=true&controlled=true",
        "https://articulo.mercadolibre.com.mx/noindex/catalog/reviews/MLM1423798166?noIndex=true&access=view_all&modal=true",
        "https://articulo.mercadolibre.com.mx/noindex/catalog/reviews/MLM1458795279?noIndex=true&access=view_all&modal=true",
        "https://www.mercadolibre.com.mx/noindex/catalog/reviews/MLM15567959?noIndex=true&access=view_all&modal=true&controlled=true",
        "https://www.mercadolibre.com.mx/noindex/catalog/reviews/MLM23537280?noIndex=true&access=view_all&modal=true&controlled=true",
        "https://www.mercadolibre.com.mx/noindex/catalog/reviews/MLM25929225?noIndex=true&access=view_all&modal=true&controlled=true",
        "https://www.mercadolibre.com.mx/noindex/catalog/reviews/MLM27144027?noIndex=true&access=view_all&modal=true&controlled=true",
        "https://articulo.mercadolibre.com.mx/noindex/catalog/reviews/MLM1958181837?noIndex=true&access=view_all&modal=true",
        "https://articulo.mercadolibre.com.mx/noindex/catalog/reviews/MLM2041772158?noIndex=true&access=view_all&modal=true",
    ]

    data_list = []

    for url in urls:
        html = get_html(url)
        data = get_comments(html)
        data_list.extend(data)

    print(data_list)
    df = pd.DataFrame(data_list, columns=["rating", "comment"])
    df.to_csv("comments.csv", index=False)
