function imgLoaded(event) {
    event.target.parentElement.style.width =
        event.target.getBoundingClientRect().width + 'px'
}


function imgClicked(event) {
    var id = event.target.id
    var rect = event.target.getBoundingClientRect()
    var point = document.querySelector('#'+ id +'-point')
    var el_json = document.querySelector('#' + id.replace(/-img$/, '-json'))
    var el_json_value = JSON.parse(el_json.value)

    el_json_value.point = [
        Math.floor(100*(event.clientX - rect.left)/rect.width),
        Math.floor(100*(event.clientY - rect.top)/rect.height)
    ]

    point.style.left = el_json_value.point[0] + '%'
    point.style.top = el_json_value.point[1] + '%'

    el_json.value = JSON.stringify(el_json_value)

}

function changeURL(event) {
    var id = event.target.id
    var url_prefix = event.target.dataset.url
    var el_json = document.querySelector('#' + id + '-json')
    var el_img = document.querySelector('#' + id + '-img')
    el_img.src = url_prefix + event.target.value

    var el_json_value = JSON.parse(el_json.value)
    el_json_value.pathway = event.target.value
    el_json_value.url = url_prefix + event.target.value
    el_json.value = JSON.stringify(el_json_value)
}
