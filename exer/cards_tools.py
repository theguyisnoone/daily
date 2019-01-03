#显示菜单
card_list=list()

def show_menu():
    '''显示菜单
    '''
    print('*' * 50)
    print('welcome to use this lame system,you loser')
    print('\n')
    print('1.create a new card')
    print('2.show all cards')
    print('3.search some card you want')
    print('\n')
    print('0.exit finally')
    print('*' * 50)


#新建名片
def new_card():
    '''新建菜单
    '''
    print('-' * 50)
    print('function:create card')

    #1.input information
    #name
    name=input('>>>print some suck name:\n')
    #phone number
    phone=input('>>>print phone_number:\n')
    #qq
    qq=input('>>>print qq:\n')
    #email
    email=input('>>>print email:\n')

    #2.save data into dic
    #card_dict
    card_dict={'name':name,
                'phone':phone,
                'qq':qq,
                'email':email
                }

    #3.list append card_dict

    card_list.append(card_dict)
    #4.print successfully
    print('successfully add %s'%card_dict['name'])
#显示全部信息
def show_all():
    '''显示全部
    '''
    print('-' * 50)
    print('function:show all')

    # for i in card_list:
    #     print(i)
    for i in ['name','phone','qq','email']:
        print(i,end='\t\t')

    print('\n')
    print('='*50)
    for card_dict  in card_list:
        print('{}\t\t{}\t\t{}\t\t{}\t\t'.format(card_dict['name'],card_dict['phone'],card_dict['qq'],card_dict['email']))


#搜索名片
def search_card():
    '''搜索名片
    '''
    print('-' * 50)
    print('function:search card')

    find_name=input('what name:\n')
    for card_dict in card_list:
        if card_dict['name'] == find_name:
            for i in ['name','phone','qq','email']:
                print(i,end='\t\t')

            print('\n')
            print('='*50)
            for card_dict  in card_list:
                print('{}\t\t{}\t\t{}\t\t{}\t\t'.format(card_dict['name'],card_dict['phone'],card_dict['qq'],card_dict['email']))
            break
        else:
            print('cant find {}'.format(card_dict['name']))
