function sendImages(){
  console.log("Vamos a enviar");
  //myAwesomeDropzone.processQueue();
}


$( document ).ready(function() {
    console.log( "ready!" );

    $("#labelspecs").click(function() {
        $( "#specs" ).toggle( "fold" );
    });

    Dropzone.options.myAwesomeDropzone = {
        maxFilesize: 0.15,
        dictResponseError: 'Server not Configured',
        acceptedFiles: ".png,.jpg,.gif,.bmp,.jpeg",
        addRemoveLinks: true,
        autoProcessQueue: false,
        init: function() {
          this.on("addedfile", function(file) {
            alert("Added file.");
          });
          this.on("sending", function(file, xhr, formData) {
            // Will send the filesize along with the file as POST data.
            formData.append("final-url", "www.afdfdfdf.com");
          });
        }
    };
});
