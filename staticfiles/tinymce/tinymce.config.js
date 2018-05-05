(function() {
    var selectedImage = null;

    var tinymceConfig = {
        selector: 'textarea[rich-editor="true"]',
        height: 300,
        paste_as_text: true,
        force_p_newlines: true,
        invalid_elements: 'br,div',
        cleanup: true,
        plugins: ["advlist autolink lists link image charmap print preview anchor", "searchreplace visualblocks code fullscreen", "insertdatetime media table contextmenu paste imagetools", "wordcount", "textcolor colorpicker"],
        toolbar: "insertfile undo redo | styleselect | forecolor backcolor | bold italic | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | link media image | browse | fullscreen",
        image_caption: true,
        relative_urls: false,
        images_upload_url: '/media/',
        /*
        init_instance_callback: function(editor) {
            return editor.on('click', function(e) {
                var node;
                node = tinymce.activeEditor.selection.getNode();
                if (node.tagName === 'IMG' && node.getAttribute('src').indexOf('blob:') === -1) {
                    return selectedImage = node.getAttribute('src');
                }
            });
        },
        setup: function(editor) {
            editor.addButton('browse', {
                title: 'Insert files',
                icon: 'browse',
                onclick: function() {
                    fileBrowserCallback('id_content_ifr', 'files', 'type', window);
                    return console.log('fileBrowserCallback');
                }
            });
            return editor.on('SaveContent', function(event) {
                return event.content = event.content.replace(/&nbsp;/g, ' ').replace(/\s{2,}/g, ' ');
            });
        },*/
        /*
        images_upload_handler: function(blobInfo, success, failure) {
            var filename, form;
            filename = blobInfo.filename();
            if (filename.indexOf('imagetool') === 0) {
                filename = selectedImage;
            }
            form = new FormData();
            form.append('image', blobInfo.blob());
            form.append('filename', filename);
            return UploadFile(`${window.__MEDIA_MANAGER_PATH__}file_upload_handler`, form).then(function(res) {
                if (!res.data.failure) {
                    return success(res.data.success);
                } else {
                    return failure();
                }
            }).catch(function(err) {
                return failure();
            });
        },
        file_browser_callback: function(field_name, url, type, win) {
            console.log(field_name, url, type, win);
            return fileBrowserCallback(field_name, url, type, win);
        }*/
    };

    /*
    var fileBrowserCallback = function(field_name, url, type, win) {
        var mediaManager;
        mediaManager = window.__MEDIA_MANAGER_PATH__;
        return tinymce.activeEditor.windowManager.open({
            file: mediaManager,
            title: 'Media Manager',
            width: 1000,
            height: 600,
            resizable: "yes",
            plugins: "media",
            inline: "yes",
            close_previous: "no"
        }, {
            window: win,
            input: field_name
        });
    };*/

    tinymceConfig;
    tinymce.init(tinymceConfig);
})();
