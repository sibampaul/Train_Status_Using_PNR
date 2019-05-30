# Program to find PNR in Python

import json,requests

def get_train_details():

    api_key = "arz6oaccpj"
    url = "https://api.railwayapi.com/v2/pnr-status/pnr/"

    pnr_number=input("\nPlease Enter Your PNR No. : ")
    #pnr_number = "4604322242"

    final_url = url + pnr_number + "/apikey/" + api_key + "/"

    response = requests.get(final_url)

    result = response.json()
    #print(result)

    if result["response_code"] == 200:
        pnr_num = result["pnr"]
        train_name = result["train"]["name"]
        train_number = result["train"]["number"]
        date_of_journey = result["doj"]
        from_station = result["from_station"]["name"]
        to_station = result["to_station"]["name"]
        boarding_point = result["boarding_point"]["name"]
        reservation_upto = result["reservation_upto"]["name"]
        chart_prepared = result["chart_prepared"]
        total_passengers = result["total_passengers"]

        print("\n-------------------------------\n Train name : " + str(train_name) + "\n Train number : " + str(train_number)+ "\n From station : " + str(from_station)
              + "\n To station : " + str(to_station) + "\n Boarding point : " + str(boarding_point) + "\n Reservation upto : " + str(reservation_upto)
              + "\n PNR number : " + str(pnr_num) + "\n Date of journey : " + str(date_of_journey) + "\n Total no. of passengers: " + str(total_passengers) + "\n Chart prepared : " + str(chart_prepared))

        passengers_list = result["passengers"]

        for x in passengers_list:

            current_status = x["current_status"]
            booking_status = x["booking_status"]

            print(" Current status : " + str(current_status) + "\n Booking_status : " + str(booking_status))

    else:
        print("record is not found for given request")

    continue_or_not()

def continue_or_not():
    take_input =input("\n If you want to try again Press Y/y or Press any key and Enter to exit : ")

    if take_input == 'y' or take_input=="Y":
        get_train_details()
    else:
        return 0
get_train_details()
