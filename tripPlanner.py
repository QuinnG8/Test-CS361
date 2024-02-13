# Itinerary Service
class ItineraryService:
    def create_itinerary(self, name, itinerary_details):
        # Create a new itinerary for the user
        pass
    def update_itinerary(self, name, itinerary_id, updated_details):
        # Update an existing itinerary
        pass
    def get_itinerary(self, name, itinerary_id):
        # Retrieve itinerary details for a user
        pass

# Budget Service
class BudgetService:
    def suggest_accommodations(self, destination, budget):
        # Suggest cost-effective accommodations based on budget and destination
        pass
    def suggest_activities(self, destination, budget):
        # Suggest cost-effective activities based on budget and destination
        pass
    def set_budget(self, name, budget_amount):
        # Set the budget for a user's trip
        pass
    def get_budget(self, name):
        # Get the budget for a user's trip
        pass

# Trip Recording Service
class TripRecordingService:
    def record_trip_details(self, name, trip_details):
        # Store trip details including ratings, favorite and least favorite items, memories, etc.
        print("Recording trip details...")
        print(f"User ID: {name}")
        print("Trip Details:")
        for key, value in trip_details.items():
            print(f"{key.capitalize()}: {value}")
        print("Trip details recorded successfully!")
        pass
    def store_trip_record(self, name, trip_details):
        pass
    def retrieve_trip_record(self, name, trip_id):
        # Retrieve trip details for a user
        pass

# Text-based UI
class TextUI:
    def __init__(self):
        self.itinerary_service = ItineraryService()
        self.budget_service = BudgetService()
        self.trip_recording_service = TripRecordingService()

    def start(self):
        print("Welcome to the Trip Planner App! Plan, Budget, or Record a Trip quick, easy and free!")
        while True:
            print("\nPlease select an option:")
            print("1. Create/Update Itinerary")
            print("2. Manage Budget")
            print("3. Record Trip")
            print("4. Quit")
            choice = input("Enter your choice (1-4): ")

            if choice == "1":
                self.create_update_itinerary()
            elif choice == "2":
                self.manage_budget()
            elif choice == "3":
                self.record_trip()
            elif choice == "4":
                print("Thank you for using the Trip Planner App!")
                break
            else:
                print("Invalid choice. Please enter a valid option.")

    def create_update_itinerary(self):
        print("Welcome to the Create Itinerary section.\n")
        cancel_option = input("Enter 'cancel' at any time to cancel the itinerary creation. Press Enter to continue.")
        if cancel_option.lower() == 'cancel':
            print("Itinerary creation canceled.")
            return

        name = input("Enter your name: ")
        if name.lower() == 'cancel':
            print("Itinerary creation canceled.")
            return

        # Initialize an empty itinerary
        itinerary = {}

        # Ask for dates and activities
        while True:
            date = input("Enter date (YYYY-MM-DD) or type 'done' if finished: ")
            if date.lower() == 'cancel':
                print("Itinerary creation canceled.")
                return
            elif date.lower() == 'done':
                break

            activities = []
            while True:
                time_of_day = input("Enter time of day: ")
                if time_of_day.lower() == 'cancel':
                    print("Itinerary creation canceled.")
                    return

                activity_type = input("Enter activity type (activity/meal): ")

                # Check if the user wants to cancel
                if activity_type.lower() == 'cancel':
                    sure_cancel = input("Are you sure you want to cancel? (yes/no): ")
                    if sure_cancel.lower() == 'yes':
                        break
                    else:
                        continue  # Continue asking for activity type

                # Proceed if the user didn't choose to cancel
                if activity_type.lower() == "activity":
                    activity_name = input("Enter activity plans: ")
                elif activity_type.lower() == "meal":
                    activity_name = input("Enter meal plans: ")

                activities.append({'time_of_day': time_of_day, 'type': activity_type, 'name': activity_name})
                add_another = input("Add another activity? (yes/no): ")
                if add_another.lower() != 'yes':
                    break

            itinerary[date] = activities

        # Send itinerary to the ItineraryService to store
        if itinerary:  # Only create itinerary if activities were added
            self.itinerary_service.create_itinerary(name, itinerary)
            print("Itinerary created successfully!")
            self.print_itinerary(itinerary)
        else:
            print("Itinerary creation canceled.")
        pass

    def manage_budget(self):


        print("Welcome to the Budget Management section.\n")
        cancel_option = input("Enter 'cancel' at any time to cancel the itinerary creation. Press Enter to continue.")
        if cancel_option.lower() == 'cancel':
            print("Itinerary creation canceled.")
            return

        # Get user input for the number of days, total budget, and priorities
        total_days = input("Enter the number of days for your trip: ")

        if total_days.lower() == 'cancel':
            print("Budget management canceled.")
            return

        total_days = int(total_days)

        total_budget = input("Enter your total budget in dollars: ")
        if total_budget.lower() == 'cancel':    
            print("Budget management canceled.")
            return
        total_budget = float(total_budget)

        print("Please rank your priorities from 1 to 3 (1 being the highest priority)")
        priorities = []
        for i in range(1, 4):
            priority = input(f"Enter priority {i} (1 for Living, 2 for Food, 3 for Activities/Souvenirs): ")
            if priority.lower() == 'cancel':
                print("Budget management canceled.")
                return
            
            priority = int(priority)
            priorities.append(priority)

        # Calculate budget breakdown
        living_percentage = 0
        food_percentage = 0
        activities_percentage = 0

        if priorities == [1, 2, 3]:
            living_percentage = 0.60
            food_percentage = 0.30
            activities_percentage = 0.10
        elif priorities == [1, 3, 2]:
            living_percentage = 0.60
            food_percentage = 0.15
            activities_percentage = 0.25
        elif priorities == [2, 1, 3]:
            living_percentage = 0.50
            food_percentage = 0.40
            activities_percentage = 0.10
        elif priorities == [2, 3, 1]:
            living_percentage = 0.30
            food_percentage = 0.30
            activities_percentage = 0.40
        elif priorities == [3, 1, 2]:
            living_percentage = 0.50
            food_percentage = 0.10
            activities_percentage = 0.40
        elif priorities == [3, 2, 1]:
            living_percentage = 0.30
            food_percentage = 0.40
            activities_percentage = 0.30

        living_budget = total_budget * living_percentage
        food_budget = total_budget * food_percentage
        activities_budget = total_budget * activities_percentage

        # Calculate total cost per day
        total_cost_per_day = total_budget / total_days

        # Calculate cost per expense per day
        living_cost_per_day = living_budget / total_days
        food_cost_per_day = food_budget / total_days
        activities_cost_per_day = activities_budget / total_days

        # Calculate total cost per expense for the entire trip
        living_cost_total = living_budget
        food_cost_total = food_budget
        activities_cost_total = activities_budget

        # Print budget breakdown
        print("\nBudget Breakdown:")
        print(f"Living: ${living_budget:.2f}")
        print(f"Food: ${food_budget:.2f}")
        print(f"Activities/Souvenirs: ${activities_budget:.2f}")

        # Print total cost per day
        print("\nTotal Cost per Day:")
        print(f"${total_cost_per_day:.2f}")

        # Print cost per expense per day
        print("\nCost per Expense per Day:")
        print(f"Living: ${living_cost_per_day:.2f}")
        print(f"Food: ${food_cost_per_day:.2f}")
        print(f"Activities/Souvenirs: ${activities_cost_per_day:.2f}")

        # Set the budget for the user's trip
        name = input("Enter your name or 'cancel' to cancel: ")
        if name.lower() == 'cancel':
            print("Budget management canceled.")
            return
        self.budget_service.set_budget(name, total_budget)
        print("Budget set successfully!")
        pass
    

    def record_trip(self):
        print("Welcome to the Trip Recording section.")

        # Get user input for trip details
        cancel_option = input("Enter 'cancel' at any time to cancel recording trip details. Press Enter to continue.")
        if cancel_option.lower() == 'cancel':
            print("Recording trip details canceled.")
            return

        location = input("Where did you travel to: ")
        if location.lower() == 'cancel':
            print("Recording trip details canceled.")
            return

        travel_companions = input("Did you travel alone or with others? ")
        if travel_companions.lower() == 'cancel':
            print("Recording trip details canceled.")
            return

        food_rating = input("How would you rate the food on the trip (1-10): ")
        if food_rating.lower() == 'cancel':
            print("Recording trip details canceled.")
            return
        food_rating = int(food_rating)

        favorite_food = input("What was your favorite food: ")
        if favorite_food.lower() == 'cancel':
            print("Recording trip details canceled.")
            return

        least_favorite_food = input("What was your least favorite food: ")
        if least_favorite_food.lower() == 'cancel':
            print("Recording trip details canceled.")
            return

        hotel_rating = input("How would you rate the hotel/living (1-10): ")
        if hotel_rating.lower() == 'cancel':
            print("Recording trip details canceled.")
            return
        hotel_rating = int(hotel_rating)

        activities_rating = input("How would you rate the day-to-day activities (1-10): ")
        if activities_rating.lower() == 'cancel':
            print("Recording trip details canceled.")
            return
        activities_rating = int(activities_rating)

        favorite_activity = input("What was your favorite activity: ")
        if favorite_activity.lower() == 'cancel':
            print("Recording trip details canceled.")
            return

        least_favorite_activity = input("What was your least favorite activity: ")
        if least_favorite_activity.lower() == 'cancel':
            print("Recording trip details canceled.")
            return

        likelihood_to_go_back = input("How likely would it be for you to go back (1-10): ")
        if likelihood_to_go_back.lower() == 'cancel':
            print("Recording trip details canceled.")
            return
        likelihood_to_go_back = int(likelihood_to_go_back)

        memories = []
        while True:
            memory = input("Do you have a memory you'd like to remember? (Enter memory or 'done' to finish): ")
            if memory.lower() == 'done':
                break
            memories.append(memory)

        # Create trip details dictionary
        trip_details = {
            'location': location,
            'travel_companions': travel_companions,
            'food_rating': food_rating,
            'favorite_food': favorite_food,
            'least_favorite_food': least_favorite_food,
            'hotel_rating': hotel_rating,
            'activities_rating': activities_rating,
            'favorite_activity': favorite_activity,
            'least_favorite_activity': least_favorite_activity,
            'likelihood_to_go_back': likelihood_to_go_back,
            'memories': memories
        }

        # Send trip details to the TripRecordingService to store
        name = input("Enter your name: ")
        self.trip_recording_service.record_trip_details(name, trip_details)
        pass

    def print_itinerary(self, itinerary):
        print("\nYour Itinerary:")
        for date, activities in itinerary.items():
            print(f"\nDate: {date}")
            for activity in activities:
                print(f"Time of Day: {activity['time_of_day']}")
                print(f"Type: {activity['type']}")
                print(f"Plans: {activity['name']}")
                print("------------------------")




# Usage
if __name__ == "__main__":
    text_ui = TextUI()
    text_ui.start()