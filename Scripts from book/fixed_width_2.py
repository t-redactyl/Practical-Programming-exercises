def read_weather_data(r):
    '''Read weather data from reader r in fixed-width format. The field
    widths are:
      4,2,2   YYYMMDD (date)
      2,2,2   DDMMSS (latitude)
      2,2,2   DDMMSS (longitude)
      6,6,6   FF.FFF (temp, deg. C; humidity, %; pressure, kPa)
    The results is a list of tuples, where each tuple is of the form:
    (YY, MM, DD, DD, MM, SS, DD, MM, SS, Temp, Hum, Press)
    '''
    
    fields = ((4, int), (2, int), (2, int),             # date
              (2, int), (2, int), (2, int),             # latitude
              (2, int), (2, int), (2, int),             # longitude
              (6, float), (6, float), (6, float))        # data
    result = []
    
    # For each record
    for line in r:
        start = 0
        record = []
        # For each field in the record
        for (width, target_type) in fields:
            # Convert the text
            text = line[start:start+width]
            field = target_type(text)
            # Add it to the record
            record.append(field)
            # Move on
            start += width
        # Add the completed record to the result
        result.append(record)
    return result
    
    