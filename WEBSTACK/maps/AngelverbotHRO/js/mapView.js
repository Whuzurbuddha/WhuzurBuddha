var map = L.map('map').setView([54.0833784,  12.1550113], 12);
    L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        }).addTo(map);

 
function showData(gebiet, info, coordinate){
   

        for(var i = 0; i < 12; i++){
           var pairs = coordinate[0][i]
           var lat = pairs[1]
           var lon = pairs[0]
           
            L.marker([lat,  lon]).addTo(map)
                .bindPopup(info)
                .openPopup();
                        
        }      
}
		


