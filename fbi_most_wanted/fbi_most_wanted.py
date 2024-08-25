"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config


class State(rx.State):
    """The app state."""

    ...
def card():
    return rx.center(
        rx.card(
            rx.vstack(
                rx.image(
                    height="420px",
                    object_fit="cover",
                    src="https://cloud-j01975nem-hack-club-bot.vercel.app/0theguy.png"
                ),
                rx.hstack(
                    rx.image(
                        src="https://cloud-l3qxq1qyh-hack-club-bot.vercel.app/0male_1.png",
                        width="21px",
                        height="21px"
                    ),
                    width="100%",
                    height="26px",
                    margin_top="16px",  
                    padding="2px"
                ),
                rx.vstack(
                    
                    rx.text(
                        "EFRAIN VASQUEZ-YANEZ",
                        font_size="24px",
                          
                    ),
                    rx.text(
                        "The FBI is offering a reward of up to $20,000 for information leading to the arrest of Efrain Vasquez-Yanez",
                        font_size="16px",
                        font_weight="bolder",
                        line_height="22.4px",
                        margin_top="8px"
                    ),
                    rx.text(
                        "Vasquez-Yanez is a known member of the Mara Salvatrucha (MS-13) gang with ties to El Salvador. He speaks both English and Spanish, although Spanish is his primary language. He was last seen in July of 2016, in Everett, Massachusetts",
                        font_sise = "14px",
                        font_weight="400",
                        margin_top="8px"
                          
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
        height="100%"
    ),

def index() -> rx.Component:
    # Welcome Page (Index)
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
        rx.hstack(
            card(),
            card(),
            card(),
            
            spacing="0",
            width="100vw",
            height="890px",
            padding_right="78px",
            padding_left="78px"
        )
    )


app = rx.App()
app.add_page(index)
