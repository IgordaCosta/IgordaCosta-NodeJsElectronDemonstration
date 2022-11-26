
function GetValueFromKey (DatabaseDataGotten, Key) {

    return new Promise((resolve, _reject) => {

    

    // console.log(DatabaseDataGotten);
    
    let valueGotten = DatabaseDataGotten[Key];

    // console.log(valueGotten);

    resolve(valueGotten);


  }

  )

}

exports.GetValueFromKey = GetValueFromKey;
