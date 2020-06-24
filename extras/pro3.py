details={'name':[],'roll':[],'marks':[]}
x=int(input('enter no of students'))
for i in range(x):
    details['name'].append(input('name: '))
    details['roll'].append(input('roll: '))
    details['marks'].append(eval(input('marks: ')))
print(details)
#to show details of highest marks
ind=details['marks'].index(max(details['marks']))
for key in details.keys():
    print(key,':',details[key][ind])
avg=sum(details.get('marks'))/x
print('average marks is',avg)
#to remove details of lowest marks
ind1=details['marks'].index(min(details['marks']))
for key in details.keys():
    print(details[key].pop(ind))
print(details)
