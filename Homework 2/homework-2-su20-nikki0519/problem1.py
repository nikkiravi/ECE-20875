def addressbook(name_to_phone, name_to_address):
    #name_to_phone and name_to_address are both dictionaries
    
    # Write your code here

    # return the variable storing address_to_all
    # Output should be a dictionary

    result = {}

    for name, address in name_to_address.items():
    	if(address not in result):
    		names = [name]
    		phone = name_to_phone[name]
    		result[address] = (names, phone)

    	else:
    		result[address][0].append(name)
    		if(name_to_phone[name] != result[address][1]):
    			print("Warning: %s has a different number for %s than %s. Using the number for %s." % (name, address, result[address][0][0], result[address][0][0]))

    return(result)
    
    pass
