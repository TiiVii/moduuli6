
def tervehdi(teksti, kerrat):
    for i in range(kerrat):
        print(teksti)
    return

print('aloitetaan', 'jeboi', sep='/' )
tervehdi('hei', 1)
print('lopetetaan')
tervehdi('hei taas', 3)

#####

def tervehdi():
    print('huoment')
    return

print('aloitetaan')
tervehdi()
print('lopetetaan')

for i in range(3):
   tervehdi()