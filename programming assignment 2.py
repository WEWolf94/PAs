# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 13:34:57 2024

@author: LMOakes
"""

import random as rand
from tabulate import tabulate
#Given Queue class
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []
    
    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        self.out = self.items.pop()
        return self.out

    def size(self):
        return len(self.items)
    
class Customer:
    def __init__(self, rate_per_item = 0):
        self.items = rand.randint(6, 20)
        self.rate_per_item = rate_per_item
        self.time_for_just_items = self.items*self.rate_per_item
        self.time_to_checkout = self.time_for_just_items + 45
        self.less_than_10 = False
    
    def subtract_second_from_checkout_time(self):
        self.time_to_checkout -= 1
        if self.time_for_just_items > -1:
            self.time_for_just_items -= 1
    
    def get_items(self):
        return self.items
        
    def get_time_to_checkout(self):
        return self.time_to_checkout
        
    def get_less_than_10(self):
        if self.items < 10:
            self.less_than_10 = True
        else:
            self.less_than_10 = False
        return self.less_than_10
    
    def get_time_for_items(self):
        return self.time_for_just_items

class Register:
    def __init__(self, is_express_lane, reg_name):
        self.is_express_lane = is_express_lane
        self.queue_of_customer = Queue()
        self.total_time_customers_waiting = 0
        self.total_num_customers_served = 0
        self.total_idle_time = 0
        self.current_customer = None
        self.total_items = 0
        self.avg_wait_time = 0
        self.reg_name = reg_name
        
    def add_customer_to_queue(self, Customer):
        if self.current_customer == None:
            self.current_customer = Customer
        else:
            self.queue_of_customer.enqueue(Customer)
    
    def remove_customer_from_queue(self):
        if self.queue_of_customer.size() == 0:
            self.current_customer = None
        else:
            self.current_customer = self.queue_of_customer.dequeue()
        self.total_num_customers_served += 1
    
    def check_if_empty(self):
        if self.current_customer == None and self.queue_of_customer.size() == 0:
            self.total_idle_time += 1
            return True
        else:
            return False
    
    def total_time_customers_waiting_plus_one(self):
        self.total_time_customers_waiting += 1
        return 0
    
    def total_items_plus_one(self):
        self.total_items += 1
        
    def get_avg_wait_time(self):
        if self.total_time_customers_waiting != 0:
            self.avg_wait_time = self.total_num_customers_served // self.total_time_customers_waiting
        return self.avg_wait_time
    
    def get_current_customer(self):
        return self.current_customer
    
    def get_size_customer_queue(self):
        return self.queue_of_customer.size()
    
    def get_customer_queue(self):
        return self.queue_of_customer.items
    
    def get_express(self):
        return self.is_express_lane
    
    def get_reg_name(self):
        return self.reg_name


def simulation(num_registers_stand, num_registers_express, items_for_express,
               rate_per_item, total_sec_for_simulation):
    
    list_of_registers = []

    count = 0
    for reg in range(num_registers_stand):
        count += 1
        reg_name = "Register " + str(count)
        temp_name = Register(False, reg_name)
        list_of_registers.append(temp_name)
    
    count += 1
    reg_name = "Register " + str(count)
    exp_reg = Register(True, reg_name)
    list_of_registers.append(exp_reg)      
        
    for second in range(total_sec_for_simulation):
        
        if ((second + 1) % 30) == 0:
            list_of_registers = new_customer(list_of_registers, rate_per_item)
            
        if ((second + 1) % 50) == 0:
            sec50_output(list_of_registers)
        
        for reg in list_of_registers:
            reg.check_if_empty()
            
            current_customer = reg.get_current_customer()
            
            if current_customer != None:
                if current_customer.get_time_for_items() % rate_per_item == 0:
                    reg.total_items_plus_one()
                    
                current_customer.subtract_second_from_checkout_time()
                if current_customer.get_time_to_checkout() == 0:
                    reg.remove_customer_from_queue()
                    
            if reg.get_size_customer_queue != 0:
                queue_customers = reg.get_customer_queue()
                
                for customer in queue_customers:
                    reg.total_time_customers_waiting_plus_one()
    
    for reg in list_of_registers:
        reg.get_avg_wait_time()
        
    return list_of_registers


def new_customer(list_of_registers, rate_per_item):
    new_cust = Customer(rate_per_item)
    new_cust_reg = []
 
    if new_cust.get_less_than_10() == True:
        for reg in list_of_registers:
            if reg.get_express() == True and reg.check_if_empty() == True:
                reg.add_customer_to_queue(new_cust)
                return list_of_registers
        if new_cust_reg == []:
            for reg in list_of_registers:
                if reg.get_current_customer() == None:
                    new_cust_reg.append(reg)
        if new_cust_reg == []:
            smallest_queue = min(reg.get_size_customer_queue() for reg in list_of_registers)
            for reg in list_of_registers:
                if reg.get_size_customer_queue() <= smallest_queue:
                    new_cust_reg.append(reg)

    else:
        for reg in list_of_registers:
            if reg.get_current_customer() == None and reg.get_express() == False:
                new_cust_reg.append(reg)
        if new_cust_reg == []:
            smallest_queue = min(reg.get_size_customer_queue() for reg in list_of_registers)
            for reg in list_of_registers:
                if reg.get_size_customer_queue() <= smallest_queue and reg.get_express() == False:
                    new_cust_reg.append(reg)
    
    new_reg = rand.choice(new_cust_reg)
    
    for reg in list_of_registers:
        if new_reg == reg:
            reg.add_customer_to_queue(new_cust)
            
    return list_of_registers


def sec50_output(list_of_registers):
    print()
    print()
    for reg in list_of_registers:
        print(reg.get_reg_name())
        if reg.get_current_customer() != None:
            print("Items for current customer: " + str(reg.get_current_customer().get_items()))
        print("Customers in queue: " + str(reg.get_size_customer_queue()))


def final_output(list_of_registers):
    none = None
    data_2 = []
    for reg in list_of_registers:
        data = []
        a = reg.get_reg_name
        data.append(a)
        z = reg.get_customers_served
        data.append(z)
        y = reg.get_total_items
        data.append(y)
        b = reg.get_idle_time
        data.append(b)
        x = reg.get_avg_wait_time
        data.append(x)
        data_2.append(data)
        
    headers = ['Register', 'total customers', 'total items',
               'total idle time (min)', 'average wait time (sec)']
    
    table = tabulate(data_2, headers, tablefmt="grid")
    

def main():
    items_for_express = 10
    rate_per_item = 4
    total_sec_for_simulation = 1200
    num_registers_stand = 4
    num_registers_express = 1
    
    list_of_registers = simulation(num_registers_stand, num_registers_express, 
            items_for_express, rate_per_item, total_sec_for_simulation)
    
    sec50_output(list_of_registers)
    
    
    
    data = []
    
    headers = ['Register', 'total customers', 'total items',
               'total idle time (min)', 'average wait time (sec)']
    
    table = tabulate(data, headers, tablefmt="grid")
    
main()

