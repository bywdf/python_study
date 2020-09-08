class Restaurant():
    """describe restaurant"""

    def __init__(self, restaurant_name, cuising_type):
        '''init'''
        self.restaurant_name = restaurant_name
        self.cuising_type = cuising_type
        self.number_served = 0

    def describe_restaurant(self):
        print(self.restaurant_name + "接待了" + str(self.number_served)+ "人")

    def open_restaurant(self):
        print('酒店正在营业！')

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self,number_day):
        self.number_served += number_day

# restaurant_1 = Restaurant("夏日酒店", "五星级")
# restaurant_1.increment_number_served(15)
# restaurant_1.increment_number_served(15)
# restaurant_1.describe_restaurant()



class  IceCreamStand(Restaurant):
    ''''''

    def __init__(self, restaurant_name, cuising_type):
        super().__init__(restaurant_name, cuising_type)
        self.flavors = ['奶油', '芝士', '草莓']
    
    def show_icecream(self):
        for i in self.flavors:
            print(i)

# icecream_1 = IceCreamStand('夏日酒店', 'wuxing')
# icecream_1.describe_restaurant()
# icecream_1.show_icecream()
