nationals={ 'bird':'peacock',
            'anthem': 'jana gana mana',
            'song': 'Vandhe mataram',
            'Animal':'Tiger',
            'Flower':'Lotus'}
print( nationals['anthem'])
print(nationals.get( 'game'))
print(nationals.keys())
print(nationals.items())
print(nationals.values())



nationals.update({ 'game':'hockey'})
nationals.update({'fruit':'Mango'})
nationals.clear()

for key,values in nationals.items():
    print(key,values)