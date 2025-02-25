class Restaurant:
    def __init__(self, name, menu):
        self.name = name
        self.menu = menu

    def __str__(self):
        return f"Restaurant: {self.name}, Menu: {self.menu}"

class Order:
    def __init__(self, restaurant_name, items):
        self.restaurant_name = restaurant_name
        self.items = items

    def __str__(self):
        return f"Order from {self.restaurant_name}: {self.items}"

class FoodDeliveryApp:
    def __init__(self):
        self.restaurants = []
        self.orders = []

    def add_restaurant(self, name, menu):
        restaurant = Restaurant(name, menu)
        self.restaurants.append(restaurant)

    def view_restaurants(self):
        if not self.restaurants:
            print("No restaurants available.")
            return
        for restaurant in self.restaurants:
            print(restaurant)

    def place_order(self, restaurant_name, items):
        order = Order(restaurant_name, items)
        self.orders.append(order)

    def view_orders(self):
        if not self.orders:
            print("No orders placed.")
            return
        for order in self.orders:
            print(order)

# Example usage
if __name__ == "__main__":
    app = FoodDeliveryApp()
    app.add_restaurant("Pizza Place", {"Margherita": 8.5, "Pepperoni": 9.5})
    app.add_restaurant("Burger Joint", {"Cheeseburger": 7.0, "Veggie Burger": 6.5})

    print("Available Restaurants:")
    app.view_restaurants()

    print("\nPlacing an order...")
    app.place_order("Pizza Place", {"Margherita": 2, "Pepperoni": 1})

    print("\nCurrent Orders:")
    app.view_orders()