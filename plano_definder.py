def defind_all_plans(p, grupy_godz, grupy_no, godzina_start=8, pomijane_przedmioty=[]):
    Wiersze = ['8','9','10','11','12','13','14','15','16','17','18','19','20','21']
    kliker_grupa = [0 for i in range(len(p))]
    Gotowe_plany = []
    while True:
        zestaw = []
        #tworzenie zestawu
        for i in range(len(grupy_godz)):
            if p[i] not in pomijane_przedmioty:
                zestaw.append([p[i]+' '+grupy_no[i][kliker_grupa[i]], grupy_godz[i][kliker_grupa[i]]])
        #sprawdzanie zestawu
        for i in range(len(grupy_godz)):
            if p[i] not in pomijane_przedmioty:
                for k in range(len(grupy_godz[i][kliker_grupa[i]])):
                    if grupy_godz[i][kliker_grupa[i]][k][1] >= godzina_start:
                        for ii in range(len(grupy_godz)):
                            if(ii != i and p[ii] not in pomijane_przedmioty):
                                for kk in range(len(grupy_godz[ii][kliker_grupa[ii]])):
                                    if grupy_godz[ii][kliker_grupa[ii]][kk][1] >= godzina_start:
                                        if(grupy_godz[i][kliker_grupa[i]][k][0] == grupy_godz[ii][kliker_grupa[ii]][kk][0]):    #dzień tygodnia
                                            if (grupy_godz[i][kliker_grupa[i]][k][1] <= grupy_godz[ii][kliker_grupa[ii]][kk][1]):
                                                if (grupy_godz[i][kliker_grupa[i]][k][2] > grupy_godz[ii][kliker_grupa[ii]][kk][1]):
                                                    break   #colision
                                    else:
                                        break
                                else:
                                    continue
                                break
                        else:
                            continue
                        break
                    else:
                        break
                else:
                    continue
                break
        else:        
            plan = [['' for j in range(5+1)] for i in range(int(Wiersze[0]),int(Wiersze[-1]))]
            for i in range(len(zestaw)):                                            #przedmiot
                for j in range(len(zestaw[i][1])):                                  #zajęcia
                    for k in range(zestaw[i][1][j][1]-8,zestaw[i][1][j][2]-8):
                        plan[k][0] = Wiersze[k]
                        plan[k][zestaw[i][1][j][0]+1] = zestaw[i][0]
            if plan not in Gotowe_plany:
                Gotowe_plany.append(plan)
        # zmiana zestawu
        kliker_grupa[0] += 1
        for i in range(len(kliker_grupa)):
            if kliker_grupa[i] >= len(grupy_godz[i]):
                if i+1>=len(kliker_grupa):
                    return Gotowe_plany

                if p[i+1] not in pomijane_przedmioty:
                    kliker_grupa[i+1] += 1
                else:
                    kliker_grupa[i+1] = len(grupy_godz[i+1])
                kliker_grupa[i] = 0