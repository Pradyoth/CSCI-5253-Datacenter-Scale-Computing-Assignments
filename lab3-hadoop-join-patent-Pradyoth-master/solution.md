Mapper 1 and Reducer 1  : 
The mapper one will take as input the citation file and the patent file and I am printing the output in the following format: Cited, Citing, State. It takes in both the input files and for the citation file the State will be '-' and for the patent file I am outputting patent id and the respective location. The shuffler then does the job of sorting the output of the mapper using the Cited_Id as the key. The reducer takes the output of the first mapper as its input. In my reducer I am reading line by line and if the location actually exists it stores the location in a local variable, else I'm appending all the citing values to a list. Once I detect that there is a change to the cited_id I  iterate through the citing list and print out the cited_id, citing_id and the location. So what reducer1 is doing is basically doing a join based on the cited_id as the key value. It prints out cited_id citing_id and state of the cited_id.  

Mapper 2 and Reducer 2 :
The mapper2 takes as input the output of the first reducer( in the format cited_id citing_id and state of cited_id) and the patent file. In my mapper 2 I'm doing a split to distinguish between the 2 files. If the number of columns is 3(Output of reducer1 file) it prints out the citing as the key and creates a string concatinating the cited and the cited state. Citing  'Cited, Cited State'. In the else case(which means its the patent file) I'm printing it out in the following format: Patent_id Patent_state and have added one more column(just to distinguish between the earlier print statement). So basically all the same citing keys will end up at the same reducer. 
The reducer 2 takes the output of mapper2 and does a split on the tab spaces. If the number of columns is 2 I'm appending 'Cited, Cited State' into an array citing_id_list. If the number of columns is 3 (it means its the patent file information) it constructs a dictionary with key as the patent id and value as the respective location. Also here I  added an additional check condition to see if the citing_id has changed since the last time. If the citing_id has changed then I check to see the contents of the citing_id_list and then compare the 2 respective states (citing_id state and cited_id state) If they are same increment the count. Finally I'm printing out the citing_id and the count, reset the count and the citing_id_list and go about the next iterations. Reducer 2 will output the patent_id and the total number of same state citations that patent_id has. 

Mapper 3 and Reducer 3:
My mapper 3 will just print the patent_id and the count of the number of occurences of the patent_id. Also It will output the patent information. 
The reducer 3 has two dictionaries and once it compares the corresponding values it appends the count of the number of occurences to the patent dictionary. 

As part of the colloboration policy I discussed ideas and the way to approach the problem with Vandana Sridhar from Data Center Scale Computing. 





