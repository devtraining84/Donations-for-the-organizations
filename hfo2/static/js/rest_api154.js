document.addEventListener("DOMContentLoaded", function() {
    
   
    function show_id(event)
{
    var ids = get_checked_chexboxes();
    var params = new URLSearchParams();
    ids.forEach(id => params.append("type_ids", id))
    var address = '/get_inst_by_id?'+ params.toString();
    fetch(address)
        .then(response => response.text())
        .then(data => document.getElementById("li").innerHTML = data);

}
function get_checked_chexboxes()
{
    var markedCheckbox = document.querySelectorAll('input[type="checkbox"]:checked');
    var ids = [];
    markedCheckbox.forEach(box => ids.push(box.value));
    console.log(ids);
    return ids;
}



$( document ).ready(function() {
    var li_buttons = $('.rest_api_exe');
    li_buttons.click(show_id);
});


    
   
    });
    
    
    