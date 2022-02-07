import pygal.maps.fr
import numpy as np
from pygal.style import Style
'''Fuction to get the corresponding neighbour list from the neighbours matrix'''
def neigbours(x,vectDep,Matrix):    
    neigh=[]
    for y in Matrix[x]:
        if (Matrix[x][y]==1):
            neigh.append(y)
    return neigh
'''Creates the matrix vector with the n-tuples and the neighbors matrix''' '''À modifier selon préferences'''
def SetNeighbours(Matrix): 
    Matrixin= []
    Matrixin.append((38,73,74,39,71,69)) #1
    Matrixin.append((59,80,60,77,71,8)) #2
    Matrixin.append((42,71,58,18,23,63))    #3
    Matrixin.append((83,6,5,26,84,13))  #4
    Matrixin.append((4,26,38,73))   #5
    Matrixin.append((83,4,20))  #6
    Matrixin.append((48,30,84,26,38,69,43)) #7
    Matrixin.append((55,51,2,59))   #8
    Matrixin.append((31,11,66)) #9
    Matrixin.append((89,21,52,51,77))   #10
    Matrixin.append((9,31,81,34))   #11
    Matrixin.append((34,30,48,15,46,82,81)) #12
    Matrixin.append((30,84,83,20))  #13
    Matrixin.append((27,61,50)) #14
    Matrixin.append((48,43,63,19,46,12))    #15
    Matrixin.append((17,79,86,87,24))   #16
    Matrixin.append((85,79,16,33))  #17
    Matrixin.append((36,41,45,89,58,3,23))  #18
    Matrixin.append((23,87,24,46,15,63))    #19
    Matrixin.append((13,83,6))  #20
    Matrixin.append((10,89,58,71,39,70,52)) #21
    Matrixin.append((29,56,35)) #22
    Matrixin.append((87,19,63,3,18,36)) #23
    Matrixin.append((17,16,87,19,46,47,33)) #24
    Matrixin.append((39,70,90)) #25
    Matrixin.append((84,4,5,38,69,7))   #26
    Matrixin.append((76,60,96,78,28,61,14)) #27
    Matrixin.append((27,78,91,45,41,72,61)) #28
    Matrixin.append((22,56))    #29
    Matrixin.append((34,12,48,7,26,84,13))  #30
    Matrixin.append((65,32,82,81,11,9)) #31
    Matrixin.append((31,65,64,40,47,82))    #32
    Matrixin.append((17,24,47,40))  #33
    Matrixin.append((11,81,12,30))  #34
    Matrixin.append((50,53,49,44,56,22))    #35
    Matrixin.append((37,41,18,23,87,86))    #36
    Matrixin.append((41,36,86,49,72))   #37
    Matrixin.append((5,73,1,69,7,26,5)) #38
    Matrixin.append((1,71,21,70,25))    #39
    Matrixin.append((33,47,32,64))  #40
    Matrixin.append((72,37,36,18,45,28))    #41
    Matrixin.append((43,69,71,3,63))    #42
    Matrixin.append((48,7,69,42,63,15)) #43
    Matrixin.append((56,35,53,49,85))   #44
    Matrixin.append((91,77,28,41,18,58,89)) #45
    Matrixin.append((15,19,24,47,82,12))    #46
    Matrixin.append((33,40,32,82,46,24))    #47
    Matrixin.append((12,30,7,43,15)) #48
    Matrixin.append((44,53,72,37,86,79,85)) #49
    Matrixin.append((14,61,53,35))  #50
    Matrixin.append((2,77,10,52,55,8))  #51
    Matrixin.append((21,70,88,55,51,10))    #52
    Matrixin.append((49,72,61,50,35,44))    #53
    Matrixin.append((57,67,88,55))  #54
    Matrixin.append((54,88,52,51,8))    #55
    Matrixin.append((29,22,35,44))  #56
    Matrixin.append((67,88,54)) #57
    Matrixin.append((3,71,21,89,45,18)) #58
    Matrixin.append((2,80,62,8))    #59
    Matrixin.append((2,80,76,27,95,77)) #60
    Matrixin.append((14,27,28,72,53,60))    #61
    Matrixin.append((80,59,2))  #62
    Matrixin.append((15,43,42,3,23,19)) #63
    Matrixin.append((40,32,65))   #64
    Matrixin.append((64,32,31)) #65
    Matrixin.append((9,11)) #66
    Matrixin.append((68,88,54,57))  #67
    Matrixin.append((90,70,88,67))  #68
    Matrixin.append((1,71,42,43,7,26,38))   #69
    Matrixin.append((21,39,25,90,88,52))    #70
    Matrixin.append((3,42,69,1,39,21,58))   #71
    Matrixin.append((28,61,53,49,37,41))    #72
    Matrixin.append((74,1,38,5))    #73
    Matrixin.append((73,1)) #74
    Matrixin.append((92,93,94)) #75
    Matrixin.append((80,60,27)) #76
    Matrixin.append((89,10,51,2,60,95,91,45))   #77
    Matrixin.append((95,27,28,91,92))   #78
    Matrixin.append((17,85,28,91,92))   #79
    Matrixin.append((62,59,2,60,76)) #80
    Matrixin.append((11,34,12,82,31))   #81
    Matrixin.append((32,31,81,12,46,47)) #82
    Matrixin.append((13,84,4,6,20)) #83
    Matrixin.append((13,4,26,7,30)) #84
    Matrixin.append((44,49,79,17))  #85
    Matrixin.append((36,37,49,79,16,87))    #86
    Matrixin.append((23,19,24,16,86))   #87
    Matrixin.append((70,90,68,67,57,54,55,52))  #88
    Matrixin.append((58,21,10,77,45))   #89
    Matrixin.append((25,70,88,68))  #90
    Matrixin.append((25,70,88,68))  #91
    Matrixin.append((75,95,78,93))  #92
    Matrixin.append((92,95,94)) #93
    Matrixin.append((77,75,92,93,91))   #94
    Matrixin.append((78,27,60,93,92))   #95
    for i in np.arange(1):
        for j in np.arange(len(Matrixin[i])):
            index=Matrixin[i][j]
            Matrix[i][index-1]=1
    return
Departments = np.zeros(95)
Neighbours = np.zeros((95,95))
SetNeighbours(Neighbours)
'''Fuction to set the colors in red'''
custom_style = Style( 
  #background='transparent',
  #plot_background='transparent',
  #foreground='#53E89B',
  #foreground_strong='#53A0E8',
  #foreground_subtle='#630C0D',
  #opacity='.6',
  #opacity_hover='.9',
  #transition='400ms ease-in',
  #colors=('#E853A0', '#E8537A', '#E95355', '#E87653', '#E89B53'))
  colors=('#0000FF', '#FF0000'))
fr_chart = pygal.maps.fr.Departments(human_readable=True,style=custom_style)
fr_chart.title = 'Population by department'
fr_chart.add('SET TITLE', {'01': Departments[0], '02': Departments[1], '03': Departments[2], '04': Departments[3], '05': Departments[4], '06': Departments[5], '07': Departments[6], '08': Departments[7], '09': Departments[8], '10': Departments[9], '11': Departments[10], '12': Departments[11], '13': Departments[12], '14': Departments[13], '15': Departments[14], '16': Departments[15], '17': Departments[16], '18': Departments[17], '19': Departments[18], '20': Departments[19], '21': Departments[20], '22': Departments[21], '23': Departments[22], '24': Departments[23], '25': Departments[24], '26': Departments[25], '27': Departments[26], '28': Departments[27], '29': Departments[28], '30': Departments[29], '31': Departments[30], '32': Departments[31], '33': Departments[32], '34': Departments[33], '35': Departments[34], '36': Departments[35], '37': Departments[36], '38': Departments[37], '39': Departments[38], '40': Departments[39], '41': Departments[40], '42': Departments[41], '43': Departments[42], '44': Departments[43], '45': Departments[44], '46': Departments[45], '47': Departments[46], '48': Departments[47], '49': Departments[48], '50': Departments[49], '51': Departments[50], '52': Departments[51], '53': Departments[52], '54': Departments[53], '55': Departments[54], '56': Departments[55], '57': Departments[56], '58': Departments[57], '59': Departments[58], '60': Departments[59], '61': Departments[60], '62': Departments[61], '63': Departments[62], '64': Departments[63], '65': Departments[64], '66': Departments[65], '67': Departments[66], '68': Departments[67], '69': Departments[68], '70': Departments[69], '71': Departments[70], '72': Departments[71], '73': Departments[72], '74': Departments[73], '75': Departments[74], '76': Departments[75], '77': Departments[76], '78': Departments[77], '79': Departments[78], '80': Departments[79], '81': Departments[80], '82': Departments[81], '83': Departments[82], '84': Departments[83], '85': Departments[84], '86': Departments[85], '87': Departments[86], '88': Departments[87], '89': Departments[88], '90': Departments[89], '91': Departments[90], '92': Departments[91], '93': Departments[92], '94': Departments[93], '95': Departments[94]})
fr_chart.render_to_file('departments.svg')



    


    