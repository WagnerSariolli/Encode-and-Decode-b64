#Wagner Sariolli
#fri/aug/2017

#----------------------------------------
import base64;
from os import system

system('clear')
#----------------------------------------
def menu():
    print """
  .     .  :     .    .. :. .___---------___.
       .  .   .    .  :.:. _".^ .^ ^.  '.. :"-_. Mark WS Encode base64
    .  :       .  .  .:../:            . .^  :.:\.
        .   . :: +. :.:/: .   .    .        . . .:
 .  :    .     . _ :::/:               .  ^ .  . .:
  .. . .   . - : :.:./.                        .  .:
  .      .     . :..|:                    .  .  ^. .:
    .       . : : ..||        .                . . !:
  .     . . . ::. ::\(                           . :)
 .   .     : . : .:.|. ######              .#######::
  :.. .  :-  : .:  ::|.#######           ..########:
 .  .  .  ..  .  .. :\ ########          :######## :
  .        .+ :: : -.:\ ########       . ########.:
    .  .+   . . . . :.:\. #######       #######..: By Wagner Sariolli
      :: . . . . ::.:..:.\           .   .   ..:
   .   .   .  .. :  -::::.\.       | |     . .:
      .  :  .  .  .-:.":.::.\             ..:
 .      -.   . . . .: .:::.:.\.           .:
.   .   .  :      : ....::_:..:\   ___.  :
   .   .  .   .:. .. .  .: :.:.:\       :
     +   .   .   : . ::. :.:. .:.|\  .:/    Encode      Decode
"""

#----------------------------------------
def main():

    choice = str(raw_input('it inserts a choice >> '))

    if (choice.upper() == 'ENCODE'):
        command = raw_input('It inserts something >> ')
        code = (base64.b64encode("" + command))
        print 'Code = ' + code
    elif (choice.upper() == 'DECODE'):
        command = raw_input('It inserts something >> ')
        code = (base64.b64decode("" + command))
        print 'Decoded = ' + code
    else:
        print 'It inserts something I validate'
#----------------------------------------
menu()
while True:
    main()
