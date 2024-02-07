// Create a new XMLHttpRequest object
let xhr = new XMLHttpRequest();

// Set the request method and the URL
xhr.open('GET', 'https://hellosalut.stefanbohacek.dev/?lang=fr');

// Define what to do when the response is ready
xhr.onload = function() {
  // Parse the JSON response
  let data = JSON.parse(this.responseText);

  // Get the hello value
  let hello = data.hello;

  // Get the DIV#hello element
  let div = document.getElementById('hello');

  // Set the innerHTML of the div to the hello value
  div.innerHTML = hello;
};

// Send the request
xhr.send();

