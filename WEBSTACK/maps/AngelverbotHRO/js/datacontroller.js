$(document).ready(function() {

    var data = {
      resource_id: '72cedbae-1045-434a-8800-8313a0c629f4', // die Ressourcen-ID
    };
      
    $.ajax({
      url: 'https://www.opendata-hro.de/api/3/action/datastore_search',
      type: 'GET',
      data: data,
      dataType: 'json',
      success: function(data) {
        var gebiete = []
        var info = []
        var coordinate = []
        var records = data.result.records;
       
        for(var i = 0; i < records.length; i++){
          if(records[i].bezeichnung != null){
            var bezeichnung = records[i].bezeichnung;
            var beschreibung = records[i].beschreibung;
           gebiete.push(bezeichnung)
           info.push(beschreibung)
            var all_coordinates = records[i].geometrie.coordinates;
            for(var j = 0; j < all_coordinates.length; j++){
                coordinate.push(all_coordinates)
            }
          }
        }
        loadData(gebiete, info, coordinate)
      },
      error: function() {
        alert('GOT NO DATA');
      },
    });
    
  });
