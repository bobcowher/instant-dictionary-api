import justpy as jp
import definition

class Api:

    @classmethod
    def serve(cls, req):
        wp = jp.WebPage()
        word = req.query_params.get('w')
        definition_instance = definition.Definition(term=word)
        dictionary_definition = definition_instance.get()
        print(dictionary_definition)
        jp.Div(a=wp, text=dictionary_definition)

        return wp

