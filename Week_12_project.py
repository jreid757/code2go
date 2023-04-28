# 1) The list should be empty initially
service_list = []

# 2) Populate the list using append or insert
service_list.append('S3')
service_list.append('EC2')
service_list.append('Lambda')
service_list.append('Cloud9')

# 3) Print the list and the length of the list
print(service_list)
print(len(service_list))

# 4) Remove two specific services from the list by name or by index
del service_list[0]
del service_list[1]

# 5) Print the new list and the new length of the list
print(service_list)
print(len(service_list))
