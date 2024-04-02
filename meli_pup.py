import asyncio

from bs4 import BeautifulSoup
from pyppeteer import launch


async def get_html(url):
    browser = await launch()
    page = await browser.newPage()
    await page.goto(url)

    # Clicking on the button to filter by 5-star ratings
    await page.click('button[id=":Ronah:"]')
    print("Clicked on the button to filter by 5-star ratings")
    await page.waitForSelector('li[data-testid="filterItem-rating-1"]')
    print("Waited for the 5-star ratings filter to appear")
    await page.click('li[data-testid="filterItem-rating-1"]')
    print("Clicked on the 5-star ratings filter")

    # Wait for the page to load after filtering
    await page.waitForNavigation()

    # Get the HTML content
    html = await page.content()

    await browser.close()
    return html


def get_comments(html):
    soup = BeautifulSoup(html, "html.parser")
    comments = []
    for p in soup.find_all(
        "p", class_="ui-review-capability__summary__plain_text__summary_container"
    ):
        comments.append(p.text.strip())
    return comments


if __name__ == "__main__":
    url = "https://articulo.mercadolibre.com.mx/noindex/catalog/reviews/MLM1385142136?noIndex=true&access=view_all&modal=true"
    html = asyncio.get_event_loop().run_until_complete(get_html(url))
    comments = get_comments(html)

    print("-" * 50)
    print("Comments:")
    for comment in comments:
        print(comment)
    print("-" * 50)
