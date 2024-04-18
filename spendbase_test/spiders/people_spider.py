import scrapy
import pygsheets
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

class RealtySpider(scrapy.Spider):
    name = "people_spider"
    start_urls = ["https://interaction24.ixda.org/"]
    data_list = []

    def parse(self, response):
        PEOPLE_SELECTOR = ".speakers-list_item-wrapper"
        NAME_SELECTOR = ".speakers-list_item-heading" + "::text"
        ROLE_SELECTOR = ".margin-bottom.margin-small div:nth-child(2)" + "::text"
        IMG_SELECTOR = ".image-absolute"
        SOCIAL_MEDIA = ".speakers-list_social-link" + "::attr(href)"

        people = response.css(PEOPLE_SELECTOR)[3::]

        for person in people:
            links = person.css(SOCIAL_MEDIA).getall()
            linkedin = links[0] if links and links[0] != "index.html#" else None
            twitter = links[1] if links and links[1] != "index.html#" else None
            personal_website = links[3] if links and links[3] != "index.html#" else None

            data = {
                "name": person.css(NAME_SELECTOR).get(),
                "role": person.css(ROLE_SELECTOR).get(),
                "img": person.css(IMG_SELECTOR).attrib["src"][3:],
                "linkedin": linkedin,
                "twitter": twitter,
                "personal_website": personal_website,
            }
            
            yield data

            self.data_list.append(data)

        self.write_data(self.data_list)

    def write_data(self, data_list):

        gc = pygsheets.authorize(service_file=os.getenv("PATH_TO_CREDENTIALS_FILE"))

        df = pd.DataFrame(data_list)

        sh = gc.open(os.getenv("SPREADSHEET_NAME"))

        wks = sh[0]

        wks.set_dataframe(df, (1, 1))
