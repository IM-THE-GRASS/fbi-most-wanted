import reflex as rx
import requests
import threading
from rxconfig import config


class State(rx.State):
    people:list[dict[str,str]] = []
    def get_people(page=1):
        response = requests.get(
            "https://api.fbi.gov/wanted/v1/list", 
            params={
                "page":page
            }          
        )
        data = response.json()["items"]
        for person in data:
            new_person = {}
            if person["title"]:
                new_person["name"] = person["title"].lower().title()
            if person["images"]:
                new_person["img"] = person["images"][0]["large"]
            new_person["dsc"] = person["caution"]
            if person["race"]:
                new_person["race"] = person["race"].title()
            new_person["description"] = person["description"]
            # if person["height_min"]:
            #     try:
            #         person["height_min"] = str(person["height_min"])
            #         new_person["height"] = person["height_min"][0] + "'" + person["height_min"][2]
            #     except:pass 
            if new_person["dsc"]:
                print("yes")
                return new_person
    for i in range(5):
        persons:dict = get_people(i)
        if persons:
            print("DOUBLE YES")
            people.append(persons)
def card(info):
    return rx.center(
        
        rx.card(
            rx.vstack(
                rx.image(
                    height="420px",
                    object_fit="cover",
                    src=info["img"]
                ),
                rx.hstack(
                    # rx.image(
                    #     src="https://cloud-l3qxq1qyh-hack-club-bot.vercel.app/0male_1.png",
                    #     width="21px",
                    #     height="21px",
                    #     margin_right="11px"
                    # ),
                    rx.text(
                        info["height"],
                        font_size="24px",
                        margin_right="11px"
                    ),
                    rx.text(
                        info["race"],
                        font_size="24px",
                        margin_right="11px"
                    ),
                    width="100%",
                    height="26px",
                    margin_top="16px",  
                    padding="2px"
                ),
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
                            # font_sise = "14px",
                            # font_weight="400",
                            # margin_top="8px"
                            
                        ),
                        
                        
                        spacing="0",
                        margin_top="16px",
                        
                        
                    ),  
                    width="100%",
                    height="224px",
                    margin_top="16px"
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
# @rx.page(on_load=State.on_load)
def index() -> rx.Component:
    return rx.vstack(
        # rx.moment(
        #     format="",
        #     interval=100,
        #     on_change=State.on_update,
        #     display="none"  
        # ),
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
