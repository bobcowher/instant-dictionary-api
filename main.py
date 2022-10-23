import justpy as jp
import definition
import json

class Api:

    @classmethod
    def serve(cls, req):
        wp = jp.WebPage()
        word = req.query_params.get('w')
        definition_instance = definition.Definition(term=word)
        dictionary_definition = definition_instance.get()

        response = {
            "word":word,
            "definition":dictionary_definition
        }

        wp.html = json.dumps(response)

        return wp

jp.Route("/", Api.serve)
jp.justpy()