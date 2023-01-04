import re
def reference_dic_needed(the_frame):
    needed_data_dic = {
    'locality' : 'locality',
    'Type_property' : 'property_type',
    'Price' : 'Price, ',
    'Sale_type' : 'sale_type',
    'Number_bedrooms' : "bedroom",
    'Living_area' : '\\n Living area\\n , ',
    'fully_equipped_kitchen' : 'Kitchen type, ',#Yes no
    'Furnished' : 'Furnished, ',
    'terrace' : 'Terrace surface, ',
    'garden' : 'Garden surface, ', 
    'surface_land' : 'size_of_house',
    'surface_area_plot' : 'Surface of the plot, ',
    'facades_number' : '\\n Number of frontages\\n , ',
    'Swimming_pool' : '\\n Swimming pool\\n , ',
    'building_state' : '\\n Building condition\\n , ',
    'fire_place' : 'How many fireplaces?, '
    }
    last_frame = {}
    only_number_cat = ['Living_area','surface_area_plot','surface_land','facades_number','garden','terrace','Price'] 
    for key,value in needed_data_dic.items() :
        last_frame[key] = the_frame[value]
        #only number
        if key in only_number_cat : 
            for i,value in enumerate(last_frame[key]) :
                if value =='None' :
                    pass
                else : 
                    result = re.sub(r'[^\d]', '',value)
                    last_frame[key][i] = result.strip()
        #only letter 
        elif key not in only_number_cat :
            for i,value in enumerate(last_frame[key]) :
                if value =='None' :
                        pass
                else : 
                    result = re.sub(r'[^\w\s\-]', '', value)      
                    last_frame[key][i] = result.strip()
        #Special condition with value
        if key == "Price" :
            #keep only the price
            for i,price in enumerate(last_frame[key]) :
                if len(price) > 8 : 
                    result = price[:int(len(price)/2)]
                last_frame[key][i] = result.strip()

        
            

    
    return last_frame
def clean_escape_characters(string):
    return re.sub(r'\\n|\\x..', '', string)