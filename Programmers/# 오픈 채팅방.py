def solution(record):
    user_dict, chat_list = {}, []
    for info in record :
        info_list = info.split(' ')
        
        if len(info_list) == 2 :
            action, user_id = info_list
        else :
            action, user_id, nick_name = info_list
            
        if action == 'Change' :
            user_dict[user_id] = nick_name
            continue
        if action == 'Enter' :
            user_dict[user_id] = nick_name
            chat_list.append(('e', user_id))
        else :
            chat_list.append(('l', user_id))
    answer = []
    for info in chat_list:
        action, user_id = info
        if action == 'e' :
            answer.append("{}님이 들어왔습니다.".format(user_dict[user_id]))
        else :
            answer.append("{}님이 나갔습니다.".format(user_dict[user_id]))
    return answer