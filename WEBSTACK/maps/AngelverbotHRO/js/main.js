function loadData(gebiete, info, coordinate) {
    var select = document.getElementById("gebiete");
    for (var i = 0; i < gebiete.length; i++) {
      var option = document.createElement("option");
      option.value = i;
      option.text = gebiete[i];
      select.add(option);
      option.addEventListener("click", function(event){
        //deleteMarker();
        var selectedOption = event.target.value;  
        if(info[selectedOption] == null){
          info[selectedOption] = gebiete[selectedOption]
        }
        showData(gebiete[selectedOption], info[selectedOption], coordinate[selectedOption])
      })
    }
  }
 
