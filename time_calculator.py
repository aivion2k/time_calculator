def add_time(start, duration, d= 'Day' ):

  # int of hour
  # int of minutes 
  # print sth like this:
  # str(int_hour) + ":"+str(int_min)
  # if PM and new hour > 12, then int_hour - 12 <- new day and we switch PM to AM

  
  # future me here, it was harder than I expected xd

    # function to change 0/1
    def change(l):
      if l==0:
        return 1
      elif l==1:
        return 0

    # list of days and ampm, reading day from input
    ampm_list = ['AM','PM']
    


    # split input 
    tmp_list = start.split(' ')
    time_list = tmp_list[0].split(':')
    dur_list = duration.split(':')
    
    # am/pm according to input
    if tmp_list[1] == "AM":
      ampm = 0
    else:
      ampm = 1
    
    tmp_ampm = ampm
    

    # ints
    hours = int(time_list[0])
    mins = int(time_list[1])

    d_hours = int(dur_list[0])
    d_mins = int(dur_list[1])

    # adding inputs
    hours += d_hours
    mins += d_mins

    
    
    add_day = 0
    next_day =''
    # counting days and preparing the correct day index
    if hours>24:
      add_day = hours // 24


    # reducing hours to max 12, counting and changing am/pm
    if hours>12:
      
      while hours>12:
        hours-=12
        ampm=change(ampm)
      
        
    
    # same with minutes and if minutes change over 12hrs
    if mins>60:
      mins-=60
      hours +=1

      if hours>12:
        hours-=12
        ampm=change(ampm)

    
    if tmp_ampm>ampm:
      add_day+=1
    
    if hours==12 and ampm==1:
      add_day+=1    
      ampm=change(ampm)
    
    if hours==12 and tmp_ampm==0:
      ampm=1
      
    
      
    # next day, n days later
    if add_day>1:
      next_day = ' ({} days later)'.format(add_day)
    elif add_day==1:
      next_day = ' (next day)' 
      

    # prep output list and add '0' if min<10
    new_time_list = [str(hours),str(mins)]
    if len(new_time_list[1]) == 1:
      new_time_list[1] = '0'+new_time_list[1]

    

    if d!='Day':
      day_list =['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
      d=d.lower()
      day = day_list.index(d)+1

      
      day+=add_day
      if day>7:
        while day>7:
          day-=7
      

      string_day = day_list[day-1].title()

      new_time = new_time_list[0] + ':' + new_time_list[1] + ' ' + ampm_list[ampm] + ', ' + string_day + str(next_day)
    else:
      new_time = new_time_list[0] + ':' + new_time_list[1] + ' ' + ampm_list[ampm] + str(next_day)

    print(new_time)
    return new_time
