# Get user input:
bouwlaag_input = QInputDialog().getText(None, "Input bouwlaag", "Vul de bouwlaag in\n\n-2, -1, 0, 1, 2, etc... (DEFAULT: 0)")[0]
categorie_dbk_input = QInputDialog().getText(None, "Input categorie DBK", "Vul de categorie voor de DBK in\n\nalgemeen (sneltoets: a) (DEFAULT)\nspoor (sneltoets: s)\nmetro (sneltoets: m)")[0]

# Check values for bouwlaag_input
try: 
    # This must be an integer
    int(bouwlaag_input)
except ValueError:
    # Value will be set to 0 (defeault) when not an integer
    bouwlaag_input = 0

# Check and map values for categorie_dbk_input
if categorie_dbk_input == 'a' or categorie_dbk_input == 'algemeen':
    categorie_dbk_input = 'algemeen'
elif categorie_dbk_input == 's' or categorie_dbk_input == 'spoor':
    categorie_dbk_input = 'spoor'
elif categorie_dbk_input == 'm' or  categorie_dbk_input == 'metro':
    categorie_dbk_input = 'metro'
else:
    categorie_dbk_input = 'algemeen'

# Get layers from the canvas
layers = iface.mapCanvas().layers()

# Skip the first layer (Status)
iterlayers = iter(layers)
next(iterlayers)

# Set filter according to user input:
for layer in iterlayers:
    try:
        # Save edits that are made in the layers
        iface.vectorLayerTools().saveEdits(layer)
        # Stop editing mode of the layers (otherwise, the filter will not be applied on the layer)
        iface.vectorLayerTools().stopEditing(layer, False)
    except TypeError:
        pass


    layer.setSubsetString('"bouwlaag" = {} and "categorie_dbk" = \'{}\''.format(bouwlaag_input, categorie_dbk_input))

print("\n=============================================\n-- Bouwlaag / verdiepingen gefilterd op: {}\n-- Categorie gefilterd op: {}\n=============================================".format(bouwlaag_input, categorie_dbk_input))

