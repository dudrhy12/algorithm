def solution(today, terms, privacies):
    answer = []
    today_year = int(today.split(".")[0])
    today_month = int(today.split(".")[1])
    today_date = int(today.split(".")[2])
    terms_dic = {}
    for i in range(len(terms)):
        key = terms[i].split(" ")[0]
        value = terms[i].split(" ")[1]
        terms_dic[key] = value  
    for i in range(len(privacies)):
        collected_day = privacies[i].split(" ")[0]
        collected_term = privacies[i].split(" ")[1]
        if validate_check(today_year, today_month, today_date, collected_day, collected_term, terms_dic) == False:
            answer.append(i+1)
    return answer

def validate_check(today_year, today_month, today_date, collected_day, collected_term, terms_dic):
    expiration_date = terms_dic[collected_term]
    destroy_year, destroy_month, destroy_date = calculate_date(today_year, today_month, today_date, collected_day, expiration_date)
    if destroy_year > today_year:
        return True
    elif destroy_year == today_year and destroy_month > today_month:
        return True
    elif destroy_year == today_year and destroy_month == today_month and destroy_date >= today_date:
        return True
    return False
    
    
def calculate_date(today_year, today_month, today_date, collected_day, expiration_date):
    collected_date = collected_day.split(".")[2]
    collected_month = collected_day.split(".")[1]
    collected_year = collected_day.split(".")[0]
    
    destroy_year = int(collected_year)
    destroy_month = int(collected_month) + int(expiration_date)
    destroy_date = int(collected_date) - 1
    
    if destroy_month > 12 :
        destroy_year += ( destroy_month // 12 )
        destroy_month = ( destroy_month % 12 )
    
    if destroy_date < 1:
        destroy_date = 28
        destroy_month -= 1
    
    if destroy_month < 1:
        destroy_month = 12
        destroy_year -= 1
        
    return destroy_year, destroy_month, destroy_date
        