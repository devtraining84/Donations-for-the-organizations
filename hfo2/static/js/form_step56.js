
document.addEventListener("DOMContentLoaded", function() {
    
    var button4 = document.getElementById("button4");
    var bags = document.getElementById("bags");
    var address = document.getElementById("address");
    var city = document.getElementById("city");
    var postcode = document.getElementById("postcode");
    var phone = document.getElementById("phone");
    var date = document.getElementById("date");
    var time = document.getElementById("time");
    var more_info = document.getElementById("more_info");
    var organization = document.getElementById("organization");
  

    
    
    button4.addEventListener('click', function (e) {
        console.log('click on button4');
    
        var data = $('form').serializeArray().reduce(function(obj, item) {
            
            if(document.getElementById(obj.organization) != null){
                var idPost=document.getElementById(obj.organization).innerHTML;
            }
            
            obj[item.name] = item.value;
            console.log(obj);
            bags.innerText = (obj.bags + " workow z darami");
            address.innerText = obj.address;
            city.innerText = obj.city;
            postcode.innerText = obj.postcode;
            phone.innerText = obj.phone;
            date.innerText = obj.date;
            time.innerText = obj.time;
            more_info.innerText = obj.more_info;
            organization.innerHTML =("Dla organizacji: <b>" + idPost + "</b>");

            
            return obj;
    
        }, {});
        
    
    
    });

    






    });
    
    
    
    