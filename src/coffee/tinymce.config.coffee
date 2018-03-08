# UploadFile = require './file_upload_handler'

# axios = require 'axios'
# UploadFile = (url, form) ->
#     csrfmiddlewaretoken = document.querySelector('input[name="csrfmiddlewaretoken"]').value
#     form.append 'csrfmiddlewaretoken', csrfmiddlewaretoken
#     axios.post url, form

# selectedImage = null

tinymceConfig =
    selector: 'textarea[rich-editor="true"]'
    height: 300
    paste_as_text: true
    force_p_newlines: true
    invalid_elements: 'br,div'
    cleanup : true
    plugins: [
        "advlist autolink lists link image charmap print preview anchor"
        "searchreplace visualblocks code fullscreen"
        "insertdatetime media table contextmenu paste imagetools"
        "wordcount"
        "textcolor colorpicker"
    ]

    toolbar: "insertfile undo redo | styleselect | forecolor backcolor | bold italic | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | link media image | browse | fullscreen"

    # toolbar: "insertfile undo redo | styleselect | forecolor backcolor | bold italic | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | link | browse | fullscreen"

    image_caption: true
    relative_urls: false
    images_upload_url: '/media/'
    init_instance_callback: (editor) ->
        editor.on 'click', (e) ->
            node = tinymce.activeEditor.selection.getNode()
            if node.tagName == 'IMG' and node.getAttribute('src').indexOf('blob:')==-1 then selectedImage = node.getAttribute 'src'


    setup: (editor) ->
        editor.addButton 'browse',
            title: 'Insert files',
            icon: 'browse',
            onclick: ->
                # fileBrowserCallback 'id_content_ifr', 'files', 'type', window
                console.log 'fileBrowserCallback'

        editor.on 'SaveContent', (event) ->
            event.content = event.content
                .replace(/&nbsp;/g, ' ')
                .replace(/\s{2,}/g, ' ')

    ###
    images_upload_handler: (blobInfo, success, failure) ->

        filename = blobInfo.filename()

        if filename.indexOf('imagetool')==0 then filename = selectedImage

        form = new FormData()

        form.append 'image', blobInfo.blob()
        form.append 'filename', filename

        UploadFile("#{window.__MEDIA_MANAGER_PATH__}file_upload_handler", form)
            .then (res) ->
                if(!res.data.failure)
                    return success(res.data.success)
                else
                    return failure()
            .catch (err) ->
                return failure()

    file_browser_callback: (field_name, url, type, win) ->
        console.log field_name, url, type, win
        fileBrowserCallback field_name, url, type, win
    ###

###
fileBrowserCallback = (field_name, url, type, win) ->
    mediaManager = window.__MEDIA_MANAGER_PATH__

    tinymce.activeEditor.windowManager.open
        file: mediaManager
        title: 'Media Manager'
        width: 1000
        height: 600
        resizable: "yes"
        plugins: "media"
        inline: "yes"
        close_previous: "no"

            window: win
            input: field_name
###



module.exports = tinymceConfig
