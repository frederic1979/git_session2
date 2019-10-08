import pyforms
from   pyforms.basewidget import BaseWidget
from   pyforms.controls import ControlText
from   pyforms.controls import ControlButton
from   pyforms.controls import ControlCombo
from   pyforms.controls import ControlSlider
from   pyforms.controls import ControlNumber

class NourrissonStep3(BaseWidget):

    def __init__(self):
        super(NourrissonStep3, self).__init__('Suivi nourrisson Step 3')

        #Definition of the forms fields
        self._gender        = ControlCombo('Genre')
        self._gender.add_item("Fille", "f")
        self._gender.add_item("Garçon", "g")

        self._age               = ControlSlider("Age (en mois)")
        self._age.min           = 0
        self._age.max           = 60
        
        self._weight            = ControlNumber("Poids (en kg)")
        self._weight.min        = 0
        self._weight.max        = 50
        self._weight.decimals   = 1
        self._weight.step       = 0.1
        self._weight.value      = 0.0

        self._height            = ControlNumber("Taille (en cm)")
        self._height.min        = 0
        self._height.max        = 200
        self._height.decimals   = 1
        self._height.step       = 0.1
        self._height.value      = 0.0

        self._skull         = ControlNumber("Pérmiètre cranien (en cm)")
        self._skull.min        = 0
        self._skull.max        = 100
        self._skull.decimals   = 1
        self._skull.step       = 0.1
        self._skull.value      = 0.0   

        #Define the button action
        self._button        = ControlButton('Vérifier les constantes')
        self._button.value  = self.__buttonAction

        BaseWidget.isFullScreen = False

    def __buttonAction(self):
        print("A faire")

#Execute the application
if __name__ == "__main__": pyforms.start_app( NourrissonStep3 )