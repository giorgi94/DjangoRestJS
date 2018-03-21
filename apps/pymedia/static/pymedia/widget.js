function imgLoaded(event) {
    event.target.parentElement.style.width =
        event.target.getBoundingClientRect().width + 'px'
}


function imgClicked(event) {
    var rect = event.target.getBoundingClientRect()
    var point = document.querySelector('#'+event.target.id+'-point')
    
    point.style.left = Math.floor(100*(event.clientX - rect.left)/rect.width) + '%'
    point.style.top = Math.floor(100*(event.clientY - rect.top)/rect.height) + '%'
}
