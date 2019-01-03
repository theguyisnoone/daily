#card system
import cards_tools
while True:
    #TODO（lee） 显示系统菜单
    #用户输入
    action=input('请输入所需要的功能：')
    #如果输入123
    if action in ['1','2','3']:
        if action == '1':
            cards_tools.new_card()
        elif action == '2':
            cards_tools.show_all()
        elif action == '3':
            cards_tools.search_card()

    elif action == '0':
        print('thank you.hope that you will use  this system again')
        # exit()
        break
    else:
        print('error system')
