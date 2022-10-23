import justpy as jp

class Documentation():
    path = "/documentation"

    @classmethod
    def serve(cls, req):
        wp = jp.WebPage()

        div = jp.Div(a=wp, classes="bg-gray-200 h-screen")
        jp.Div(a=div, text="Instant Dictionary API Documentation", classes="text-4xl m-2")
        jp.Div(a=div, text="Get definitions of words:", classes="text-lg")
        jp.Hr(a=div)
        jp.Div(a=div, text="www.example.com/api?w=moon")
        jp.Div(a=div, text="""
        {
          "word": "moon",
          "definition": [
            "A natural satellite of a planet.",
            "A month, particularly a lunar month (approximately 28 days).",
            "To fuss over adoringly or with great affection.",
            "Deliberately show ones bare ass (usually to an audience, or at a place, where this is not expected or deemed appropriate).",
            "To be lost in phantasies or be carried away by some internal vision, having temorarily lost (part of) contact to reality."
          ]
        }
        """)

        return wp
