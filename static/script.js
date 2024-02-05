let watchlistButtonClickListener;
BASE_URL = 'http://127.0.0.1:5000';


let userId = document.getElementById('userId');
userId = parseInt(userId.innerText);


//retrieves watchlist from backend and populates DOM on login


let watchlist = document.getElementById("watchlist-data").innerHTML;
watchlistInnerHTML = watchlist.replace(/&amp;/g, '&').replace(/'/g, '"');


if(watchlistInnerHTML) array = JSON.parse(watchlistInnerHTML);
let userWatchlist = new Set(array);

for (item of userWatchlist) {
  console.log(item.symbol, item.price.toFixed(2), item.change.toFixed(2), item.changep.toFixed(2), item.name);
  let table = document.getElementById('watchlist-table');

  const row = document.createElement('tr');
  const symbolCell = document.createElement('td');
  symbolCell.textContent = item.symbol;
  symbolCell.id = item.symbol;
  row.appendChild(symbolCell);

  const priceCell = document.createElement('td');
  priceCell.textContent = item.price.toFixed(2);
  row.appendChild(priceCell);

  const changeCell = document.createElement('td');
  changeCell.textContent = item.change.toFixed(2);
  row.appendChild(changeCell);


  const PctchangeCell = document.createElement('td');
  PctchangeCell.textContent = item.changep.toFixed(2);
  row.appendChild(PctchangeCell);

  if (item.change > 0) {
    priceCell.className = 'positive';
    changeCell.className = 'positive';
    PctchangeCell.className = 'positive';
  } else {
    priceCell.className = 'negative';
    changeCell.className = 'negative';
    PctchangeCell.className = 'negative';

  }

  const nameCell = document.createElement('td');
  nameCell.textContent = item.name;
  row.appendChild(nameCell);

  let removeButton = document.createElement('button');
  removeButton.textContent = 'Remove';

  removeButton.id = 'remove';
  row.appendChild(removeButton);
  removeButton.onclick = async function () {
    await removeTickerFromDOM(row, item.symbol);
    await removeTickerFromDb(item.symbol);
  };


  table.appendChild(row);

}




async function retrieveQuote() {

  let user_input = document.getElementById('ticker');
  let ticker = user_input.value.toUpperCase();

  if (!ticker) {
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
    user_input.value = '';
    return;
  }

};

document.addEventListener('DOMContentLoaded', (event) => {
  const quoteButton = document.getElementById('quote');
  quoteButton.addEventListener('click', (event) => {
    event.preventDefault();
    retrieveQuote();
  });
});

function displayQuote(response, ticker) {

  const displayContainer = document.getElementById('quote-section');
  document.getElementById('symbolField').textContent = ticker;
  price = document.getElementById("priceField");
  price.textContent = response.data.regularMarketPrice.toFixed(2);
  changeD = document.getElementById('changeField');
  changeD.textContent = response.data.regularMarketChange.toFixed(2);
  changeP = document.getElementById('Pctchange');
  changeP.textContent = response.data.regularMarketChangePercent.toFixed(2);
  symbol = document.getElementById('nameField').textContent = response.data.shortName;

  if (response.data.regularMarketChange > 0) {
    price.className = 'positive';
    changeD.className = 'positive';
    changeP.className = 'positive';
  } else {
    price.className = 'negative';
    changeD.className = 'negative';
    changeP.className = 'negative';

  }
  const watchlistButton = document.getElementById('add');
  watchlistButton.removeEventListener('click', watchlistButtonClickListener);
  watchlistButtonClickListener = () => addTickerToDatabase(ticker, response);
  watchlistButton.addEventListener('click', watchlistButtonClickListener);

  // function handleWatchlistButtonClick(ticker, response) {
  //   watchlistButton.removeEventListener('click', handleWatchlistButtonClick);
  //   addTickerToDatabase(ticker, response);

  // }
}

async function addTickerToDatabase(ticker, response) {
  console.log('data to add to DOM ', response);
  console.log('the watchlist now contains', userWatchlist);
  let params = {
    "ticker_code": ticker,
    "ticker_name": response.data.shortName,
    "ticker_type": response.data.quoteType,
    "user_id": userId
  };
  console.log('adding this to db', params);
  let url = 'http://127.0.0.1:5000/add_ticker';

  try {
    console.log('calling api');
    let res = await axios.post(url, params);
    console.log('api called');
    return displayQuoteInWatchlist(ticker, response);

  } catch (error) {
    if (error.response && error.response.status === 409) { // Assuming 409 status code for duplicate entry
      alert('Ticker Already in Watchlist');
    } else {
      alert('An error occurred while adding the ticker');
    }
    return error;
  }
}



function displayQuoteInWatchlist(ticker, data) {
  console.log('time to add to watchlist: ', ticker, data);
  userWatchlist.add({
    symbol: ticker,
    price: data.data.regularMarketPrice,
    change: data.data.regularMarketChange,
    changep: data.data.regularMarketChangePercent,
    name: data.data.shortName
  });


  let table = document.getElementById('watchlist-table');
  const row = document.createElement('tr');
  const symbolCell = document.createElement('td');
  symbolCell.textContent = ticker;
  symbolCell.id = ticker;
  console.log('element id is: ', symbolCell.id);
  row.appendChild(symbolCell);

  const priceCell = document.createElement('td');
  priceCell.textContent = data.data.regularMarketPrice.toFixed(2);
  row.appendChild(priceCell);



  const changeCell = document.createElement('td');
  changeCell.textContent = data.data.regularMarketChange.toFixed(2);
  row.appendChild(changeCell);

  const PctchangeCell = document.createElement('td');
  PctchangeCell.textContent = data.data.regularMarketChangePercent.toFixed(2);
  row.appendChild(PctchangeCell);

  if (data.data.regularMarketChange > 0) {
    changeCell.className = 'positive';
    priceCell.className = 'positive';
    PctchangeCell.className = 'positive';
  } else {
    changeCell.className = 'negative';
    priceCell.className = 'negative';
    PctchangeCell.className = 'negative';

  }


  const nameCell = document.createElement('td');
  nameCell.textContent = data.data.shortName;
  row.appendChild(nameCell);
  table.appendChild(row);

  let removeButton = document.createElement('button');
  removeButton.textContent = 'Remove';

  removeButton.id = 'remove';
  row.appendChild(removeButton);
  removeButton.onclick = async function () {
    await removeTickerFromDOM(row, ticker, symbolCell.id);
    await removeTickerFromDb(ticker);
  };




  // addTickerToDatabase(ticker, data.shortName, data.quoteType, userId);


}

async function removeTickerFromDOM(row, ticker, id) {
  console.log('removing ', row, ticker);
  if (ticker === id) {
    await row.parentNode.removeChild(row);
    console.log('removing', ticker);
    removeTickerFromDb(ticker);
  } else {
    console.log('Houston, we got a problem');
    return 1;
  }

}


async function removeTickerFromDb(ticker) {

  console.log('executing remove Ticker for ', ticker);

  let url = `http://127.0.0.1:5000/delete_ticker/${ticker}`;


  let response = axios.post(url)
    .then(response => {
      console.log('Response from server:', response);
    });
  console.log(response);
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


// async function getWatchlist(id) {


//   url = `http://127.0.0.1:5000/get_watchlist/${id}`;


//   let response = await axios.get(url);
//   console.log('user id is', id);
//   console.log('getWatchlist returns: ', response.data);
//   watchlist = response.data;

//   return watchlist;



// }




// // window.addEventListener('load', getWatchlist(userId));


// async function refreshWatchlist(watchlist) {
//   console.log('sending to update', watchlist);

//   let url = 'http://127.0.0.1:5000/update_watchlist/';
//   try {
//     const response = await axios.post(url, { watchlist: watchlist });
//     console.log('Response from server:', response);
//     for(let item in response){
//       console.log('id is ',item.id)
//       console.log('data: ',item['regularMarketPrice'])
//     }
//     for (let item of watchlist) console.log(item)

//   }
//   catch (error) {
//     console.error('Error while sending data:', error);
//     // Handle error appropriately. Maybe return null or a custom error object.
//     return null;
//   }
// }



//create function to  replace watchlist in DOM with the refreshed watchlist
// get ticker and watchlist from refreshWatchlist
//assign a ticker  id to each element



// document.addEventListener('DOMContentLoaded', async () => {
//   // Initialize event listeners and fetch initial data
//   document.getElementById('quote').addEventListener('click', retrieveQuote);
// //   document.getElementById('zodiac-signs').addEventListener('change', fetchHoroscope);
//   document.getElementById('btn-city').addEventListener('click', getWeather);
//   document.getElementById('joke-me').addEventListener('click', fetchJoke);

// Fetch initial data for various sections
//   await getWatchlist(userId);
//   await get_marketSummary();
//   await get_news();
//   await getEcoNums();
//   await get_econ_calendar();
// });





// document.addEventListener('DOMContentLoaded', function() {
//   // Attach an event listener to each remove button
//   document.querySelectorAll('.wl-remove').forEach(function(button) {
//       button.addEventListener('click', function() {
//           var symbol = this.getAttribute('data-symbol');
//           var row = this.closest('tr'); // Find the closest parent <tr> element
//           removeItem(symbol, row);
//       });
//   });
// });

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
  url = `${BASE_URL}/delete_ticker/${symbol}`;
  const response = await axios.post(url);
  return response;
}

// function refreshWindow() {
//   setTimeout(function() {
//       window.location.reload();
//   }, 5000); // 5000 milliseconds = 5 seconds
// }

// refreshWindow(); // Call the function to start the process