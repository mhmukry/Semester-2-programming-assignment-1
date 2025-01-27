import datetime 
#Class to test various scenarios of the Think Python exercise
class Think_Python:
  #Trying to solve exercise 2.2 
    width = 17
    height = 12.0
    delimeter = '.'
    print(f'width/2:{width/2}')
    print(f'width/2.0:{width/2.0}')
    print(f'height/3:{height/3}')
    print(f'delimeter*5:{delimeter*5}')
    #Trying to solve exercise 2.3 Question # 1
    r = 5
    volume = (4/3) * (22/7) * (r*r*r)
    print(f'volume = (4/3) * (22/7) * (r^3):{volume}')  
    #Trying to solve exercise 2.3 Question # 2
    book_cost = 24.95
    discounted_book_cost = 0.6 * book_cost
    total_discounted_book_cost = 60 * discounted_book_cost
    shipping_cost = 3 + (59 * 0.75)
    print(f'discounted price + shipping:{shipping_cost+ total_discounted_book_cost }')  
    #Trying to solve exercise 2.3 Question # 3
    # Initializing a date and time 
    date_and_time = datetime.datetime(2025, 1, 26, 6, 52, 0) 
      
    print("Original time:") 
    print(date_and_time) 
      
    # Calling the timedelta() function  
    time_change = datetime.timedelta(seconds=495) 
    new_time = date_and_time + time_change 
    date_and_time = new_time
    print("changed time:") 
    print(new_time) 
      # Calling the timedelta() function  
    time_change = datetime.timedelta(seconds=432*3) 
    new_time = date_and_time + time_change 
    date_and_time = new_time
    # Printing the new datetime object 
    print("changed time:") 
    print(new_time) 
      # Calling the timedelta() function  
    time_change = datetime.timedelta(seconds=495) 
    new_time = date_and_time + time_change 
    date_and_time = new_time
    # Printing the new datetime object 
    print("changed time:") 
    print(new_time) 