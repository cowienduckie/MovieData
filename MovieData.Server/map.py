
from datetime import datetime
import pandas as pd
from operator import itemgetter

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
    movie_meta = pd.read_csv('movies_metadata.csv', low_memory = False)
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
                if  'code' in row_fi[i][0][1:-1]:
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
    movie_meta = pd.read_csv('movies_metadata.csv', low_memory = False).sort_values(by=['popularity'], ascending=False).reset_index(drop=True)
    data = (movie_meta[['imdb_id','budget', 'original_title', 'overview', 'popularity', 'vote_average', 'release_date', 'production_countries']])
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
    movie_meta = pd.read_csv('movies_metadata.csv', low_memory = False)
    result = []
    total = []
    code = []
    df = (movie_meta['genres'])
    vote_a = movie_meta['popularity']
    vote_c = movie_meta['vote_count']
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
                    # print((row_fi[i][0]))
                    if  'id' in row_fi[i][0][1:-1]:
                        row_code = row_fi[i][1].replace(' ', '')
                        # print(row_code, row_fi[i][1], row_fi[i][1][1:-1])
                        # print(row_fi[i][1])
                        if row_code not in code:
                            # print(row_code)
                            code.append(row_code)
                            result.append([row_code, row_fi[i+1][1][2:-1], 1, vote_a[ind_row] , vote_c[ind_row]])
                        else: 
                            result[code.index(row_code)][2] += 1
                            result[code.index(row_code)][3] += vote_a[ind_row] 
                            result[code.index(row_code)][4] += vote_c[ind_row]
    for i in result:
        if int(i[3]) != 0:
            i[3] = round(i[3], 3)
        i[4] = int(i[4])
        temp = ChartPie(i)
        i = {'code': temp.code, 'type': temp.name, 'movieCount': temp.movieCount, 'popularity' :temp.popularity, 'voteCount': temp.voteCount}
        total.append(i)
    # for i in result:
    #     if str(i[3]) == "nan":
    #         print("err", i)
    #         break
    return total
# print((type_info('US')))
def line_chart(code):
    movie_meta = pd.read_csv('movies_metadata.csv', low_memory = False).sort_values(by=['runtime'], ascending=False).reset_index(drop=True)
    data = movie_meta['runtime']
    data = pd.DataFrame(data).fillna('')
    data['popularity'] = movie_meta['popularity'].round(3).values.tolist()
    nation_col = movie_meta['production_countries']
    lit = []
    
    for ind, row in enumerate(nation_col):
        # data['popularity'][ind] = round(data['popularity'][ind], 3)
        if code in row:
            lit.append(ind)
    
    total_code = []
    total_all = []
    temp_all = data.head(len(lit)).values.tolist()[::-1][1:]
    temp_code = data.filter(items=lit, axis=0).values.tolist()[::-1][1:]
    # print(temp_code)
    for j in temp_code:
        temp = ChartLine(j)
        j = {'runtime': temp.runtime, 'popularity': temp.popularity,
        }
        total_code.append(j)
    for j in temp_all:
        temp = ChartLine(j)
        j = {'runtime': temp.runtime, 'popularity': temp.popularity, 
        }
        total_all.append(j)
    final = {
        'region' : total_code,
        'all': total_all
    }

    return final
# print(line_chart('VN'))

def histo_chart(code):
    movie_meta = pd.read_csv('movies_metadata.csv', low_memory = False).sort_values(by=['runtime'], ascending=False).reset_index(drop=True)
    data = movie_meta['runtime'].fillna('')
    nation_col = movie_meta['production_countries']
    lit = []
    for ind, row in enumerate(nation_col):
        if code in row:
            lit.append(ind)
    
    data_list = data.filter(items=lit, axis=0).values.tolist()
    final = []
    data_set = set(data_list)
    for i in data_set:
        final.append([i, data_list.count(i)])
    
    total_code = []
    for j in final:
        temp = ChartHisto(j)
        j = {'runtime': temp.runtime, 'movieCount': temp.movieCount,
        }
        total_code.append(j)

    return {
        'data' : total_code
    }
# print(histo_chart('US'))

def pyramid_chart(code):
    movie_meta = pd.read_csv('movies_metadata.csv', low_memory = False)
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

# print(bar_chart('US'))