#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 16:14:03 2019

@author: vikram
"""

import json
json_string = """
{
"student":{
"First Name":"vikram",
"Last Name":"sinhg",
"photo":"www.jsonlint.com",
"Department":"computer science",
"Research Areas":{
"Research 1":"cryptography",
"Research 2":"data science"
},
"Contact Details":[
{
"phone number":"987",
"email id":"abc@gmail.com"
}
]
}

}
"""
print (type(json_string))
my_data = json.loads(json_string)
print(my_data)
print (my_data['student']["Research Areas"])
print (my_data['student']["Research Areas"]['Research 1'])


import json
json_string = """
{
	"Faculty": {

		"faculty1": {
			"First Name": "vikram",
			"Last Name": "sinhg",
			"photo": "www.jsonlint.com",
			"Department": "computer science",
			"Research Areas": {
				"Research 1": "cryptography",
				"Research 2": "data science"
			},
			"Contact Details": {
				"phone number": ["987", "645"],
				"email id": "abc@gmail.com"
			}
		},
		"faculty2": {
			"First Name": "rahul",
			"Last Name": "kumar",
			"photo": "www.jsonlint.com",
			"Department": "computer science",
			"Research Areas": {
				"Research 1": "cryptography",
				"Research 2": "data science"
			},
			"Contact Details": {
				"phone number": ["987", "645"],
				"email id": "abc@gmail.com"
			}
		}
	}
}
"""

print (type(json_string))
my_data = json.loads(json_string)
print(my_data)
print (my_data['Faculty']["faculty1"])
print (my_data['Faculty']["faculty2"]['Department'])