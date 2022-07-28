fetch('https://save-photos.herokuapp.com/')
  .then((response) => response.json())
  .then((data) => console.log(data));