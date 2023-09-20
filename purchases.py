def add_tax(sales_tax, cost_list):
 
  sales_tax_list = []
 
  for i in range(len(cost_list)):
   
    total_cost = (sales_tax*float(cost_list[i])+float(cost_list[i]))
   
    sales_tax_list.append(total_cost)
   
  return sales_tax_list



def customer_and_cost_dict(customer_list, total_cost_list):
    
    customer_cost_dict = dict()
    
    for customer, cost in zip(customer_list, total_cost_list):
        
        if customer in customer_cost_dict:
            customer_cost_dict[customer] += cost
            
        else:
            customer_cost_dict[customer] = cost
            
    return customer_cost_dict
     




def main():
 
  customer_list = []
  cost_list = []
 
  num_purchases = int(input("Number of purchases: "))
  sales_tax = float(input("Sales tax: "))
 
  for i in range(num_purchases):
    customer = input("Customer: ")
    cost = input("Cost: ")
    customer_list.append(customer)
    cost_list.append(cost)
   
  sales_tax_cost_list = (add_tax(sales_tax, cost_list))
 
  print(customer_and_cost_dict(customer_list, sales_tax_cost_list))
   
   
main()

