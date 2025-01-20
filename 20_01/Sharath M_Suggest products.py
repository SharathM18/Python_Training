class ecommerce:
    def __init__(self):
        self._database = {
            'red tshirt': 'cloth',
            'trending tshirt': 'cloth',
            'branded tshirt': 'cloth',
            'cotton tshirt': 'cloth',
            'dr. set': 'toy',
            'kitchen set': 'toy',
            'teddy': 'toy',
            'unicorn':'toy',
            'fishing':'toy',
            'chair': 'furniture',
            'table': 'furniture',
            'sofa': 'furniture'
        }
        self._suggest_prod_list = []

    def prod_suggestion(self):

        prod_name = input('Search: ').lower()

        if prod_name in self._database:
            print(f'Item name: {prod_name}')

            print('Suggested items for you:')

            for product_name, category in self._database.items():
                if  self._database[prod_name] == category:
                    self._suggest_prod_list.append(product_name)


            for i in self._suggest_prod_list:
                if prod_name == i:
                    continue
                print(i)
        else:
            print('No matching item found.')

ecommerce().prod_suggestion()