$(document).ready(function(){

var granimInstance = new Granim({
    element: '#canvas-basic',
    name: 'radial-gradient',
    direction: 'top-bottom',
    opacity: [1, 1],
    isPausedWhenNotInView: true,
    states : {
        "default-state": {
            gradients: [
              ['#eee','#e9ecef'],
              ['#A7E8D9','#71C0FF']

            ]
        }
    }
});


});
