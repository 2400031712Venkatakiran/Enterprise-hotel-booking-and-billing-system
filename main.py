from abc import ABC,abstractmethod
class Room:
    def __init__(self,room_id,room_type,base_price,is_available):
        self.room_id=room_id
        self.room_type=room_type
        self.base_price=base_price
        self.is_available=is_available
class StandardRoom(Room):
    def __init__(self,room_id,room_type,base_price,is_available):
        super().__init__(room_id,room_type,500,"yes")
class DeluxeRoom(Room):
    def __init__(self,room_id,room_type,base_price,is_available):
        super().__init__(room_id,room_type,1000,"yes")
class SuiteRoom(Room):
    def __init__(self,room_id,room_type,base_price,is_available):
        super().__init__(room_id,room_type,1500,"yes")
class Guest:
    def __init__(self,guest_id,name,email):
        self.guest_id=guest_id
        self.name=name
        self.email=email
    def Create_Bookings(self):
        pass
    def View_Bill(self):
        pass
    def Cancel_Bookings(self):
        pass
class Bookings:
    def __init__(self,booking_id,guest,room,check_in_days,status):
        self.booking_id=booking_id
        self.guest=guest
        self.room=room
        self.check_in_days=check_in_days
        self.status=status
        self.services=[]
    def add_service(self,service):
        self.services.append(service)
    def calculate_total(self):
        pass
    def change_status(self):
        pass
    def cancel_booking(self):
        if self.status == 'Booked':
            refund=self.amount*0.9
        elif self.status=='checkedin':
            refund=self.amount*0.5
        else:
            refund=0
        return refund
class Service:
    def __init__(self,name,price):
        self.price=price
        self.name=name
class Pricing_Startegy:
    @abstractmethod
    def pricing_startegy(self):
        pass
class Regular_Pricing(Pricing_Startegy):
    def pricing_startegy(self,amount):
        self.final_bill=amount
        return self.final_bill

class Seasonal_Pricing(Pricing_Startegy):
    def pricing_startegy(self,amount):
        self.final_bill=amount
        return self.final_bill

class Festival_Pricing(Pricing_Startegy):
    def pricing_startegy(self,amount):
        self.final_bill=amount*1.2
        return self.final_bill
class HotelManager:
    def __init__(self):
        pass
def main():
    manager = HotelManager()

    while True:
        print("\n--- Hotel Booking System ---")
        print("1. Add Room")
        print("2. Register Guest")
        print("3. Create Booking")
        print("4. Add Service")
        print("5. Process Payment")
        print("6. Cancel Booking")
        print("7. Show All Bookings")
        print("8. Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:

            pass

        elif choice == 2:
            pass

        elif choice == 3:
            pass

        elif choice == 4:
            pass

        elif choice == 5:
            pass

        elif choice == 6:
            pass

        elif choice == 7:
            pass

        elif choice == 8:
            break

        else:
            print("Invalid choice")
if __name__=="__main__":
    main()











