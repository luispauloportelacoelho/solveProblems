def search_contact(name, contacts):
    if name in contacts:
        response = name + "=" + str(contacts[name])
        return response
    else:
        return "Not found"


if __name__ == '__main__':
    number_numbers = int(input())

    contacts = {}
    for x in range(number_numbers):
        name_number = str(input())
        aux = name_number.split()
        contacts.update({aux[0]: aux[1]})

    for y in range(number_numbers):
        name = str(input())
        print(search_contact(name, contacts))    
