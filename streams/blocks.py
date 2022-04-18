from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

class TitleBlock(blocks.StructBlock):
    text = blocks.CharBlock(
        required=True,
        help_text='Text to diplay',
    )

    class Meta:
        template = "streams/title_block.html"
        icon = "edit"
        label = "Title"
        help_text = "Centered text to display on the page"



class CardsBlock(blocks.StructBlock):
    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("title", blocks.CharBlock(max_length=100, help_text="Bold title text for this card. Max lenth 100 characters.")),
                ("text", blocks.TextBlock(max_length=255, help_text="Optional text for this card. Max length is 255 characters.", required=False)),
                ("image", ImageChooserBlock(help_text="Image will be automatically cropped to 570px x 370px.")),
            ]
        )
    )

    class Meta:
        template = "streams/cards_block.html"
        icon = "image"
        label = "Standard Cards"

