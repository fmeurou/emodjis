from django_unicorn.components import UnicornView


class SearchView(UnicornView):
    search = ""

    def updated_search(self, query):
        print("updated_search", query)
        self.parent.load_emojis(search=query)
