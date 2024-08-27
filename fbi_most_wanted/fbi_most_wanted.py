import reflex as rx
import requests
from rxconfig import config

class State(rx.State):
    people: list[dict[str, str]] = []

    def get_people(self):
        response = requests.get("https://api.fbi.gov/wanted/v1/list")
        data = response.json()["items"]
        for person in data:
            new_person = {}
            new_person["name"] = person["title"]
            new_person["img"] = person["images"][0]["large"]
            new_person["dsc"] = person["caution"]
            new_person["race"] = person["race"]
            new_person["description"] = person["description"]
            self.people.append(new_person)
        print(self.people)

def card(info):
    return rx.center(
        rx.card(
            rx.vstack(
                rx.center(
                    rx.image(
                        height="45.7vh",
                        object_fit="cover",
                        src=info["img"]
                    ),
                    height="45.7vh",
                    width="20.86vw"
                    
                ),
                rx.vstack(
                    rx.scroll_area(
                        rx.vstack(
                            rx.text(
                                info["name"],
                                font_size="2.5vh",
                                line_height="2.7vh"
                            ),
                            rx.text(
                                info["description"],
                                font_size="2.5vh",
                                font_weight="bolder",
                                line_height="3vh",
                                margin_top="0.87vh"
                            ),
                            rx.html(
                                info["dsc"],
                            ),
                            spacing="0",
                            margin_top="1.74vh",
                        )
                    ),
                    width="100%",
                    height="24.37vh",
                    spacing="0",
                    margin_top="1.74vh",
                ),
                spacing="0"
            ),
            padding="1.74vh",
            width="22.6vw",
            height="79.87vh",
        ),
        margin_right="4.06vw",
        margin_left="4.06vw",
        height="100%",
        margin_top="1.74vh",
        margin_bottom="1.74vh"
    )

@rx.page(on_load=State.get_people)
def index() -> rx.Component:
    return rx.vstack(
        rx.box(
            rx.image(
                src="https://cloud-6nswpw11z-hack-club-bot.vercel.app/0screenshot_2024-08-23_124044_1.png",
                width="56.46vw",
                height="20.35vh"
            ),
            bg="#B62244",
            width="100vw",
            height="20.35vh"
        ),
        rx.grid(
            rx.foreach(
                State.people,
                card
            ),
            margin_top="0.87vh",
            columns="3",
            width="100vw",
            padding_right="4.06vw",
            padding_left="4.06vw"
        )
    )

app = rx.App()
app.add_page(index)