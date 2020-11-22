import json 

with open('training.json') as f :
    data = json.load(f)



#sample_dict = data['data'][0]['paragraphs'][0]
def create_input(sample_dict):
    return_list = list()
    context = sample_dict['context']
    for i in range(len(sample_dict['qas'])):
        question = sample_dict['qas'][i]['question']
        if sample_dict['qas'][i]['is_impossible'] == False:
            if len(sample_dict['qas'][i]['answers']) > 1:
                print('haha multiple!')
            answer = sample_dict['qas'][i]['answers'][0]['text']   
        else: 
            answer = ''
        return_str = str(context) + str(question)
        return_tuple = (return_str,answer)
        return_list.append(return_tuple)
    return return_list


total_list = list()
for i in range(len(data['data'])):
    for j in range(len(data['data'][i]['paragraphs'])):
        list_to_append = create_input(data['data'][i]['paragraphs'][j])
        total_list.extend(list_to_append)
