//load all api data

getEcoNums();
get_econ_calendar();

let watchlistButtonClickListener;
BASE_URL = 'http://127.0.0.1:5000';


let userId = document.getElementById('userId');
userId = parseInt(userId.innerText);


//retrieves watchlist from backend and populates DOM on login


let watchlist = document.getElementById("watchlist-data").innerHTML;
watchlistInnerHTML = watchlist.replace(/&amp;/g, '&').replace(/'/g, '"');
let userWatchlist = new Set();

if (watchlistInnerHTML) {
  let array = JSON.parse(watchlistInnerHTML);
  userWatchlist = new Set(array);
}
if (userWatchlist.size > 0) {
  for (let item of userWatchlist) {
    let table = document.getElementById('watchlist-table');

    let row = document.createElement('tr');
    let symbolCell = document.createElement('td');
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

    removeButton.className = 'btn btn-danger';
    row.appendChild(removeButton);

    removeButton.addEventListener('click', () => removeTickerFromDOM(row, item.symbol));

    table.appendChild(row);


  }


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


  let removeButton = document.createElement('button');
  removeButton.textContent = 'Remove';

  removeButton.classList.add('btn','btn-danger');


  row.appendChild(removeButton);

  removeButton.addEventListener('click', function () {
    removeTickerFromDOM(row, ticker);


  });




  table.appendChild(row);


}

function removeTickerFromDOM(row, ticker) {
  if (!ticker) {
    console.error('Ticker is undefined or null');
    return; // Exit the function if ticker is not defined
  }

  row.parentNode.removeChild(row);



  userWatchlist = new Set([...userWatchlist].filter(item => item.symbol !== ticker));

  removeTickerFromDb(ticker);

}



async function removeTickerFromDb(ticker) {



  let url = `http://127.0.0.1:5000/delete_ticker/${ticker}`;


  let response = await axios.post(url)
    .then(response => {
      console.log('Response from server:', response);
    });
  console.log(response);
  return 'ticker deleted';



}
async function updateWatchlist() {
  let symbolsArray = Array.from(userWatchlist).map(item => item.symbol);
  params = { "symbols": symbolsArray };
  let url = `${BASE_URL}/watchlist_refresh`;

  try {
    let response = await axios.post(url, params);
    response.data.forEach(updatedItem => {
      updateWatchlistItem(updatedItem);
    });

  } catch (error) {
    console.error('error updating watchlist: ', error);

  }


}

function updateWatchlistItem(updatedItem) {

  let item = [...userWatchlist].find(i => i.symbol === updatedItem.symbol);
  if (item) {

    item.price = updatedItem.price;
    item.change = updatedItem.change;
    item.changep = updatedItem.changep;

    updateDOMForWatchlistItem(item);


  }


}
function updateDOMForWatchlistItem(item) {
  let symbolCell = document.getElementById(item.symbol);
  if (symbolCell) {
    let row = symbolCell.parentElement;
    row.cells[1].textContent = item.price.toFixed(2);
    row.cells[2].textContent = item.change.toFixed(2);
    row.cells[3].textContent = item.changep.toFixed(2);
    // Update the class for positive/negative changes if needed
  }
}





function startUpdatingWatchlist() {
  updateWatchlist(); // Initial call to the function
  setInterval(updateWatchlist, 10000); // Set interval for 10 seconds (10000 milliseconds)
}

document.addEventListener('DOMContentLoaded', startUpdatingWatchlist);




document.getElementById('zodiac-signs').addEventListener('change', function () {
  var selectedSign = this.value;
  console.log(selectedSign);
  let url = `http://127.0.0.1:5000/horoscope/${selectedSign}`;
  axios.get(url)
    .then(function (response) {

      let reading = document.getElementById('todays-horoscope');
      reading.innerHTML = ` ${response.data}`;
    })
    .catch(function (error) {
      console.error(error); // Handle errors
    });


});


document.getElementById('btn-city').addEventListener('click', getWeather);

function getWeather() {

  let city = document.getElementById('input-city').value;
  let url = `http://127.0.0.1:5000/weather/${city}`;
  axios.get(url)
    .then(function (response) {
      // let weather=document.getElementById('todays-weather')
      // weather.innerHTML=`${city}-${response.data}`

      let location = response.data.location.name;
      let temp = response.data.data.values.temperature;
      let humidity = response.data.data.values.humidity;
      let precipitation = response.data.data.values.precipitationProbability;

      document.getElementById("location").innerHTML = location;
      document.getElementById("temp").innerHTML = temp;
      document.getElementById("humidity").innerHTML = humidity;
      document.getElementById("precipitation").innerHTML = precipitation;

      document.getElementById('todays-weather');

    })
    .catch(function (error) {
      console.error(error); // Handle errors
    });



}

async function get_marketSummary() {
  clearMarketDataSummary()
  let table = document.getElementById('market-summary');
  url = 'http://127.0.0.1:5000/market_summary';

  response = await axios.get(url)
    .then(function (response) {

      for (let item of response.data) {
        let row = table.insertRow();

        let cell1 = row.insertCell(0);
        let cell2 = row.insertCell(1);
        let cell3 = row.insertCell(2);
        let cell4 = row.insertCell(3);

        if (item.longName) {
          cell1.innerHTML = item.longName;

        } else {
          cell1.innerHTML = item.shortName;
        }
        cell2.innerHTML = item.regularMarketPrice.fmt;
        cell3.innerHTML = item.regularMarketChange.fmt;
        cell4.innerHTML = item.regularMarketChangePercent.fmt;
      }

    });


}
//clear market summary prior to periodic update


  function clearMarketDataSummary() {
    const table = document.getElementById('market-summary');
    // Clear all rows except the header, if there is one
    while (table.rows.length > 1) {
        table.deleteRow(1);
    }
}


function updateMarketSummary() {

  get_marketSummary(); // Initial call to the function
  clearMarketDataSummary()
  setInterval(get_marketSummary, 60000); // Set interval for 60 seconds (10000 milliseconds)
}

document.addEventListener('DOMContentLoaded', updateMarketSummary);

async function get_news(){
  clearNews()

  let headlines= document.getElementById('news-table');
  url = 'http://127.0.0.1:5000/us_news';
  await axios.get(url)
  .then(function (response) {

     response.data.news.forEach(story => {
        let row = headlines.insertRow();
        row.classList.add('news-row');
        let cell=row.insertCell(0)

        const link = document.createElement('a');
        link.href = story.link;
        link.textContent = story.title;
        link.target = "_blank"; // Open in new tab

        cell.appendChild(link);



})

  })
}



function updateNews() {

  get_news()
  clearNews()

  ; // Initial call to the function
  setInterval(get_news,180000); // Set interval for 180000 seconds (10000 milliseconds)
}

function clearNews(){

  let table= document.getElementById('news-table')
  while (table.rows.length > 0) {
    table.deleteRow(0);
}


}

document.addEventListener('DOMContentLoaded', updateNews);



async function jokeMe() {
  url = 'http://127.0.0.1:5000/joke';
  let joke = document.getElementById('joke');
  await axios.get(url)
    .then(function (response) {
      joke.innerHTML = response.data;


    });
}

const joker = document.getElementById('joke-me');

joker.addEventListener('click', jokeMe);




async function getEcoNums() {
  url = 'http://127.0.0.1:5000/economic_data';
  let econTable = document.getElementById('ecoStats');
  await axios.get(url)
    .then(function (response) {

      for (let item in response.data) {

        // Create a new row
        const row = document.createElement('tr');

        // Create the first cell for the indicator name
        const nameCell = document.createElement('td');
        nameCell.textContent = item;
        row.appendChild(nameCell);

        // Create the second cell for the indicator value
        const valueCell = document.createElement('td');
        valueCell.textContent = response.data[item];
        row.appendChild(valueCell);

        // Append the new row to the table
        econTable.appendChild(row);
      }
    });



}
async function get_econ_calendar() {
  url = 'http://127.0.0.1:5000/calendar';

  response = await axios.get(url);
  display_econ_calendar(response);
}

function display_econ_calendar(data) {
  const container = document.getElementById('econ-calendar');
  const table = document.getElementById('eco-releases');
  data.data.map((el) => {
    for (const [key, value] of Object.entries(el)) {


      const row = document.createElement('tr');
      const keyCell = document.createElement('td');
      keyCell.textContent = key;
      row.append(keyCell);
      const valueCell = document.createElement('td');
      if (el.value !== 'NA') {
        const link = document.createElement('a');
        link.href = value;
        link.textContent = value;
        link.target = "_blank";
        valueCell.append(link);
      } else {
        valueCell.textContent = 'NA';
      }
      row.append(valueCell);
      table.appendChild(row);

    }
  });
  container.appendChild(table);

}


