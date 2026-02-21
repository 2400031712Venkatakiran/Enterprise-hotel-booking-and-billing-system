from abc import ABC,abstractmethod

class Room:
    def __init__(self,room_id,room_type,base_price,is_available):
        self.room_id=room_id
        self.room_type=room_type
        self.base_price=base_price
        self.is_available=is_available


class StandardRoom(Room):
    def __init__(self,room_id):
        super().__init__(room_id,'StandardRoom',500,True)


class DeluxeRoom(Room):
    def __init__(self,room_id):
        super().__init__(room_id,'DeluxeRoom',1000,True)


class SuiteRoom(Room):
    def __init__(self,room_id):
        super().__init__(room_id,'SuiteRoom',1500,True)


class Guest:
    def __init__(self,guest_id,name,email):
        self.guest_id=guest_id
        self.name=name
        self.email=email


class Bookings:

    def __init__(self,booking_id,guest,room,check_in_days):
        self.booking_id=booking_id
        self.guest=guest
        self.room=room
        self.check_in_days=check_in_days
        self.status='Booked'
        self.services=[]

    def add_service(self,service):
        self.services.append(service)

    def calculate_total(self,pricing_startegy):
        total_days=self.check_in_days*(self.room.base_price)
        service_amount=sum(service.price for service in self.services)
        final_amount=total_days+service_amount
        return pricing_startegy.apply(final_amount)

    def change_status(self,name):
        self.status=name

    def cancel_booking(self):

        final_amount=(self.check_in_days)*self.room.base_price
        if self.status == 'Booked':
            refund=final_amount*0.9
        elif self.status=='checkedin':
            refund=final_amount*0.5
        else:
            refund=0
            self.status='cancel'
            self.room.is_available=True
        return refund

class Service:

    def __init__(self,name,price):
        self.price=price
        self.name=name

class Pricing_Startegy(ABC):

    @abstractmethod
    def apply(self,amount):
        pass


class Regular_Pricing(Pricing_Startegy):

    def apply(self,amount):
        final_amount=amount
        return final_amount

class Seasonal_Pricing(Pricing_Startegy):

    def apply(self,amount):
        final_amount=amount
        return final_amount

class Festival_Pricing(Pricing_Startegy):

    def apply(self,amount):
        final_amount=amount*1.2
        return final_amount


class Payment_Method(ABC):
    @abstractmethod
    def pay(self,amount):
        pass

class CardPayment(Payment_Method):
    def pay(self,amount):
        print(f"{amount} was paid using CardPayment method")

class UPIpayment(Payment_Method):
    def pay(self,amount):
        print(f"{amount}was paid using UPIpayment method")

class CashPayment(Payment_Method):
    def pay(self,amount):
        print(f"{amount} was paid using Cashpayment method")


class HotelManager:

    def __init__(self):
        self.Rooms={}
        self.Bookings={}
        self.guests={}
    def add_room(self,Room):
        self.Rooms[Room.room_id]=Room
        return f"Room was added"
    def register_guest(self,guest):
        self.guests[guest.guest_id]=guest
        return f"Guest was registered"
    def create_booking(self,booking_id,room_id,guest_id,days):
        if room_id not in self.Rooms or guest_id not in self.guests:
            return f"Booking doesnt exist"
        room=self.Rooms[room_id]
        if not(room.is_available):
            return f"Rooms are not available"
        room.is_available=False
        self.Bookings[booking_id]=Bookings(booking_id,self.guests[guest_id],room,days)
        return "Booking has done"

    def cancel_booking(self,booking_id):
        if booking_id in self.Bookings:
            self.Bookings[booking_id].cancel_booking()

            return f"Booking canceled"
        return f"Booking id doesn't exist"
    def add_service(self,booking_id,service):
        if booking_id in self.Bookings:
            self.Bookings[booking_id].add_service(service)
            return f"service added"
        return f"booking id doesnt exist"
    def process_payment(self,booking_id,pricing_startegy,payment_method):
        if booking_id in self.Bookings:
            final_amount=self.Bookings[booking_id].calculate_total(pricing_startegy)
            payment_method.pay(final_amount)
            self.Bookings[booking_id].status='checkedin'
            return f"process completed"
        return f"booking id doesnt exist"

    def show_all_bookings(self):
        for bookings in self.Bookings.values():
            print(f"Booking id is {bookings.booking_id}")
            print(f"guest name is {bookings.guest.name}")
            print(f"status and check in days are {bookings.check_in_days} and {bookings.status}")




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
            room_id=int(input("enter the room id"))
            room_type = int(input("Choose room type: "))

            if room_type == 1:
                room = StandardRoom(room_id)
            elif room_type == 2:
                room = DeluxeRoom(room_id)
            else:
                room = SuiteRoom(room_id)

            print(manager.add_room(room))

        elif choice == 2:
            guest_id=int(input("enter guest id: "))
            guest_name=input("enter the guest name: ")
            email=input("enter the email: ")
            print(manager.register_guest(Guest(guest_id,guest_name,email)))

        elif choice == 3:
            room_id=int(input("enter the room id: "))
            guest_id=int(input("enter the guest id: "))
            booking_id=int(input("enter the booking id: "))
            days=int(input("enter the no of days you want to stay"))
            print(manager.create_booking(booking_id,room_id,guest_id,days))

        elif choice == 4:
            booking_id=int(input("enter the booking id"))
            service_name=input("enter the service name")
            service_price=int(input("enter the service price"))
            service=Service(service_name,service_price)
            manager.add_service(booking_id,service)


        elif choice == 5:
            booking_id=int(input("enter the booking id "))
            print("1. Regular\n2. Seasonal\n3. Festival")
            pricing_choice = int(input("Choose pricing strategy: "))
            if pricing_choice == 1:
                pricing = Regular_Pricing()
            elif pricing_choice == 2:
                pricing = Seasonal_Pricing()
            else:
                pricing = Festival_Pricing()

            print("1. Card\n2. UPI\n3. Cash")
            payment_choice = int(input("Choose payment method: "))
            if payment_choice == 1:
                payment = CardPayment()
            elif payment_choice == 2:
                payment = UPIpayment()
            else:
                payment = CashPayment()

            print(manager.process_payment(booking_id, pricing, payment))


        elif choice == 6:
            booking_id=int(input("enter the booking id: "))
            manager.cancel_booking(booking_id)

        elif choice == 7:
            manager.show_all_bookings()

        elif choice == 8:
            break

        else:
            print("Invalid choice")
if __name__=="__main__":
    main()











