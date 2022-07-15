
import pandas as pd
from operator import itemgetter
movie_meta = pd.read_csv('movies_metadata.csv', low_memory = False)
actor_meta = pd.read_csv('credits.csv', low_memory = False)
def processHeat(data, code):
    # monthList = ['T1', 'T2','T3','T4', 'T5', 'T6', 'T7',' T8', 'T9', 'T10', 'T11','T12']
    minDate = data['min']
    maxDate = data['max']
    dictAll = {str(i):[0]*12 for i in range(int(minDate), int(maxDate)+1)}
    dict1 = {str(i):[0]*12 for i in range(int(minDate), int(maxDate)+1)}
    list1 = data[code][1:]
    listAll = data['all'][1:]
   
    for i in list1:
        
        dict1[i['year'][:4]][int(i['year'][-2:])-1] += int(i['count_movie'])
    for i in listAll:
        dictAll[i['year'][:4]][int(i['year'][-2:])-1] += int(i['count_movie'])
    for i in range(int(minDate), int(maxDate)+1):
        temp = []
        tempAll = []
        for ind,j in enumerate(dict1[str(i)]):
            j = {
                'x': 'T'+ str(ind+1),
                'y': j
            }
            temp.append(j)
        dict1[str(i)] = temp
        for ind,j in enumerate(dictAll[str(i)]):
            j = {
                'x': 'T'+ str(ind+1),
                'y': j
            }
            tempAll.append(j)
        dictAll[str(i)] = tempAll
        # dict1[str(i)] = dict(zip(monthList, dict1[str(i)]))
        # dictAll[str(i)] = dict(zip(monthList, dictAll[str(i)]))
    return {
        'min': int(minDate),
        'max': int(maxDate),
        'region' :    [{'year' : j, 'data' : dict1[j] } for j in dict1]
        # 'all':   [{'year' : j, 'data' : dictAll[j] } for j in dictAll]
    }
class DataMap:
    def __init__(self, data):
        self.code = data[0]
        self.name = data[1]
        self.movieCount = data[2]
        self.tb = data[3]
        self.voteCount = data[4]

class ChartLine:
    def __init__(self, data):
        self.runtime = data[0]
        self.popularity = data[1]
class ChartHisto:
    def __init__(self, data):
        self.runtime = data[0]
        self.movieCount = data[1]
class ChartPyramid:
    def __init__(self, data):
        self.year = data[0]
        self.movieCount = data[1]
class ChartPie:
    def __init__(self, data):
        self.code = data[0]
        self.name = data[1]
        self.movieCount = data[2]
        self.popularity = data[3]
        self.voteCount = data[4]
        self.revenue = data[5]
class Film:
    def __init__(self, data):
        # 
        self.id = data[0]
        self.budget = data[1]
        self.title = data[2]
        self.overview = data[3]
        self.popularity = data[4]
        self.vote_tb = data[5]
        self.date = data[6]
        self.country = data[7]


def data_map():
    # movie_meta = pd.read_csv('movies_metadata.csv', low_memory = False)
    result = []
    code = []
    total = []
    df = (movie_meta['production_countries'])
    vote_a = movie_meta['vote_average']
    vote_c = movie_meta['vote_count']
    for ind_row, row in enumerate(df):
        
        if row != '[]':
            try:
                row_c = (row[1:-1].replace("{","").replace("}","").split(','))
            except Exception as e:
                print(e, row)
            row_fi = [i.split(":") for i in row_c]
            
            for i in range(0, len(row_fi),2):
                # print(len(row_fi[i][0]))
                if  'iso_3166_1' in row_fi[i][0][1:-1]:
                    row_code = row_fi[i][1].replace(' ', '')[1:-1]
                    if row_code not in code:
                        code.append(row_code)
                        result.append([row_code, row_fi[i+1][1][2:-1], 1, vote_a[ind_row] * vote_c[ind_row], vote_c[ind_row]])
                    else: 
                        result[code.index(row_code)][2] += 1
                        result[code.index(row_code)][3] += vote_a[ind_row] * vote_c[ind_row]
                        result[code.index(row_code)][4] += vote_c[ind_row]
    for i in result:
        if int(i[3]) != 0:
            i[3] = round(i[3] / i[4], 3)
        i[4] = int(i[4])
        temp = DataMap(i)
        i = {'code': temp.code, 'name': temp.name, 'movieCount': temp.movieCount, 'voteAvg' :temp.tb, 'voteCount': temp.voteCount}
        total.append(i)
        # print(i)
    # for i in result:
    #     if str(i[3]) == "nan":
    #         print("err", i)
    #         break
    return total
# print(data_map())
def get_film(code):
    movie_meta1 = movie_meta.sort_values(by=['popularity'], ascending=False).reset_index(drop=True)
    data = (movie_meta1[['imdb_id','budget', 'original_title', 'overview', 'popularity', 'vote_average', 'release_date', 'production_countries']])
    count = 0
    index_row = []
    for index,row in enumerate(data['production_countries']):
        if count == 20: break
        if code in row:
            # print(data.filter(items=[index-1], axis=0))
            index_row.append(index)
            count += 1
    
    total_code = []
    total_all = []
    temp_all = data.head(20).values.tolist()
    temp_code = data.filter(items=index_row, axis=0).values.tolist()
    for j in temp_code:
        temp = Film(j)
        j = {'id': temp.id, 'budget': temp.budget, 'title': temp.title, 'overview' :temp.overview, 'popularity': temp.popularity,
        'voteAverage' : temp.vote_tb, 'date': temp.date, 'country': temp.country,
        }
        total_code.append(j)
    for j in temp_all:
        temp = Film(j)
        j = {'id': temp.id, 'budget': temp.budget, 'title': temp.title, 'overview' :temp.overview, 'popularity': temp.popularity,
        'voteAverage' : temp.vote_tb, 'date': temp.date, 'country': temp.country,
        }
        total_all.append(j)
    data_return = {
        'region' : total_code,
        'all': total_all
    }
    return (data_return)
# get_film('VN')


def type_pie(nation_code):
    # movie_meta = pd.read_csv('movies_metadata.csv', low_memory = False)
    result = []
    total = []
    code = []
    df = (movie_meta['genres'])
    vote_a = movie_meta['popularity']
    vote_c = movie_meta['vote_count']
    revenue = movie_meta['revenue']
    nation_col = movie_meta['production_countries']
    for ind_row, row in enumerate(df):
        if nation_code in nation_col[ind_row]:
            if row != '[]':
                try:
                    row_c = (row[1:-1].replace("{","").replace("}","").split(','))
                except Exception as e:
                    pass
                row_fi = [i.split(":") for i in row_c]
                for i in range(0, len(row_fi),2):
                    if  'id' in row_fi[i][0][1:-1]:
                        row_code = row_fi[i][1].replace(' ', '')
                        if row_code not in code:
                            code.append(row_code)
                            result.append([row_code, row_fi[i+1][1][2:-1], 1, vote_a[ind_row] , vote_c[ind_row], int(revenue[ind_row])])
                        else: 
                            result[code.index(row_code)][2] += 1
                            result[code.index(row_code)][3] += vote_a[ind_row] 
                            result[code.index(row_code)][4] += vote_c[ind_row]
                            result[code.index(row_code)][5] += int(revenue[ind_row])
    for i in result:
        if int(i[3]) != 0:
            i[3] = round(i[3], 3)
        i[4] = int(i[4])
        temp = ChartPie(i)
        i = {'code': temp.code, 'type': temp.name, 'movieCount': temp.movieCount, 'popularity' :temp.popularity, 'voteCount': temp.voteCount, 'revenue': temp.revenue}
        total.append(i)
    # for i in result:
    #     if str(i[3]) == "nan":
    #         print("err", i)
    #         break
    return total
# print((type_info('US')))
def line_chart(code):
    movie_meta2 = movie_meta.sort_values(by=['runtime'], ascending=False).reset_index(drop=True)
    data = movie_meta2['runtime']
    data = pd.DataFrame(data).fillna('')
    data['popularity'] = movie_meta2['popularity'].round(3).values.tolist()
    nation_col = movie_meta2['production_countries']
    lit = []
    for ind, row in enumerate(nation_col):
        if code in row:
            lit.append(ind)
    total_code = []
   
    temp_code = data.filter(items=lit, axis=0).values.tolist()[::-1]
    # print(temp_code)
    check_code = []
    temp_check_code = []
   
    for i in temp_code:
        if i[0] not in check_code:
            check_code.append(i[0])
            temp_check_code.append([i[0],i[1]])
        else:
            temp_check_code[check_code.index(i[0])][1] += i[1]
    for j in temp_check_code:
        temp = ChartLine(j)
        j = {'runtime': temp.runtime, 'popularity': temp.popularity,
        }
        total_code.append(j)
   
    final = {
        'region' : total_code,
    }

    return final
# print(line_chart('VN'))

def histo_chart(code):
    movie_meta3 = movie_meta.sort_values(by=['runtime'], ascending=False).reset_index(drop=True)
    data = movie_meta3['runtime'].fillna('')
    nation_col = movie_meta3['production_countries']
    lit = []
    for ind, row in enumerate(nation_col):
        if code in row:
            lit.append(ind)
    
    data_list = data.filter(items=lit, axis=0).values.tolist()
    # print(data_list)
    final = []
    data_set = set(data_list)
    for i in data_set:
        if i != '':
            final.append([float(i), data_list.count(i)])
    
    total_code = []
    for j in final:
        temp = ChartHisto(j)
        j = {'runtime': temp.runtime, 'movieCount': temp.movieCount,
        }
        total_code.append(j)

    return {
        'data' : sorted(total_code, key=itemgetter('runtime'))
    }
# print(histo_chart('US'))

def pyramid_chart(code):
    # movie_meta = pd.read_csv('movies_metadata.csv', low_memory = False)
    data = movie_meta['release_date'].fillna('')
    nation_col = movie_meta['production_countries']
    lit = []
    for ind, row in enumerate(nation_col):

        if len(data[ind]) > 0:
            if "/" not in data[ind]:
                data[ind] = (data[ind][:4])
            else: data[ind] = data[ind][-4:]
        if code in row:
            lit.append(ind)
    data_list = data.filter(items=lit, axis=0).values.tolist()
    final = []
    final_all = []
    data_set = set(data_list)
    for i in data_set:
        final.append([i, data_list.count(i)])
    data_all = data.values.tolist()
    data_all_set = set(data_all)
    for i in data_all_set:
        final_all.append([i, data_all.count(i)])

    temp_code = sorted(final, key=itemgetter(0))
    temp_all = sorted(final_all, key=itemgetter(0))
    total_code = []
    total_all = []
    for j in temp_code:
        temp = ChartPyramid(j)
        j = {'year': temp.year, 'movieCount': temp.movieCount,
        }
        total_code.append(j)
    for j in temp_all:
        temp = ChartPyramid(j)
        j = {'year': temp.year, 'movieCount': temp.movieCount,
        }
        total_all.append(j)
    return {
        'region' : total_code,
        'all' : total_all,
    }

def heat_chart(code):
    movie_meta = pd.read_csv('movies_metadata.csv', low_memory = False)
    data = movie_meta['release_date'].fillna('')
    nation_col = movie_meta['production_countries']
    lit = []

    for ind, row in enumerate(nation_col):

        if len(data[ind]) >  0:
            
            if "/" not in data[ind]:
                data[ind] = "/".join((data[ind][:7]).split("-"))
                # print(data[ind])
            else: 
                data[ind] = "/".join(data[ind][-7:].split("/")[::-1])
                
            # print(data[ind])
        if code in row:
            lit.append(ind)
    # print(data)
    data_list = data.filter(items=lit, axis=0).values.tolist()
    final = []
    final_all = []
    data_set = set(data_list)
    for i in data_set:
        final.append([i, data_list.count(i)])
    data_all = data.values.tolist()
    data_all_set = set(data_all)
    for i in data_all_set:
        final_all.append([i, data_all.count(i)])

    temp_code = sorted(final, key=itemgetter(0))
    temp_all = sorted(final_all, key=itemgetter(0))
    total_code = []
    total_all = []
    for j in temp_code:
        temp = ChartPyramid(j)
        j = {'year': temp.year, 'count_movie': temp.movieCount,
        }
        total_code.append(j)
    for j in temp_all:
        temp = ChartPyramid(j)
        j = {'year': temp.year, 'count_movie': temp.movieCount,
        }
        total_all.append(j)
    return {
        'min': min(total_code[1]['year'], total_all[1]['year'])[:4],
        'max': max(total_code[-1]['year'], total_all[-1]['year'])[:4],
        code : total_code,
        'all' : total_all[1:],
    }

def pie_process(nation_code):
    movie_meta = pd.read_csv('movies_metadata.csv', low_memory = False)
    result = []
    code = []
    
    df = (movie_meta['genres'])
    data = movie_meta['release_date'].fillna('')
    nation_col = movie_meta['production_countries']
  
    for ind_row, row in enumerate(df):
        if nation_code in nation_col[ind_row]:
            if row != '[]':
                try:
                    row_c = (row[1:-1].replace("{","").replace("}","").split(','))
                except Exception as e:
                    print(e, row)
                row_fi = [i.split(":") for i in row_c]
                for i in range(0, len(row_fi),2):
                    if  'id' in row_fi[i][0][1:-1]:
                        row_code = row_fi[i][1].replace(' ', '')
                        if len(data[ind_row]) > 0:
                            if "/" not in data[ind_row]:
                                data[ind_row] = (data[ind_row][:4])
                            else: data[ind_row] = data[ind_row][-4:]
                        if row_code+data[ind_row] not in code:
                            # print(row_code)
                            code.append(row_code+data[ind_row])
                            result.append([row_code+data[ind_row], row_fi[i+1][1][2:-1], 1])
                        else: 
                            result[code.index(row_code+data[ind_row])][2] += 1
    total = {
        '10': 1,
        '05': 1,
        'now' : 1
    }
    dictAll = {str(i[0][:2]) : {
        '10': 1,
        '05': 1,
        'now' : 1,
        'name': i[1]
        
    } for i in result}
    checkMaxYear = max([int(i[0][-4:]) for i in result])
    
    for i in result:
        if int(i[0][-4:]) == int(checkMaxYear) - 10:
            dictAll[str(i[0][:2])]['10'] += 1
            total['10'] += 1
        if int(i[0][-4:]) == int(checkMaxYear) - 5:
            dictAll[str(i[0][:2])]['05'] += 1
            total['05'] += 1
        if int(i[0][-4:]) == int(checkMaxYear):
            dictAll[str(i[0][:2])]['now'] += 1
            total['now'] += 1
    for i in dictAll:
        # print(dictAll[i])
        dictAll[i]['05'] = int(dictAll[i]['05'])
        dictAll[i]['10'] = int (dictAll[i]['10'])
        dictAll[i]['now'] = int (dictAll[i]['now'])
        dictAll[i]['10'] /= total['10']
        dictAll[i]['10'] *=  100
        dictAll[i]['10'] =  round(dictAll[i]['10'], 2)
        if dictAll[i]['10'] == 100.0:
            dictAll[i]['10'] = 1.0
        dictAll[i]['05'] /= total['05']
        dictAll[i]['05'] *= 100
        dictAll[i]['05'] =  round(dictAll[i]['05'], 2)
        if dictAll[i]['05'] == 100.0:
            dictAll[i]['05'] = 1.0
        dictAll[i]['now'] /= total['now']
        dictAll[i]['now'] *= 100
        dictAll[i]['now'] = round(dictAll[i]['now'], 2)
        if dictAll[i]['now'] == 100.0:
            dictAll[i]['now'] = 1.0
    return { 'data' : [dictAll[j] for j in dictAll]}
# print(bar_chart('US'))
def actor(nation_code):
    # movie_meta = pd.read_csv('movies_metadata.csv', low_memory = False)
    df = movie_meta[['vote_average','vote_count','id','production_countries']]
    actor_dt = pd.merge(df, actor_meta, on='id', how='inner')
    nation_col = actor_dt['production_countries']
    code = []
    result = []
    temp = []
    total = []
    for ind_row, row in enumerate(actor_dt['cast']):
        if nation_code in nation_col[ind_row]:
            if row != '[]':
                try:
                    row_c = (row[1:-1].replace("{","").replace("}","").split(','))
                except Exception as e:
                    print(e, row)
                row_fi = [i.split(":") for i in row_c]
                
                for i in row_fi:
                    if 'name' in ''.join(i):
                        temp.append([ind_row, i[1].replace('\'','').replace('\"','')[1:]])
    for i in temp:
        if i[1] not in code:
            code.append(i[1])
            result.append([i[1], actor_dt['vote_average'][i[0]]*actor_dt['vote_count'][i[0]], actor_dt['vote_count'][i[0]], 1])
        else:
            result[code.index(i[1])][1] += actor_dt['vote_average'][i[0]]*actor_dt['vote_count'][i[0]]
            result[code.index(i[1])][2] += actor_dt['vote_count'][i[0]]
            result[code.index(i[1])][3] += 1
    for i in result:
        if i[2]!=0:
            i[1] = round(i[1]/i[2],3)
    temp1 = (sorted(result, key=itemgetter(3))[::-1][:20])
    for i in temp1:
        total.append({
            'name' : i[0],
            'pointVote' : i[1],
            'movieCount' : i[3]
        })
    return {'data': total}
                
    # print(actor_dt)
# print((type_info('US')))
# print(actor('BR'))