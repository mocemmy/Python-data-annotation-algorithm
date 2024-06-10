

const isValidJSON = str => {
    try {
      JSON.parse(str);
      return true;
    } catch (e) {
      return false;
    }
  };

  console.log(isValidJSON(`{"name" : "Alice", "favorite_color" : "blue", "age" : 31}`))