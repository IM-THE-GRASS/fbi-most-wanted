import reflex as rx
import requests

from rxconfig import config


class State(rx.State):
    people:list[dict[str,str]] = []
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
                rx.image(
                    height="420px",
                    object_fit="cover",
                    src=info["img"]
                ),
                rx.vstack(
                    rx.scroll_area(
                        rx.vstack(
                            
                            rx.text(
                                info["name"],
                                font_size="24px",
                                
                            ),
                            rx.text(
                                info["description"],
                                font_size="16px",
                                font_weight="bolder",
                                line_height="22.4px",
                                margin_top="8px"
                            ),
                            rx.html(
                                info["dsc"],
                                
                            ),
                            spacing="0",
                            margin_top="16px",
                            
                        )
                    ),
                    
                    
                    width="100%",
                    height="224px",
                    spacing="0",
                    margin_top="16px",
                    
                      
                ),
                spacing="0"
            ),
            
            padding="16px",
            width="434px",
            height="734px",
            
        ),
        margin_right="78px",
        margin_left="78px",
        height="100%",
        margin_top="16px",
        margin_bottom="16px"
    )
@rx.page(on_load=State.get_people)
def index() -> rx.Component:
    return rx.vstack(
        rx.box(
            rx.image(
                src="https://cloud-6nswpw11z-hack-club-bot.vercel.app/0screenshot_2024-08-23_124044_1.png",
                width="1084px",
                height="187px"
            ),
            bg="#B62244",
            width="100vw",
            height="187px"
        ),
        rx.grid(
            rx.foreach(
                State.people,
                card
            ),
            margin_top="8px",
            columns="3",
            width="100vw",
            padding_right="78px",
            
            padding_left="78px"
        )
    )


app = rx.App()
app.add_page(index)
