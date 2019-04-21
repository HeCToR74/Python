import axios from "axios";


axios.create([axios.defaults.xsrfCookieName = "csrftoken"], [axios.defaults.xsrfHeaderName = 'X-CSRFToken'])
var instance = axios.create({
  headers: {"X-CSRFToken": "csrfToken"}
});