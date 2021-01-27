import csv

def Write_Player_Links(filename, links_list): #only for base player url links
    with open(filename, 'a') as f:
        writer = csv.writer(f)
        count = 1
        for link in links_list:
            writer.writerow([link])
            if count % 100 == 0:
                print('Processed pics for %d out of %d links' % (count,len(links_list)))
            count+=1
