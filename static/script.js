let watchlistButtonClickListener;
// let watchlist = JSON.parse(sessionStorage.getItem('watchlist')) || [];
let watchlist = document.getElementById('watchlist');

let userId = document.getElementById('userId')
userId=parseInt(userId.innerText);
let name= document.getElementById('name')
BASE_URL='http://127.0.0.1:5000'




// localStorage.setItem('user', JSON.stringify(userId));


async function retrieveQuote() {

  let user_input = document.getElementById('ticker');
  let ticker = user_input.value.toUpperCase();

  if (ticker === '') {
    // Handle empty input (e.g., display an alert or a warning message)
    alert('Input cannot be empty');
    return; // Stop the function if the input is empty
  }
  //check api for vaid ticker
  try {
    let url = `http://127.0.0.1:5000/quote/${ticker}`;
    response = await axios.get(url);
    user_input.value = '';

    return displayQuote(response, ticker);

  } catch {
    alert('invalid ticker');
    return 1;
  }

};

function displayQuote(response, ticker) {

  const displayContainer = document.getElementById('quote-section');
  document.getElementById('symbolField').textContent = ticker;
  price = document.getElementById("priceField");
  price.textContent = response.data.regularMarketPrice.toFixed(2);
  changeD = document.getElementById('changeField');
  changeD.textContent = response.data.regularMarketChange.toFixed(2);
  changeP = document.getElementById('Pctchange');
  changeP.textContent = response.data.regularMarketChangePercent.toFixed(2);
  document.getElementById('nameField').textContent = response.data.shortName;

  if (response.data.regularMarketChange > 0) {
    price.className = 'positive';
    changeD.className = 'positive';
    changeP.className = 'positive';
  } else {
    price.className = 'negative';
    changeD.className = 'negative';
    changeP.className = 'negative';

  }

  let ticker_type = response.data.quoteType;
  const watchlistButton = document.getElementById('add');
  watchlistButton.removeEventListener('click', watchlistButtonClickListener);

  // Attach a new click event listener
  watchlistButtonClickListener = () => addToWatchlist(response.data, ticker);
  watchlistButton.addEventListener('click', watchlistButtonClickListener);

  function handleWatchlistButtonClick(data, ticker) {
    // Call addToWatchlist with the correct parameters
    watchlistButton.removeEventListener('click', handleWatchlistButtonClick);

    addToWatchlist(data, ticker);
  }
}



async function addToWatchlist(data, ticker) {

  url=`${BASE_URL}/watchlist`

  let params =
  {
    "user_id": userId,
    "ticker_code": ticker,
  };
  let response = await axios.post(url, params)
  .then(response => {
    console.log('Response from server:',response)

  displayQuoteInWatchlist(ticker, data);
  });

};

function displayQuoteInWatchlist(ticker, data) {
  let table = document.getElementById('watchlist-table');
  const row = document.createElement('tr');
  const symbolCell = document.createElement('td');
  symbolCell.textContent = ticker;
  symbolCell.id = ticker;
  console.log('element id is: ',symbolCell.id)
  row.appendChild(symbolCell);

  const priceCell = document.createElement('td');
  priceCell.textContent = data.regularMarketPrice;
  row.appendChild(priceCell);



  const changeCell = document.createElement('td');
  changeCell.textContent = data.regularMarketChange;
  row.appendChild(changeCell);

  const PctchangeCell = document.createElement('td');
  PctchangeCell.textContent = data.regularMarketChangePercent;
  row.appendChild(PctchangeCell);

  if (data.regularMarketChange > 0) {
    changeCell.className = 'positive';
    priceCell.className = 'positive';
    PctchangeCell.className = 'positive';
  } else {
    changeCell.className = 'negative';
    priceCell.className = 'negative';
    PctchangeCell.className = 'negative';

  }


  const nameCell = document.createElement('td');
  nameCell.textContent = data.shortName;
  row.appendChild(nameCell);

  let removeButton = document.createElement('button');
  removeButton.textContent = 'Remove';

  removeButton.id = 'remove';
  row.appendChild(removeButton);
  removeButton.onclick = function () {
    removeTickerFromDOMAndLocalStorage(row, ticker);
  };

  table.appendChild(row);


  addTickerToDatabase(ticker, data.shortName, data.quoteType, userId);


}




document.addEventListener('DOMContentLoaded', (event) => {
  // Select the button by its ID
  const quoteButton = document.getElementById('quote');

  // Add click event listener to the button
  quoteButton.addEventListener('click', (event) => {
    // Prevent the default action of the event (e.g., form submission)
    event.preventDefault();

    // Call the validateTicker function
    retrieveQuote();
  });
});


function removeTickerFromDOMAndLocalStorage(row, ticker) {
  row.parentNode.removeChild(row);
  watchlist = watchlist.filter(symbol => symbol !== ticker);
  // sessionStorage.setItem('watchlist', JSON.stringify(watchlist));
  console.log('remove', row, ticker);
  removeTickerFromDb(ticker);




}





document.addEventListener('DOMContentLoaded', (event) => {
  // Select the button by its ID
  const removeButton = document.getElementById('remove');

  // Add click event listener to the button
  removeButton.addEventListener('click', (event) => {
    // Prevent the default action of the event (e.g., form submission)
    event.preventDefault();

    // Call the validateTicker function
    removeTicker();
  });
});






async function addTickerToDatabase(ticker, tickerName, tickerType, userId) {
  let params =
  {

    "ticker_code": ticker,
    "ticker_name": tickerName,
    "ticker_type": tickerType,
    "user_id": userId

  };
  let url = 'http://127.0.0.1:5000/add_ticker';

  //if ticker is NOT in Database - make the api call else return 0
  let response = await axios.post(url, params)
    .then(response => {
      console.log('Response from server:', response);
    });
  console.log(response)
  return response;
}


async function removeTickerFromDb(ticker) {

  let url = `http://127.0.0.1:5000/delete_ticker/${ticker}`;


  let response = await axios.post(url)
    .then(response => {
      console.log('Response from server:', response);
    });
  // console.log(response)
  return updateWatchlist();



}



// document.getElementById('zodiac-signs').addEventListener('change', function () {
//   var selectedSign = this.value;
//   console.log(selectedSign);
//   let url = `http://127.0.0.1:5000/horoscope/${selectedSign}`;
//   axios.get(url)
//     .then(function (response) {

//       let reading = document.getElementById('todays-horoscope');
//       reading.innerHTML = `${selectedSign} - ${response.data}`;
//     })
//     .catch(function (error) {
//       console.error(error); // Handle errors
//     });


// });


// document.getElementById('btn-city').addEventListener('click', getWeather);

// function getWeather() {

//   let city = document.getElementById('input-city').value;
//   let url = `http://127.0.0.1:5000/weather/${city}`;
//   axios.get(url)
//     .then(function (response) {
//       // let weather=document.getElementById('todays-weather')
//       // weather.innerHTML=`${city}-${response.data}`

//       let location = response.data.location.name;
//       let temp = response.data.data.values.temperature;
//       let humidity = response.data.data.values.humidity;
//       let precipitation = response.data.data.values.precipitationProbability;

//       document.getElementById("location").innerHTML = location;
//       document.getElementById("temp").innerHTML = temp;
//       document.getElementById("humidity").innerHTML = humidity;
//       document.getElementById("precipitation").innerHTML = precipitation;

//       document.getElementById('todays-weather');

//     })
//     .catch(function (error) {
//       console.error(error); // Handle errors
//     });



// }

// async function get_marketSummary() {
//   let table = document.getElementById('market-summary');
//   url = 'http://127.0.0.1:5000/market_summary';

//   response = await axios.get(url)
//     .then(function (response) {

//       for (let item of response.data) {
//         var row = table.insertRow();

//         var cell1 = row.insertCell(0);
//         var cell2 = row.insertCell(1);
//         var cell3 = row.insertCell(2);
//         var cell4 = row.insertCell(3);

//         if (item.longName) {
//           cell1.innerHTML = item.longName;

//         } else {
//           cell1.innerHTML = item.shortName;
//         }
//         cell2.innerHTML = item.regularMarketPrice.fmt;
//         cell3.innerHTML = item.regularMarketChange.fmt;
//         cell4.innerHTML = item.regularMarketChangePercent.fmt;


//       }

//     });

//   // add listener to reload
// }

// async function get_news() {
//   let headlines = document.getElementById('news');
//   url = 'http://127.0.0.1:5000/us_news';
//   await axios.get(url)
//     .then(function (response) {

//       response.data.news.forEach(story => {
//         const row = document.createElement('div');
//         row.classList.add('news-row');

//         const link = document.createElement('a');
//         link.href = story.link;
//         link.textContent = story.title;
//         link.target = "_blank"; // Open in new tab

//         row.appendChild(link);
//         headlines.appendChild(row);
//       });

//     })
//     .catch(function (error) {
//       console.error(error); // Handle errors
//     });

// }
// async function jokeMe() {
//   url = 'http://127.0.0.1:5000/joke';
//   let joke = document.getElementById('joke');
//   await axios.get(url)
//     .then(function (response) {
//       joke.innerHTML = response.data;


//     });
// }

// const joker = document.getElementById('joke-me');

// joker.addEventListener('click', jokeMe);




// async function getEcoNums() {
//   url = 'http://127.0.0.1:5000/economic_data';
//   let econTable = document.getElementById('ecoStats');
//   await axios.get(url)
//     .then(function (response) {

//       for (let item in response.data) {

//         // Create a new row
//         const row = document.createElement('tr');

//         // Create the first cell for the indicator name
//         const nameCell = document.createElement('td');
//         nameCell.textContent = item;
//         row.appendChild(nameCell);

//         // Create the second cell for the indicator value
//         const valueCell = document.createElement('td');
//         valueCell.textContent = response.data[item];
//         row.appendChild(valueCell);

//         // Append the new row to the table
//         econTable.appendChild(row);
//       }
//     });



// }
// async function get_econ_calendar() {
//   url = 'http://127.0.0.1:5000/calendar';

//   response = await axios.get(url);
//   display_econ_calendar(response);
// }

// function display_econ_calendar(data) {
//   const container = document.getElementById('econ-calendar');
//   const table = document.getElementById('eco-releases');
//   data.data.map((el) => {
//     for (const [key, value] of Object.entries(el)) {

//       console.log('key', key, 'value', value);
//       const row = document.createElement('tr');
//       const keyCell = document.createElement('td');
//       keyCell.textContent = key;
//       row.append(keyCell);
//       const valueCell = document.createElement('td');
//       if (el.value !== 'NA') {
//         const link = document.createElement('a');
//         link.href = value;
//         link.textContent = value;
//         link.target = "_blank";
//         valueCell.append(link);
//       } else {
//         valueCell.textContent = 'NA';
//       }
//       row.append(valueCell);
//       table.appendChild(row);

//     }
//   });
//   container.appendChild(table);

// }


async function getWatchlist(id) {


  url = `http://127.0.0.1:5000/get_watchlist/${id}`;


  let response = await axios.get(url);
  console.log('user id is', id);
  console.log('getWatchlist returns: ', response.data);
  watchlist = response.data;

  return watchlist;



}




// window.addEventListener('load', getWatchlist(userId));


async function refreshWatchlist(watchlist) {
  console.log('sending to update', watchlist);

  let url = 'http://127.0.0.1:5000/update_watchlist/';
  try {
    const response = await axios.post(url, { watchlist: watchlist });
    console.log('Response from server:', response);
    for(let item in response){
      console.log('id is ',item.id)
      console.log('data: ',item['regularMarketPrice'])
    }
    for (let item of watchlist) console.log(item)

  }
  catch (error) {
    console.error('Error while sending data:', error);
    // Handle error appropriately. Maybe return null or a custom error object.
    return null;
  }
}



//create function to  replace watchlist in DOM with the refreshed watchlist
// get ticker and watchlist from refreshWatchlist
//assign a ticker  id to each element



document.addEventListener('DOMContentLoaded', async () => {
  // Initialize event listeners and fetch initial data
  document.getElementById('quote').addEventListener('click', retrieveQuote);
//   document.getElementById('zodiac-signs').addEventListener('change', fetchHoroscope);
//   document.getElementById('btn-city').addEventListener('click', getWeather);
//   document.getElementById('joke-me').addEventListener('click', fetchJoke);

  // Fetch initial data for various sections
//   await getWatchlist(userId);
//   await get_marketSummary();
//   await get_news();
//   await getEcoNums();
//   await get_econ_calendar();
});





document.addEventListener('DOMContentLoaded', function() {
  // Attach an event listener to each remove button
  document.querySelectorAll('.wl-remove').forEach(function(button) {
      button.addEventListener('click', function() {
          var symbol = this.getAttribute('data-symbol');
          var row = this.closest('tr'); // Find the closest parent <tr> element
          removeItem(symbol, row);
      });
  });
});

function removeItem(symbol, row) {
  console.log("Removing item:", symbol);

  try {
      // Attempt to remove the ticker from the database
      removeTickerFromDb(symbol);

      // If successful, remove the row from the DOM
      row.remove();
  } catch (error) {
      // Handle error (e.g., ticker couldn't be removed from the database)
      console.error("Error removing ticker:", error);
      // Optionally, show an error message to the user
  }
}

async function removeTickerFromDb(symbol) {
  // Your AJAX call or fetch request to remove the ticker from the database
  // Example (update the URL and method as per your server-side setup):
  url=`${BASE_URL}/delete_ticker/${symbol}`
  const response = await axios.post(url);
  return response
}

// function refreshWindow() {
//   setTimeout(function() {
//       window.location.reload();
//   }, 5000); // 5000 milliseconds = 5 seconds
// }

// refreshWindow(); // Call the function to start the process