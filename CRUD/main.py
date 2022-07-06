from views import delete_product, list_of_product, retrieve_data, create_product, update_product, delete_product

def main():
    print('privet, tebe dostupny sleduyuwie funkciyi: \n\tLIST-1:\n\tRETRIEVE-2\n\tCREATE-3\n\tUPDATE-4\n\tDELETE-5')
    
    choice = input('Vvedite deistviye(1,2,3,4,5): ')
    if choice == '1':
        print(list_of_product())
    elif choice == '2':
        print(retrieve_data())
    elif choice == '3':
        print(create_product())
    elif choice == '4':
        print(update_product())
    elif choice == '5':
        print(delete_product())
    else:
        print('Invalid choice!')
        main()

    ask = input('Hotite prodoljit\'?(Yes/No)')
    if ask.lower() == 'yes':
        main()
    else:
        print('Poka! Poka!')
    
main()