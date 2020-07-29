function findProp(z){
        var prop = z.effect.numProperties;
        for (j = 1; j <= prop; j++){
            var propName = z.effect.property(j).name.toLowerCase();
            if (propName.indexOf(userText) != -1){
                z.effect.property(j).remove();
                findProp(z);
                }
            }
    }

function delEffects(){
    app.beginUndoGroup("Delete Effects")
    for (i = 0; i<layersLen; i++){
        findProp(x.selectedLayers[i]);
        }
    app.endUndoGroup
}

var x = app.project.activeItem;
if (x == null || (x instanceof CompItem) == false){
    alert('Composition and layers must be selected');
    }else{
        var layersLen = x.selectedLayers.length;
        if (layersLen == 0){
            alert('Layers must be selected');
        }else{
            var userText = prompt("enter effect name", "fill").toLowerCase();
            delEffects()
            alert('done!');
            }
        }
