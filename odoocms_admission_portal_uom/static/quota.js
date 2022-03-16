function quota_change(choice){
    console.log('quota');
     console.log(choice);
    var formData = new FormData();
    formData.append('qouta',choice)

    $.ajax({
         url: "/admissiononline/quota/save",
         type: "POST",
         dataType: "json",
         data: formData,
         contentType: false,
         processData:false,
         success: function(data) {
         },
         error: function(){
            console.log('error');
         }
   });
}