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
    
    
    
// -------------------------------------------------------------
//     function show_id(event)
// {
//     console.log("najechałeś myszka na element")
//     var id = this.dataset.id;
//     var address = '/get_car_by_type';
//     var data = {'type_id':id};
//     console.log("bede wchodze na adress ".concat(address).concat(" z danym type_id=".concat(data['type_id'])))
//     $.get(address,data, function (data, status) {
//         console.log("pobrałem dane:");
//         console.log(data);
//         $('.cars').html(data);
//         console.log("podmieniłem dane na stronie");
//     });

// }



// $( document ).ready(function() {
//     var li_buttons = $('.type');
//     li_buttons.click(show_id);
// });
// --------------------------------------------------------------



//
// var data = $('form').serializeArray().reduce(function(obj, item) {
    //     obj[item.name] = item.value;
    //     console.log(obj);
    //     return obj;

    // }, {});



